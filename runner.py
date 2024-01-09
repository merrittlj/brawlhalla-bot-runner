#!/usr/bin/env python3

import os, sys, yaml

# Local imports
from brawlhalla_bot_merrittlj.game import brawlhalla_bot

from brawlhalla_bot_merrittlj.util import logging_utils
from brawlhalla_bot_merrittlj.util import hotkey_utils


def main():
    yaml_config = yaml.safe_load(open('config.yaml'))
    yaml_inputs_data = yaml_config.get('input_keys')  # Raw input list taken from YAML that lists what input keys the program should use(ex: [input_key_left, input_key_right]) to only input "Move left" and "Move right" keys.
    bot_input_key_dict = {}  # Dictionary translating actions to keys for consistent key actions(e.g. bot looks up key for "Light attack", instead of hard-coding specific keys).
    for input in yaml_inputs_data:
        bot_input_key_dict[input] = yaml_config.get(input)

    bot = brawlhalla_bot.FFA_Bot(input_key_dict = bot_input_key_dict)

    bot_hotkey = hotkey_utils.Hotkey(key_combination = yaml_config.get('toggle_key_combination'), activated_func = bot.program_toggle)
    bot_hotkey.run()

    
if __name__ == "__main__":
    print("\n")
    main()
    print("\n")
else:
    logging_utils.logpr(f"Only use \"{os.path.basename(__file__)}\" as a script!")
    sys.exit()
