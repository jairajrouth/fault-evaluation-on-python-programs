import os


def get_code_4m_commit(repo, commit_id):
    try:
        os.system("git init")
        print(repo)
        os.system("git pull " + repo)
        print("The", repo, "repository is pulled")
        os.system("git reset —- hard" + commit_id)
    except Exception as e:
        raise e


if __name__ == '__main__':
    repo = input("Enter the repository name:")
    commit_id = input("Enter the commitId:")

    get_code_4m_commit(repo, commit_id)
