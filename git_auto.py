#!/usr/bin/env python3
import sys
import os
import json
path  = os.getcwd()

def main():    
    args = sys.argv[1:]
    if len(args) == 0:
        print("Use to automate git initialzation and pushing")
        return
    command = args[0]
    if command == "init":
        os.system("git init")
        os.system("touch .gitignore")
        with open(".gitignore", "w") as file:
            file.write("*.pyc\n__pycache__\n.vscode\nmy-git.json\n")
        if not os.path.exists(f"{path}/.git/my-git.json"):
            with open(f"{path}/.git/my-git.json", "w") as file:
                file.write(json.dumps({"online_repo": False}))
        online_repo = args[1] if len(args) > 1 else None
        print(online_repo)
        if online_repo:
            data = {}            
            os.system(f"git remote add origin {online_repo}")
            with open(f"{path}/.git/my-git.json", "r") as file:
                data = json.loads(file.read())
            data["online_repo"] = online_repo
            with open(f"{path}/.git/my-git.json", "w") as file:
                file.write(json.dumps(data))
        print("Git initialized")
    elif command == "save":
        cc = False
        with open(f"{path}/.git/my-git.json", "r") as file:
            data = json.loads(file.read())
            cc = data["online_repo"]
        message = args[1] if len(args) > 1 else "Auto commit"
        os.system("git add .")
        os.system(f'git commit -m "{message}"')
        if(cc):
            try:
                os.system("git push -u origin main")
            except:
                print("Error in pushing online repo")


    
         

if __name__ == "__main__":
    main()
