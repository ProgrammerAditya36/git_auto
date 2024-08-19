#!/usr/bin/env python3
import sys
import os
import requests
from requests.auth import HTTPBasicAuth



def check_repo_exists(username, repo_name, token):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(url, auth=HTTPBasicAuth(username, token))
    return response.status_code == 200

def create_repo(username, repo_name, token):
    url = "https://api.github.com/user/repos"
    data = {
        "name": repo_name,
        "private": False,
        "auto_init": False
    }
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.post(url, auth=HTTPBasicAuth(username, token), headers=headers, json=data)
    return response.status_code == 201

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: git_auto <command> [arguments]")
        print("Commands:")
        print("  init <repo_url>         Initialize a new Git repository")
        print("  init-online             Initialize a new Git repository and create a remote with the folder name")
        print("  save <message>          Save changes with a commit message")
        print("  status                  Show the status of the repository")
        print("  github <repo_url>       Add GitHub repository as remote")
        print("  pull                    Pull the latest changes from the remote repository")
        print("  log                     Show the commit log")
        print("  clone <repo_url>        Clone a repository")
        print("  create <repo_name>      Create a new GitHub repository")
        print("  auth                    Authenticate with GitHub CLI")
        return

    command = args[0]

    if command == "init":
        online_repo = args[1] if len(args) > 1 else "MyRepo"
        username = os.getenv("USERNAME")
        repo_name = online_repo
        token = os.getenv("GITHUB_TOKEN")
        if check_repo_exists(username, repo_name, token) == False:
            print("Creating a new repository...")
            if create_repo(username, repo_name, token) == False:
                print("Error in creating repository")
                return
            print("Repository created successfully")
        os.system("git init")
        os.system("touch .gitignore")
        with open(".gitignore", "w") as f:
            f.write(".vscode\n__pycache__\n*.pyc\n*.pyo\n*.pyd\nnode_modules\n")
        if online_repo:
            os.system(f"git remote add origin https://github.com/{username}/{online_repo}.git")
            print(f"Remote repository '{online_repo}' added")
            
        os.system("ga save Initialize")        
        print("Git initialized")


    elif command == "save":
        message = args[1] if len(args) > 1 else "Auto commit"
        os.system("git add .")
        os.system(f'git commit -m "{message}"')
        os.system("git push -u origin main")

    elif command == "status":
        os.system("git status")

    elif command == "github":
        online_repo = args[1] if len(args) > 1 else None
        if online_repo:
            os.system(f"git remote add origin {online_repo}")
        else:
            print("No online repository found")

    elif command == "pull":
        os.system("git pull origin main")

    elif command == "log":
        os.system("git log")

    elif command == "clone":
        repo = args[1] if len(args) > 1 else None
        if repo:
            os.system(f"git clone {repo}")
        else:
            print("No repository found")

    elif command == "create":
        repo_name = args[1] if len(args) > 1 else None
        if repo_name:
            os.system(f"gh repo create {repo_name} --public --confirm")
            os.system(f"git remote add origin https://github.com/ProgrammerAditya36/{repo_name}.git")
            print(f"GitHub repository '{repo_name}' created and added as remote")
        else:
            print("No repository name provided")

    elif command == "auth":
        os.system("gh auth login")

if __name__ == "__main__":
    main()
