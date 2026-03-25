#!/usr/bin/env python3
"""Fetch and display Strava athlete stats."""

import argparse
import csv
import os
import sys
import json
import urllib.request
import urllib.parse
import urllib.error

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

STRAVA_API_BASE = "https://www.strava.com/api/v3"
TOKEN_URL = "https://www.strava.com/oauth/token"


def get_credentials():
    """Load Strava credentials from environment variables."""
    client_id = os.environ.get("STRAVA_CLIENT_ID")
    client_secret = os.environ.get("STRAVA_CLIENT_SECRET")
    access_token = os.environ.get("STRAVA_ACCESS_TOKEN")
    refresh_token = os.environ.get("STRAVA_REFRESH_TOKEN")
    return client_id, client_secret, access_token, refresh_token


def refresh_access_token(client_id, client_secret, refresh_token):
    """Exchange a refresh token for a new access token."""
    data = urllib.parse.urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }).encode()

    req = urllib.request.Request(TOKEN_URL, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")

    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def api_get(endpoint, access_token, params=None):
    """Make an authenticated GET request to the Strava API."""
    url = f"{STRAVA_API_BASE}{endpoint}"
    if params:
        url += "?" + urllib.parse.urlencode(params)

    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {access_token}")

    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def get_access_token(client_id, client_secret, access_token, refresh_token):
    """Return a valid access token, refreshing if needed."""
    if access_token:
        return access_token
    if refresh_token and client_id and client_secret:
        console.print("[yellow]Refreshing access token...[/yellow]")
        token_data = refresh_access_token(client_id, client_secret, refresh_token)
        return token_data["access_token"]
    return None


def format_distance(meters):
    km = meters / 1000
    miles = meters / 1609.34
    return f"{km:.1f} km ({miles:.1f} mi)"


def format_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    if h > 0:
        return f"{h}h {m}m"
    return f"{m}m"


def format_elevation(meters):
    feet = meters * 3.28084
    return f"{meters:.0f} m ({feet:.0f} ft)"


def show_athlete(athlete):
    name = f"{athlete.get('firstname', '')} {athlete.get('lastname', '')}".strip()
    city = athlete.get("city", "")
    country = athlete.get("country", "")
    location = ", ".join(filter(None, [city, country]))
    followers = athlete.get("follower_count", 0)
    following = athlete.get("friend_count", 0)

    info = f"[bold]{name}[/bold]"
    if location:
        info += f"\n[dim]{location}[/dim]"
    info += f"\n[cyan]Followers:[/cyan] {followers}  [cyan]Following:[/cyan] {following}"
    console.print(Panel(info, title="[bold green]Athlete Profile[/bold green]", expand=False))


def stats_rows(stats):
    """Yield (period, activity, count, distance_m, moving_time_s, elevation_m) rows."""
    sections = [
        ("all_time", "all_run_totals", "all_ride_totals", "all_swim_totals"),
        ("ytd", "ytd_run_totals", "ytd_ride_totals", "ytd_swim_totals"),
        ("recent_4w", "recent_run_totals", "recent_ride_totals", "recent_swim_totals"),
    ]
    sport_map = {0: "Run", 1: "Ride", 2: "Swim"}
    for period, run_key, ride_key, swim_key in sections:
        for i, key in enumerate([run_key, ride_key, swim_key]):
            totals = stats.get(key, {})
            if totals:
                yield (
                    period,
                    sport_map[i],
                    totals.get("count", 0),
                    totals.get("distance", 0),
                    totals.get("moving_time", 0),
                    totals.get("elevation_gain", 0),
                )


def show_stats(stats):
    period_labels = {
        "all_time": "All-Time Totals",
        "ytd": "Year-to-Date Totals",
        "recent_4w": "Recent Totals (4 weeks)",
    }
    current_period = None
    table = None

    for period, activity, count, dist, time, elev in stats_rows(stats):
        if period != current_period:
            if table:
                console.print(table)
                console.print()
            current_period = period
            table = Table(
                title=period_labels[period], box=box.ROUNDED,
                show_header=True, header_style="bold cyan"
            )
            table.add_column("Activity", style="bold")
            table.add_column("Count", justify="right")
            table.add_column("Distance", justify="right")
            table.add_column("Moving Time", justify="right")
            table.add_column("Elevation Gain", justify="right")

        table.add_row(
            activity,
            str(count),
            format_distance(dist),
            format_time(time),
            format_elevation(elev),
        )

    if table:
        console.print(table)
        console.print()


def get_recent_activities(access_token, limit=10):
    console.print(f"[yellow]Fetching last {limit} activities...[/yellow]")
    return api_get("/athlete/activities", access_token, params={"per_page": limit})


def show_recent_activities(activities):
    table = Table(title="Recent Activities", box=box.ROUNDED, header_style="bold cyan")
    table.add_column("Date", style="dim")
    table.add_column("Name")
    table.add_column("Type", style="bold")
    table.add_column("Distance", justify="right")
    table.add_column("Moving Time", justify="right")
    table.add_column("Elevation", justify="right")

    for act in activities:
        table.add_row(
            act.get("start_date_local", "")[:10],
            act.get("name", "—"),
            act.get("sport_type", act.get("type", "—")),
            format_distance(act.get("distance", 0)),
            format_time(act.get("moving_time", 0)),
            format_elevation(act.get("total_elevation_gain", 0)),
        )

    console.print(table)


def export_csv(athlete, stats, activities, path):
    """Write all fetched data to a CSV file."""
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)

        # Athlete profile
        writer.writerow(["# Athlete Profile"])
        writer.writerow(["name", "city", "country", "followers", "following"])
        writer.writerow([
            f"{athlete.get('firstname', '')} {athlete.get('lastname', '')}".strip(),
            athlete.get("city", ""),
            athlete.get("country", ""),
            athlete.get("follower_count", 0),
            athlete.get("friend_count", 0),
        ])
        writer.writerow([])

        # Aggregate stats
        writer.writerow(["# Aggregate Stats"])
        writer.writerow(["period", "activity", "count", "distance_km", "distance_miles",
                         "moving_time_seconds", "elevation_gain_m", "elevation_gain_ft"])
        for period, activity, count, dist, time, elev in stats_rows(stats):
            writer.writerow([
                period, activity, count,
                round(dist / 1000, 2),
                round(dist / 1609.34, 2),
                time,
                round(elev, 1),
                round(elev * 3.28084, 1),
            ])
        writer.writerow([])

        # Recent activities
        writer.writerow(["# Recent Activities"])
        writer.writerow(["date", "name", "type", "distance_km", "distance_miles",
                         "moving_time_seconds", "elevation_gain_m", "elevation_gain_ft",
                         "average_speed_mps", "average_heartrate", "max_heartrate"])
        for act in activities:
            dist = act.get("distance", 0)
            elev = act.get("total_elevation_gain", 0)
            writer.writerow([
                act.get("start_date_local", "")[:10],
                act.get("name", ""),
                act.get("sport_type", act.get("type", "")),
                round(dist / 1000, 2),
                round(dist / 1609.34, 2),
                act.get("moving_time", 0),
                round(elev, 1),
                round(elev * 3.28084, 1),
                act.get("average_speed", ""),
                act.get("average_heartrate", ""),
                act.get("max_heartrate", ""),
            ])

    console.print(f"[bold green]CSV saved:[/bold green] {path}")


