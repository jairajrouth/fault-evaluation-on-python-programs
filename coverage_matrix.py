from bs4 import BeautifulSoup


def read_lines():
    with open("buggy_version/htmlcov/black_py.html", "r") as f:
        for line in f.readlines()[1:120]:
            soup = BeautifulSoup(line, 'html.parser')
            myps = soup.find_all("p", attrs={"class": "mis show_mis"})
            print(myps)


if __name__ == '__main__':
    read_lines()
