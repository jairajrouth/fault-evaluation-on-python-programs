from git import Repo


def clone_with_commit_id():
    bug_info_file = open("1/bug.info", "r")
    project_info_file = open("1/project.info", "r")
    split_lines = bug_info_file.read().split()
    buggy_commit_id = split_lines[1].split('"')
    buggy_commit_id = buggy_commit_id[1]
    fixed_commit_id = split_lines[2].split('"')
    fixed_commit_id = fixed_commit_id[1]
    project_url_string = project_info_file.read().split()
    print("project_url_string", project_url_string)
    project_url = project_url_string[0].split("=")
    project_url = project_url[1].strip('"')
    print("project_url", project_url)
    bug_info_file.close()
    project_info_file.close()

    """For Fetching buggy version of the project"""
    buggy_repo = Repo.clone_from(project_url,
                                 "/home/jai/PycharmProjects/fault-evaluation-on-python-programs/buggy_version",
                                 no_checkout=True)
    buggy_repo.git.checkout(buggy_commit_id)
    """For fetching the fixed version of the project"""
    fixed_repo = Repo.clone_from(project_url,
                                 "/home/jai/PycharmProjects/fault-evaluation-on-python-programs/fixed_version",
                                 no_checkout=True)
    fixed_repo.git.checkout(fixed_commit_id)


if __name__ == '__main__':
    clone_with_commit_id()

