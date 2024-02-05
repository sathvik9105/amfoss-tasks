# I've used the following commands while doing this task :

1) ls and ls -a : to list out all folders and files in a directory.
2) cd - to change and access directories of a repo.
3) mkdir : to create a new directory.
4) touch - to create a new file in a repo.
5) rm : to remove a file or folder from a repo.
6) python3 part_.txt: to run the python text file 
7) To concatenate all part files into finalcode.txt: cat task-01/codes/part_.txt* > task-01/codes/finalcode.txt
8) To decode the secret code using base64: echo "aHR0cHM6Ly9naXRodWIuY29tL1RoZUh1bnRzbWFuNC9UaGVGaW5hbFNwZWxs" | base64 --decode > 

# git commands used in this task :

1) git clone : to clone or make a copy of git repo in local lamchine.
2) git add . : to add changes to the code or add new files/folders.
3) git status: to chech if the changes made are commited and to check untracked files/folders.
4) git commit -m" " : to commit the changes and to save them.
5) git branch -a: to list all the branches present in the remote repo.
6) git branch: to know the existing branch name.
7) git checkout <branchname>: to switch from existing branch to another branch.
8) git branch -m <oldname> <newname>: to change the branch name from master to main.
9) git push : to save the final changes and make a copy in the remote repo.


## Part-1: Enter the maze
Clone the repository and create "codes" directory

1. Clone the GitHub repository:
    ```markdown
    git clone https://github.com/KshitijThareja/TerminalWizard.git
    ```
2. Create a new directory "codes":
    ```markdown
    cd TerminalWizard
    mkdir codes

    
## Part-2: First Challenge

3. Navigate to the directory:
    ```markdown
    cd codes
    ```


4. Save the secret code to part_1.txt in the "codes" directory and commit changes:
    ```markdown
    touch part_1.txt
    code . # (To open the file in vs code to edit and save it)
    git add .
    git status
    git commit -m "<>"
    git branch -m master main
    git push origin main
    ```
    
## Part-3: Second Challenge

5. Navigate to "codes" directory:
    ```markdown
    cd codes
    ```

6. Save the secret code to part_2.txt in the "codes" directory and commit changes:
    ```markdown
    touch part_2.txt
    code . # (To open the file in vs code to edit and save it)
    git add .
    git status
    git commit -m "<>"
    git push origin main
    ```
   
## Part-4: Third Challenge

### Switch  Branches

7. List all branches presnt in the remote repo:
    ```markdown
    git branch -a
    ```

8. Switch to the branch named after Professor Lupin's subject:
    ```markdown
    git checkout <branch_name>
    ```

9. Copy the file from the other branch to the main branch and execute the python file:
    ```markdown
    git checkout <remote_branch> <relative_path_to_spell_file>
    python3 <spell_file>
    ```

10. Save the secret code to part_3.txt in the "codes" directory and commit changes:
    ```markdown
    touch part_3.txt
    code . # (To open the file in vs code to edit and save it)
    git add .
    git status
    git commit -m "<>"
    git push origin main
    ```

## Part-5: Fourth Challenge

11. View commit logs:
    ```markdown
    git log
    ```

12. Identify the commit with the spell:
    ```markdown
    git show <commit_hash>
    ```

13. Execute the spell file:
    ```markdown
    python3 <spell_file>
    ```

14. Save the secret code to part_4.txt in the "codes" directory and commit changes:
    ```markdown
    touch part_4.txt
    code . # (To open the file in vs code to edit and save it)
    git add .
    git status
    git commit -m "<>"
    git push origin main


## Part-6: The End

### Concatenate all part files and decode the FINAL SECRET CODE 

15. Concatenate all part files into finalcode.txt:
    ```markdown
    cat task-01/codes/part_.txt* > task-01/codes/finalcode.txt
    ```

16. Delete the individual part files:
    ```markdown
    rm part_1.txt
    rm part_2.txt
    rm part_3.txt
    rm part_4.txt
    git add .
    git status
    git commit -m"deleted individual text files"
    git push origin main
    ```

17. Decode the secret code using base64:
    ```markdown
    echo "aHR0cHM6Ly9naXRodWIuY29tL1RoZUh1bnRzbWFuNC9UaGVGaW5hbFNwZWxs" | base64 --decode > 
    ```

18. Commit and push final changes:
    ```markdown
    git add task-01/codes/finalcode.txt
    git status
    git commit -m "Created finalcode.txt"
    git push origin main
    ```

## Final Task

### Clone Final Task Repository and Run Script

19. Clone the repository for the final task:
    ```markdown
    git clone 
    ```

20. Run the Python script in the terminal:
    ```markdown
    python3
    ```

 # ScreenShot: 
 ![Victory] (https://github.com/sathvik9105/amfoss-tasks/blob/main/task-01/screenshot.png)
