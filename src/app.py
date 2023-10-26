from fisherman import Fisherman
from pyautogui import getWindowsWithTitle
# from inputimeout import inputimeout, TimeoutOccurred
import configparser
from time import sleep
import sys

class Controller():
    def show_prompt(self):
        if 'y' == input('Do you want to apply the configuration from config.ini? [Y/n] ').lower():
            config = configparser.ConfigParser()
            config.read('../config.ini')
            fishing_strategy= config['game'].get('fishing_strategy')
            release_strategy= config['game'].get('release_strategy')
            fish_count = config['game'].getint('fish_count')
        else:
            fishing_strategy= 'spinning' if '1' == input('Please enter the fishing strategy (1: spinning, 2: feeder): ') else 'feeder'
            release_strategy= 'unmarked' if '1' == input('Please enter the release strategy (1: unmarked, 2: none): ') else 'none'
            fish_count = int(input('Please enter the number of fish in the keepnet: '))

        sleep(0.2)
        print(f'Fishing strategy: {fishing_strategy}')
        sleep(0.2)
        print(f'Release strategy: {release_strategy}')
        sleep(0.2)
        print(f'Current number of fish: {fish_count}')
        sleep(0.2)

        for i in range(3, 0, -1):
            print(f'The script will start in: {i} seconds', end='\r')
            sleep(1)
        print('')
        print('Start executing the script')

        return fishing_strategy, release_strategy, fish_count
    
    def show_save_prompt(self, strategy, release_strategy, fish_count):
        if 'y' == input('Do you want to save the current setting?'):
            config = configparser.ConfigParser()
            name = input('Please enter the name of the new setting withoutt "-" or spaces: ')
            if '-' in name or ' ' in name:
                print('Failed to save the setting due to an invalid name')
                return
            config[name] = {
                'fishing_strategy': strategy,
                'release_strategy': release_strategy,
                'fish_count': fish_count
            }
            #todo




fishing_strategy, release_strategy, fish_count = Controller().show_prompt()
fisherman = Fisherman(fishing_strategy, release_strategy, fish_count)
window = getWindowsWithTitle("Russian Fishing 4")[0]
window.activate()
fisherman.start_fishing()