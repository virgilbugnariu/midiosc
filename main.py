import argparse
from Learn import Learn
from Start import Start




def main():
    parser = argparse.ArgumentParser(description="Test")
    parser.add_argument("-l", "--learn", action="store_true", help="Learn")
    parser.add_argument("-s", "--start", action="store_true", help="Start")

    args = parser.parse_args()
    
    if args.learn:
        inst = Learn()
    
    if args.start:
        inst = Start()

    inst.init()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error", e)