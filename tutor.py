#!/usr/bin/env python3
"""
Claude Code Learning Center
An interactive terminal-based tutorial for non-technical programmers.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Prompt, IntPrompt
from rich import box

console = Console()

# =============================================================================
# TUTORIAL CONTENT
# =============================================================================

TUTORIALS = [
    {
        "title": "Getting Started",
        "description": "What is Claude Code and how to launch it",
        "content": """
## What is Claude Code?

Claude Code is an AI assistant that lives in your terminal (command line). It can help you:

- **Read and understand code** - Even if you didn't write it
- **Make changes to files** - Fix bugs, add features, update text
- **Answer questions** - About your project or programming in general
- **Automate tasks** - Run commands, create files, organize projects

## How to Launch Claude Code

Open your terminal and type:

```
claude
```

That's it! Claude Code will start and you'll see a prompt where you can type.

## The Interface

When Claude Code starts, you'll see something like:

```
>
```

This is where you type your requests in plain English. No coding required!
""",
        "examples": [
            "claude",
            "claude --help",
        ],
        "exercise": "Open a new terminal window and type `claude` to start Claude Code. Say hello!",
        "takeaways": [
            "Claude Code runs in your terminal",
            "Start it by typing 'claude'",
            "You communicate in plain English"
        ]
    },
    {
        "title": "Your First Conversation",
        "description": "Basic prompting and asking questions",
        "content": """
## Talking to Claude Code

Claude Code understands natural language. Just describe what you want!

## Good Prompts

Think of Claude Code like a helpful colleague. Be clear about what you need:

**Instead of:** "fix it"
**Try:** "The login button isn't working. Can you check why?"

**Instead of:** "make it better"
**Try:** "Can you make this error message more user-friendly?"

## Asking Questions

You can ask Claude Code questions about:

- **Your project:** "What does this project do?"
- **Specific files:** "Explain what the config.py file does"
- **Code concepts:** "What is an API?"
- **How to do things:** "How do I add a new page to this website?"

## Having a Conversation

Claude Code remembers your conversation. You can:

- Ask follow-up questions
- Say "actually, I meant..." to clarify
- Ask "can you explain that simpler?" if something is confusing
""",
        "examples": [
            "What does this project do?",
            "Explain the main.py file in simple terms",
            "How do I run this application?",
            "What would happen if I deleted this file?",
        ],
        "exercise": "Start Claude Code in a project folder and ask: 'What is this project and what does it do?'",
        "takeaways": [
            "Write prompts like you're talking to a colleague",
            "Be specific about what you want",
            "Ask follow-up questions to clarify"
        ]
    },
    {
        "title": "Working with Files",
        "description": "Reading, editing, and creating files",
        "content": """
## Reading Files

Ask Claude Code to look at any file:

```
Show me what's in the README file
```

```
Can you read the settings.json file?
```

## Editing Files

Describe the change you want. Claude Code will show you what it plans to do and ask for approval:

```
Change the website title to "My Cool Site"
```

```
Update the copyright year to 2025
```

**Important:** Claude Code will always show you changes before making them. You can say "yes" to approve or "no" to cancel.

## Creating Files

Ask Claude Code to create new files:

```
Create a new file called notes.txt with my project ideas
```

```
Make a README file that explains how to use this project
```

## Safety First

Claude Code is careful with your files:

- It shows changes before applying them
- It won't delete important files without asking
- You can always say "undo that" if something goes wrong
""",
        "examples": [
            "Show me the contents of package.json",
            "Change the background color to blue in styles.css",
            "Create a new file called TODO.md",
            "Add a comment explaining what this function does",
        ],
        "exercise": "Ask Claude Code to create a simple text file with a to-do list for your day.",
        "takeaways": [
            "Claude Code can read, edit, and create files",
            "Always review changes before approving",
            "Describe changes in plain English"
        ]
    },
    {
        "title": "Common Tasks",
        "description": "Bug fixes, adding features, and getting explanations",
        "content": """
## Fixing Bugs

Describe the problem you're seeing:

```
The app crashes when I click the submit button. Can you fix it?
```

```
Users are seeing an error message about "undefined". Help!
```

**Tip:** Share any error messages you see - they help Claude Code find the problem.

## Adding Features

Describe what you want the feature to do:

