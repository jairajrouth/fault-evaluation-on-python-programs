from bs4 import BeautifulSoup


def read_lines():
    with open("buggy_version/htmlcov/black_py.html", "r") as f:
        coverage_file = open("coverage_file.txt", "a")
        for line in f.readlines():
            soup = BeautifulSoup(line, 'html.parser')
            if soup.find_all("p", attrs={"class": "run"}):
                print("0")
                print(soup)
                coverage_file.write("0")
            elif soup.find_all("p", attrs={"class": "mis show_mis"}):
                print("1")
                print(soup)
                coverage_file.write("1")
            elif soup.find_all("p", attrs={"class": "pln"}):
                print("0")
                print(soup)
                coverage_file.write("0")


if __name__ == '__main__':
    read_lines()
    # regex_example()
