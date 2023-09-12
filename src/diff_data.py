import random
from colorama import Fore
from load_nsight import load_nsight
from load_threatlocker import load_threatlocker

colors = list(vars(Fore).values())

def diff_data():
    nsight_data, nsight_hosts = load_nsight()
    threatlocker_data, threatlocker_hosts = load_threatlocker()
    
    threatlocker_missing = list(set(nsight_hosts).difference(threatlocker_hosts))
    nsight_missing = list(set(threatlocker_hosts).difference(nsight_hosts))
    print("missing from nsight but in threatlocker:\n")
    for el in nsight_missing:
        print(random.choice(colors) + el)
    print(Fore.RESET)
    print("\n\nmissing from threatlocker but in nsight:")
    for el in threatlocker_missing:
        print(random.choice(colors) + el)
    print(Fore.RESET)

if __name__ == "__main__":
    diff_data()