```
Add a dark mode toggle to the settings page
```

```
Make the contact form send an email when submitted
```

## Getting Explanations

Ask Claude Code to explain things:

```
Explain this error message: [paste the error]
```

```
What does this function do and why is it important?
```

```
Walk me through how the login process works
```

## Code Review

Ask Claude Code to review code:

```
Is there anything wrong with this code?
```

```
How could this be improved?
```
""",
        "examples": [
            "Fix the bug that's causing the page to load slowly",
            "Add a 'remember me' checkbox to the login form",
            "Explain why this test is failing",
            "Review this code and suggest improvements",
        ],
        "exercise": "Think of a simple feature you'd like to add to a project. Write out how you would ask Claude Code to add it.",
        "takeaways": [
            "Describe problems with details and error messages",
            "Describe features by what they should do",
            "Ask for explanations whenever confused"
        ]
    },
    {
        "title": "Project Workflows",
        "description": "Using Claude Code in real projects",
        "content": """
## Starting a New Project

Claude Code can help you start from scratch:

```
Help me create a simple website for my bakery business
```

```
Set up a new Python project with a basic structure
```

## Understanding Existing Projects

When you open someone else's project:

```
Give me an overview of this project structure
```

```
What are the main files I should know about?
```

```
How do I run this project locally?
```

## Making a Series of Changes

For bigger tasks, break them down:

1. First: "Let's add user authentication to this app"
2. Then: "Now add a registration page"
3. Finally: "Add a forgot password feature"

## Working with Git

Claude Code can help with version control:

```
What changes have I made since my last commit?
```

```
Commit these changes with a good message
```

```
Create a pull request for this feature
```
""",
        "examples": [
            "Create a new React project for a todo app",
            "Explain this project structure to me",
            "Help me understand how to contribute to this open source project",
            "Commit my changes with a descriptive message",
        ],
        "exercise": "Navigate to a project folder and ask Claude Code to explain the project structure.",
        "takeaways": [
            "Claude Code can help start new projects",
            "Break big tasks into smaller steps",
            "Use Claude Code to understand unfamiliar code"
        ]
    },
    {
        "title": "Advanced Tips",
        "description": "Slash commands, settings, and power features",
        "content": """
## Slash Commands

Type `/` to see available commands:

| Command | What it does |
|---------|-------------|
| `/help` | Get help and see all commands |
| `/clear` | Clear the conversation history |
| `/compact` | Summarize conversation to save space |
| `/status` | See current status and settings |

## Useful Settings

Configure Claude Code to work your way:

```
/config
```

This opens your settings where you can customize behavior.

## Memory Features

Claude Code can remember things across sessions:

```
/memory
```

Add notes like "I prefer TypeScript over JavaScript" or "This project uses PostgreSQL".

## Keyboard Shortcuts

- **Ctrl+C** - Cancel current operation
- **Up Arrow** - See previous prompts
- **Tab** - Autocomplete file names

## Getting Help

If you're ever stuck:

```
/help
```

