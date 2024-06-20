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
        online_repo = args[1] if len(args) > 1 else None
        print(online_repo)
        if online_repo:            
            os.system(f"git remote add origin {online_repo}")
        print("Git initialized")
    elif command == "save":       
        message = args[1] if len(args) > 1 else "Auto commit"
        os.system("git add .")
        os.system(f'git commit -m "{message}"')       
        try:
            os.system("git push -u origin main")
        except Exception as e:
            print("No online repository found")
    elif command == "status":
        os.system("git status")
    elif command == "github":
        online_repo = args[1] if len(args) > 1 else None
        if online_repo:
            try:
                os.system(f"git remote add origin {online_repo}")
            except Exception as e:
                print("Repository already exists or invalid url")
        else:
            print("No online repository found")
    elif command == "pull":
        os.system("git pull origin main")
    elif command == "log":
        os.system("git log")


    
         

if __name__ == "__main__":
    main()