def main():
    parser = argparse.ArgumentParser(description="Fetch Strava athlete stats")
    parser.add_argument("--csv", metavar="FILE", help="Export data to a CSV file")
    parser.add_argument("--limit", type=int, default=10,
                        help="Number of recent activities to fetch (default: 10)")
    args = parser.parse_args()

    console.print(Panel("[bold green]Strava Stats Fetcher[/bold green]", expand=False))

    client_id, client_secret, access_token, refresh_token = get_credentials()
    token = get_access_token(client_id, client_secret, access_token, refresh_token)

    if not token:
        console.print("[bold red]Error:[/bold red] No Strava credentials found.\n")
        console.print("Set one of the following environment variable combinations:\n")
        console.print("  [bold]Option 1 — Access Token (simplest):[/bold]")
        console.print("    STRAVA_ACCESS_TOKEN=<your_token>\n")
        console.print("  [bold]Option 2 — Refresh Token (auto-renews):[/bold]")
        console.print("    STRAVA_CLIENT_ID=<your_client_id>")
        console.print("    STRAVA_CLIENT_SECRET=<your_client_secret>")
        console.print("    STRAVA_REFRESH_TOKEN=<your_refresh_token>\n")
        console.print("[dim]Get credentials at: https://www.strava.com/settings/api[/dim]")
        sys.exit(1)

    try:
        console.print("[yellow]Fetching athlete profile...[/yellow]")
        athlete = api_get("/athlete", token)
        show_athlete(athlete)

        console.print("[yellow]Fetching athlete stats...[/yellow]")
        stats = api_get(f"/athletes/{athlete['id']}/stats", token)
        show_stats(stats)

        activities = get_recent_activities(token, limit=args.limit)
        show_recent_activities(activities)

        if args.csv:
            export_csv(athlete, stats, activities, args.csv)

    except urllib.error.HTTPError as e:
        body = e.read().decode()
        console.print(f"[bold red]HTTP {e.code}:[/bold red] {e.reason}")
        try:
            detail = json.loads(body)
            console.print(f"[red]{detail.get('message', body)}[/red]")
        except json.JSONDecodeError:
            console.print(f"[red]{body}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
