import random
import time
from rich.console import Console
from rich.table import Table
from data import presents, debug_messages # Import data from data.py

console = Console()
def display_presents():
    """Displays a list of available gifts."""
    
    console.print("\n[bold magenta]:gift: :gift: :gift: --- LIST OF AVAILABLE GIFTS --- :gift: :gift: :gift:[/bold magenta]")
    
    table = Table(
        title="🎄 Available gifts 🎁",
        show_lines=True,
        title_style="bold white",
        width=50,  # Fixed width for equality
        show_edge=False,
        box=box.DOUBLE
    )
    
    # Add columns: Number and Gift
    table.add_column("№", style="bold green", justify="center", width=5)
    table.add_column("Gift", style="yellow", justify="left", ratio=1)
    
    # Fill in the table
    for i, gift in enumerate(presents, start=1):
        table.add_row(f"{i}", f"[bold white]{gift}[/bold white]")
    
    console.print(table)
    console.print("[bold red]❄️ [/bold red]" * 25)


def get_participants() -> list:
    """Asks the user for the participants' last names."""
    
    console.print("\n[bold yellow]--- 📝 SECRET SANTA 🎅: PARTICIPANT ONBOARDING ---[/bold yellow]")
    console.print("Please enter the last names of all participants, separated by commas or spaces.")
    
    while True:
        try:
            input_str = input("Enter last names (e.g., Smith, Johnson, Williams): ").strip()
            names = [name.strip() for name in input_str.replace(',', ' ').split() if name.strip()]
            
            if len(names) < 2:
                console.print("[bold red]⚠️ At least two participants are required to play.[/bold red]")
                continue
            
            console.print(f"[bold green]✅ Participants accepted: {', '.join(names)}[/bold green]")
            return names
        except Exception as e:
            console.print(f"[bold red]❌ Input error: {e}. Please try again.[/bold red]")


def match_secret_santa(names: list) -> dict:
    """Randomly assigns givers and receivers, ensuring no one is assigned to themselves."""
    
    receivers = names[:]
    givers = names[:]
    matches = {}
    
    while True:
        random.shuffle(receivers)
        is_valid = True
        
        for giver, receiver in zip(givers, receivers):
            if giver == receiver:
                is_valid = False
                break
        
        if is_valid:
            matches = {givers[i]: receivers[i] for i in range(len(givers))}
            break
            
    return matches


def display_results(matches: dict):
    """Displays the final results in a beautifully formatted Rich table."""
    
    console.print("\n[bold cyan reverse]✨ ✨ ✨ --- HOLIDAY MIRACLE DISTRIBUTION! --- ✨ ✨ ✨[/bold cyan reverse]")
    
    for i in range(2): 
        log = random.choice(debug_messages)
        gift = random.choice(presents)
        console.print(f"[{'yellow' if 'WARNING' in log else 'green'}] {log}[/]", style="dim")
        console.print(f"🎁 Selected gift: [bold magenta]{gift}[/bold magenta]")
        time.sleep(0.5)

    console.print("\n[bold green]--- 🎉🎅 FINAL SECRET SANTA ASSIGNMENTS 🎅🎉 ---[/bold green]\n")
    
    table = Table(title="🎄 Secret Santa Match-up 🎁", style="bold white", show_lines=True)
    table.add_column("Giver", style="bold cyan", justify="left")
    table.add_column("Gifts a present", justify="center")
    table.add_column("Receiver", style="bold yellow", justify="left")
    
    for giver, receiver in matches.items():
        gift_hint = random.choice(presents).split(' ')[0]
        table.add_row(
            f"{giver}",
            f"✨ {gift_hint} ->",
            f"{receiver}"
        )
        
    console.print(table)
    console.print("\n[bold green]Happy New Year and happy gifting! 🎅[/bold green]")