Or just ask: "How do I...?"
""",
        "examples": [
            "/help",
            "/status",
            "/clear",
            "Remember that I prefer detailed explanations",
        ],
        "exercise": "Try the `/help` command to see all available options in Claude Code.",
        "takeaways": [
            "Slash commands give quick access to features",
            "Customize settings to match your preferences",
            "Use /help whenever you're stuck"
        ]
    },
]

# =============================================================================
# REFERENCE DATA
# =============================================================================

REFERENCE = {
    "Starting": [
        {"command": "claude", "description": "Start Claude Code in the current directory"},
        {"command": "claude --help", "description": "Show help and all command-line options"},
        {"command": "claude --version", "description": "Show the installed version"},
        {"command": "claude <prompt>", "description": "Start with an initial prompt"},
    ],
    "Prompting": [
        {"command": "Ask a question", "description": "Just type naturally: 'What does this do?'"},
        {"command": "Give instructions", "description": "Be specific: 'Add a login button to the header'"},
        {"command": "Share context", "description": "Paste error messages or describe what you see"},
        {"command": "Follow up", "description": "Continue the conversation: 'Now add styling to that'"},
    ],
    "Slash Commands": [
        {"command": "/help", "description": "Show help and available commands"},
        {"command": "/clear", "description": "Clear conversation history"},
        {"command": "/compact", "description": "Summarize conversation to save context"},
        {"command": "/status", "description": "Show current status and settings"},
        {"command": "/config", "description": "Open configuration settings"},
        {"command": "/memory", "description": "View and manage memory notes"},
        {"command": "/cost", "description": "Show token usage and costs"},
    ],
    "Files": [
        {"command": "Read <file>", "description": "'Show me config.json'"},
        {"command": "Edit <file>", "description": "'Change the title in index.html'"},
        {"command": "Create <file>", "description": "'Create a new file called notes.txt'"},
        {"command": "Delete <file>", "description": "'Remove the old backup file'"},
        {"command": "Find files", "description": "'Find all JavaScript files'"},
    ],
    "Git & Version Control": [
        {"command": "Status", "description": "'What changes have I made?'"},
        {"command": "Commit", "description": "'Commit these changes with a good message'"},
        {"command": "Push/Pull", "description": "'Push my changes' or 'Pull latest changes'"},
        {"command": "Branch", "description": "'Create a new branch for this feature'"},
        {"command": "PR", "description": "'Create a pull request'"},
    ],
    "Getting Help": [
        {"command": "/help", "description": "In-app help"},
        {"command": "Ask Claude", "description": "'How do I...' or 'What is...'"},
        {"command": "Explain", "description": "'Explain this error' or 'What does this mean?'"},
        {"command": "Docs", "description": "Visit docs.anthropic.com"},
    ],
}

# =============================================================================
# TIPS CONTENT
# =============================================================================

TIPS = [
    {
        "title": "How to Describe What You Want",
        "content": """
## Be Specific, Not Vague

**Vague:** "Make it better"
**Specific:** "Make the button larger and change its color to blue"

**Vague:** "Fix the bug"
**Specific:** "The form doesn't submit when I click the button on mobile"

## Include Context

- What are you trying to accomplish?
- What have you already tried?
- What error messages do you see?

## Use Examples

"I want a button like the one on the homepage, but green"

"Format the date like 'January 15, 2025' instead of '01/15/25'"
"""
    },
    {
        "title": "When to Be Specific vs. General",
        "content": """
## Start General, Then Get Specific

**Step 1 - General:** "I want to add user accounts to my website"

**Step 2 - Specific:** "Let's start with a simple login form with email and password"

**Step 3 - More Specific:** "Add a 'remember me' checkbox below the password field"

## Be Specific When You Know What You Want

"Change the font size to 16 pixels"
"Use the color #3366CC for links"
"Put the navigation menu on the left side"

## Be General When Exploring Options

"What's the best way to add search to this site?"
"How should I organize these files?"
"What are my options for adding payments?"
"""
    },
    {
        "title": "How to Review Claude's Suggestions",
        "content": """
## Before Approving Changes

1. **Read the summary** - Claude Code explains what it will change
2. **Look at the diff** - Green = added, Red = removed
3. **Ask questions** - "Why did you change this part?"
4. **Test it** - After approving, make sure it works

## It's OK to Say No

- "Don't make that change"
- "Actually, try a different approach"
- "Only change the first part, not the second"

## Ask for Explanations

- "Explain why you made this change"
- "What will this affect?"
- "Is there a simpler way?"

## Trust But Verify

Claude Code is helpful but not perfect. Always:
- Test changes before committing
- Keep backups of important files
- Review changes in context
"""
    },
    {
        "title": "Common Mistakes to Avoid",
        "content": """
## Mistake 1: Being Too Vague

**Problem:** "Fix it" - Fix what?
**Solution:** Describe the specific problem you're seeing

## Mistake 2: Approving Without Reading

**Problem:** Clicking "yes" without reviewing changes
**Solution:** Take a moment to read what will change

## Mistake 3: Not Sharing Error Messages

**Problem:** "It's not working"
**Solution:** Copy and paste the exact error message

## Mistake 4: Trying to Do Too Much at Once

**Problem:** "Rebuild the entire website"
**Solution:** Break it into smaller tasks

## Mistake 5: Not Asking Follow-up Questions

**Problem:** Accepting confusing explanations
**Solution:** Ask "Can you explain that more simply?"

## Mistake 6: Forgetting to Test

