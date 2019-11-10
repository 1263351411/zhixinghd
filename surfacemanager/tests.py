from django.test import TestCase

# Create your tests here.

if __name__ == '__main__':
    with open("../templates/publications.txt",encoding="utf-8") as f:
        line = f.readline()
        while line:
            print([i.strip() for i in line.split("@")])
            line = f.readline()

