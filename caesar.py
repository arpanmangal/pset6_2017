import sys
import cs50

def main():
    if len(sys.argv) != 2:
        print("Enter a command-line argument!")
        exit(1)
    key = int(sys.argv[1])
    if key < 0:
        print("Enter a non-negative integer key")
        exit(0)
    
    s = cs50.get_string();
    for c in s:
        if c.isupper():
            print(chr((ord(c) - ord("A") + key) % 26 + ord("A")), end = "")
        elif c.islower():
            print(chr((ord(c) - ord("a") + key) % 26 + ord("a")), end = "")
        else:
            print(c, end = "")
        
    print()
    
    
if __name__ == "__main__":
    main()