**Problem:** Assuming changes work perfectly
**Solution:** Test each change before moving on
"""
    },
]

# =============================================================================
# UI FUNCTIONS
# =============================================================================

def clear_screen():
    """Clear the terminal screen."""
    console.clear()

def show_header(title: str = "Claude Code Learning Center"):
    """Display the app header."""
    console.print()
    console.print(Panel(
        f"[bold cyan]{title}[/bold cyan]\n[dim]Interactive Tutorial for Non-Technical Users[/dim]",
        box=box.ROUNDED,
        padding=(1, 2),
    ))
    console.print()

def show_main_menu():
    """Display the main menu and get user choice."""
    clear_screen()
    show_header()

    menu_text = """
[bold]Welcome![/bold] Learn to use Claude Code even if you're not a programmer.

[bold cyan][1][/bold cyan] Tutorials - Learn step by step
[bold cyan][2][/bold cyan] Reference - Quick command lookup
[bold cyan][3][/bold cyan] Tips - Best practices
[bold cyan][4][/bold cyan] Exit
"""
    console.print(Panel(menu_text, box=box.ROUNDED, padding=(1, 2)))

    while True:
        try:
            choice = IntPrompt.ask("\n[bold]Enter your choice[/bold]", default=1)
            if 1 <= choice <= 4:
                return choice
            console.print("[red]Please enter a number between 1 and 4[/red]")
        except (ValueError, KeyboardInterrupt):
            return 4

def show_tutorial_menu():
    """Display the tutorial selection menu."""
    clear_screen()
    show_header("Tutorials")

    table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan")
    table.add_column("#", style="bold", width=3)
    table.add_column("Lesson", style="bold")
    table.add_column("Description")

    for i, tutorial in enumerate(TUTORIALS, 1):
        table.add_row(str(i), tutorial["title"], tutorial["description"])

    table.add_row("0", "[dim]Back to Main Menu[/dim]", "")

    console.print(table)

    while True:
        try:
            choice = IntPrompt.ask("\n[bold]Select a lesson[/bold]", default=1)
            if 0 <= choice <= len(TUTORIALS):
                return choice
            console.print(f"[red]Please enter a number between 0 and {len(TUTORIALS)}[/red]")
        except (ValueError, KeyboardInterrupt):
            return 0

def show_tutorial(index: int):
    """Display a single tutorial lesson."""
    tutorial = TUTORIALS[index]

    clear_screen()
    show_header(f"Lesson {index + 1}: {tutorial['title']}")

    # Main content
    console.print(Markdown(tutorial["content"]))
    console.print()

    # Examples
    console.print(Panel(
        "[bold]Example Prompts to Try:[/bold]\n\n" +
        "\n".join(f"  [cyan]{ex}[/cyan]" for ex in tutorial["examples"]),
        box=box.ROUNDED,
        title="[bold yellow]Examples[/bold yellow]",
    ))
    console.print()

    # Exercise
    console.print(Panel(
        f"[bold]Try It Yourself:[/bold]\n\n{tutorial['exercise']}",
        box=box.ROUNDED,
        title="[bold green]Exercise[/bold green]",
    ))
    console.print()

    # Takeaways
    console.print(Panel(
        "[bold]Key Takeaways:[/bold]\n\n" +
        "\n".join(f"  [green]*[/green] {t}" for t in tutorial["takeaways"]),
        box=box.ROUNDED,
        title="[bold magenta]Remember[/bold magenta]",
    ))

    console.print()

    # Navigation
    nav_options = []
    if index > 0:
        nav_options.append("[P] Previous")
    if index < len(TUTORIALS) - 1:
        nav_options.append("[N] Next")
    nav_options.append("[B] Back to Tutorials")
    nav_options.append("[M] Main Menu")

    console.print(f"[dim]{' | '.join(nav_options)}[/dim]")

    while True:
        choice = Prompt.ask("\n[bold]Navigate[/bold]", default="n" if index < len(TUTORIALS) - 1 else "b")
        choice = choice.lower()

        if choice == 'p' and index > 0:
            return ('prev', index - 1)
        elif choice == 'n' and index < len(TUTORIALS) - 1:
            return ('next', index + 1)
        elif choice == 'b':
            return ('back', None)
        elif choice == 'm':
            return ('menu', None)
        else:
            console.print("[dim]Invalid choice. Try again.[/dim]")

def show_reference():
    """Display the quick reference guide."""
    clear_screen()
    show_header("Quick Reference")

    console.print("[bold]Search for a command or browse by category.[/bold]\n")

    # Show categories
    categories = list(REFERENCE.keys())
    for i, cat in enumerate(categories, 1):
        console.print(f"[cyan][{i}][/cyan] {cat}")
    console.print(f"[cyan][0][/cyan] [dim]Back to Main Menu[/dim]")
    console.print(f"\n[dim]Or type a search term to find commands[/dim]")

    while True:
        query = Prompt.ask("\n[bold]Enter number or search[/bold]", default="0")

        # Check if it's a number
        if query.isdigit():
            num = int(query)
            if num == 0:
                return
            if 1 <= num <= len(categories):
                show_reference_category(categories[num - 1])
                return show_reference()  # Return to reference menu
        else:
            # Search
            show_search_results(query)
            Prompt.ask("\n[dim]Press Enter to continue[/dim]")
            return show_reference()

def show_reference_category(category: str):
    """Show commands in a specific category."""
    clear_screen()
    show_header(f"Reference: {category}")

    table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan")
    table.add_column("Command / Action", style="bold")
    table.add_column("Description")

    for item in REFERENCE[category]:
        table.add_row(item["command"], item["description"])

    console.print(table)
    Prompt.ask("\n[dim]Press Enter to go back[/dim]")

def show_search_results(query: str):
    """Search and display matching commands."""
    query_lower = query.lower()
    results = []

    for category, items in REFERENCE.items():
        for item in items:
            if (query_lower in item["command"].lower() or
                query_lower in item["description"].lower()):
                results.append((category, item))

    if not results:
        console.print(f"\n[yellow]No results found for '{query}'[/yellow]")
        return

    console.print(f"\n[bold]Found {len(results)} result(s) for '{query}':[/bold]\n")

    table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan")
    table.add_column("Category")
    table.add_column("Command / Action", style="bold")
    table.add_column("Description")

    for category, item in results:
        table.add_row(category, item["command"], item["description"])

    console.print(table)

def show_tips_menu():
    """Display the tips selection menu."""
    clear_screen()
    show_header("Tips & Best Practices")

    for i, tip in enumerate(TIPS, 1):
        console.print(f"[cyan][{i}][/cyan] {tip['title']}")
    console.print(f"[cyan][0][/cyan] [dim]Back to Main Menu[/dim]")

    while True:
        try:
            choice = IntPrompt.ask("\n[bold]Select a topic[/bold]", default=1)
            if choice == 0:
                return
            if 1 <= choice <= len(TIPS):
                show_tip(choice - 1)
                return show_tips_menu()
            console.print(f"[red]Please enter a number between 0 and {len(TIPS)}[/red]")
        except (ValueError, KeyboardInterrupt):
            return

def show_tip(index: int):
    """Display a single tip."""
    tip = TIPS[index]

    clear_screen()
    show_header(f"Tip: {tip['title']}")

    console.print(Markdown(tip["content"]))

    Prompt.ask("\n[dim]Press Enter to go back[/dim]")

# =============================================================================
# MAIN APP
# =============================================================================

def run_tutorials():
    """Run the tutorials section."""
    while True:
        choice = show_tutorial_menu()
        if choice == 0:
            return

        current = choice - 1
        while True:
            result, new_index = show_tutorial(current)
            if result == 'prev' or result == 'next':
                current = new_index
            elif result == 'back':
                break
            elif result == 'menu':
                return

def main():
    """Main application entry point."""
    try:
        while True:
            choice = show_main_menu()

            if choice == 1:
                run_tutorials()
            elif choice == 2:
                show_reference()
            elif choice == 3:
                show_tips_menu()
            elif choice == 4:
                clear_screen()
                console.print(Panel(
                    "[bold cyan]Thanks for learning with Claude Code![/bold cyan]\n\n"
                    "Start practicing by opening a terminal and typing: [bold]claude[/bold]\n\n"
                    "[dim]Happy coding![/dim]",
                    box=box.ROUNDED,
                    padding=(1, 2),
                ))
                break
    except KeyboardInterrupt:
        console.print("\n[dim]Goodbye![/dim]")

if __name__ == "__main__":
    main()
