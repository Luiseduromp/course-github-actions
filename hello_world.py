import os

def main():
    name = os.getenv('USERNAME')
    print(f'Hello {name}, this is the GitHub actions example')

if __name__ == "__main__":
    main()