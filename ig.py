import instaloader
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from pyfiglet import Figlet
import os

console = Console()

def banner():
    os.system("clear")
    fig = Figlet(font="slant")
    console.print(fig.renderText("Insta Info"), style="bold magenta")
    console.print(Panel("[bold yellow]Created by:[/] [bold cyan]Niranjan [/bold cyan]", style="bold magenta", box=box.DOUBLE_EDGE))

def get_instagram_profile(username):
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        # Main info table
        table = Table(title=f"[bold green]Instagram Profile: [@{username}]", box=box.HEAVY_EDGE)
        table.add_column("Field", style="bold cyan", no_wrap=True)
        table.add_column("Value", style="bold white")

        table.add_row("Username", profile.username)
        table.add_row("Full Name", profile.full_name or "N/A")
        table.add_row("Followers", str(profile.followers))
        table.add_row("Following", str(profile.followees))
        table.add_row("Posts", str(profile.mediacount))
        table.add_row("Verified", "✅ Yes" if profile.is_verified else "❌ No")
        table.add_row("Business Account", "🏢 Yes" if profile.is_business_account else "No")
        table.add_row("Private Account", "🔒 Yes" if profile.is_private else "Public")
        table.add_row("External URL", profile.external_url or "N/A")

        console.print(table)

        # Bio panel
        bio = profile.biography or "No bio available."
        console.print(Panel(bio, title="[bold yellow]Bio[/bold yellow]", style="bold magenta", box=box.SQUARE))

        # Profile Picture URL
        console.print(Panel(profile.profile_pic_url, title="[bold cyan]Profile Picture URL[/bold cyan]", style="bold green", box=box.MINIMAL_DOUBLE_HEAD))

    except instaloader.exceptions.ProfileNotExistsException:
        console.print(f"[bold red][!] Username '{username}' not found![/bold red]")
    except Exception as e:
        console.print(f"[bold red][!] Error: {e}[/bold red]")

if __name__ == "__main__":
    banner()
    username = console.input("[bold yellow]> Enter Instagram username: [/bold yellow]").strip()
    get_instagram_profile(username) 
   


