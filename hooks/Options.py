# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class AnimalKill(DefaultOnToggle):
	"""Killing Animals in each level contributes an item.
	"""
	display_name = "Animal Kill Checks"
	
class ShuffleAnimals(DefaultOnToggle):
	"""Shuffles the playable Animals into the pool. Levels are locked behind Access and the starting animal of the level.
	"""
	display_name = "Shuffle Playable Animals"
	
class ShufflePowerCells(Toggle):
	"""Shuffles the collectable Power Cells into the pool. Not recommended, not yet implemented.
	"""
	display_name = "Shuffle Power Cells"
	
class EvoUnlocksBCP(Toggle):
	"""Evo Parts open BCP, the final level. Not recommended, not yet implemented.
	"""
	display_name = "BCP Requires Evo Parts"

class RandomStartingLevel(Toggle):
	"""Randomizes the starting level (and animal to fit the level if Animals are shuffled). For generation purposes, currently set to be 5 levels start.
	"""
	display_name = "Randomize Starting Level"


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    options.update({
        'animal_kill_checks': AnimalKill,
        'shuffle_playable_animals': ShuffleAnimals,
        'shuffle_power_cells': ShufflePowerCells,
        'evo_unlocks_bcp': EvoUnlocksBCP,
        'random_starting_level': RandomStartingLevel
    })
    return options