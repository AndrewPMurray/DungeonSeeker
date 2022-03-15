from flask.cli import AppGroup
from .users import seed_users, undo_users
from .campaigns import seed_campaigns, undo_campaigns
from .characters import seed_characters, undo_characters
from .sections import seed_sections, undo_sections
from .articles import seed_articles, undo_articles

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_campaigns()
    seed_characters()
    seed_sections()
    seed_articles()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_campaigns()
    undo_characters()
    undo_sections()
    undo_articles()
    # Add other undo functions here
