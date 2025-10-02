# Git & GitHub Exercise: Merge vs Rebase

This exercise will help you practice the full Git workflow:  
- Cloning a repo  
- Making commits  
- Pushing to GitHub  
- Syncing with `main` using **merge** and **rebase**  
- Opening pull requests  

---

## 🚀 Setup

1. Fork this repository into your GitHub account.  
2. Clone your fork to your computer:

   ```bash
   git clone https://github.com/<your-username>/<this-repo>.git
   cd <this-repo>
   ```

3. Always make sure `main` is up to date:

   ```bash
   git checkout main
   git pull origin main
   ```

---

## 📝 Task 1 — First Change and Push

1. Open `app/utils.py`.  
2. Add a function:

   ```python
   def slugify(text: str) -> str:
       return text.lower().replace(" ", "-")
   ```

3. Save, then run:

   ```bash
   git checkout -b chore/add-slugify     # make a new branch
   git add app/utils.py                  # stage your changes
   git commit -m "Add slugify util"      # commit with a descriptive message
   git push origin chore/add-slugify     # push branch to your fork
   ```

4. Open a Pull Request from `chore/add-slugify` → `main`.  

---

## 🔀 Task 2 — Merge Workflow

You’ll create a conflict and practice merging **main into your feature branch**.

1. On `main`, apply the prepared change:

   ```bash
   git checkout main
   cp variants/silly_math_main_variant.py app/silly_math.py   # cp = copy file
   git add app/silly_math.py
   git commit -m "main: make fancy_add round down"
   git push
   ```

2. Create a feature branch with a conflicting change:

   ```bash
   git checkout -b feature-merge
   cp variants/silly_math_feature_merge_variant.py app/silly_math.py
   git add app/silly_math.py
   git commit -m "feature-merge: fancy_add adds a bonus point"
   git push origin feature-merge
   ```

3. Merge main into your feature branch:

   ```bash
   git merge origin/main
   ```

   - Git will show a conflict in `app/silly_math.py`.  
   - Edit the file, remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), and keep the code you want.  

   Finish the merge:

   ```bash
   git add app/silly_math.py
   git commit
   git push
   ```

4. Open a Pull Request from `feature-merge` → `main`.

---

## 🪄 Task 3 — Rebase Workflow

Now you’ll try the same conflict, but resolve it using **rebase**.

1. On `main`, apply the prepared change again:

   ```bash
   git checkout main
   cp variants/silly_math_main_variant.py app/silly_math.py
   git add app/silly_math.py
   git commit -m "main: make fancy_add round down"
   git push
   ```

2. Create a feature branch with a conflicting change:

   ```bash
   git checkout -b feature-rebase
   cp variants/silly_math_feature_rebase_variant.py app/silly_math.py
   git add app/silly_math.py
   git commit -m "feature-rebase: fancy_add returns a string with emoji"
   git push origin feature-rebase
   ```

3. Rebase the feature branch onto main:

   ```bash
   git fetch origin
   git rebase origin/main
   ```

   - Resolve the conflict in `app/silly_math.py` just like before.  
   - Then continue:

   ```bash
   git add app/silly_math.py
   git rebase --continue
   ```

4. Push the rebased branch:

   ```bash
   git push --force-with-lease
   ```

5. Open a Pull Request from `feature-rebase` → `main`.

---

## ✅ Commands Recap

- `git clone <repo>` → copy repo to your computer  
- `git checkout -b <branch>` → create & switch to new branch  
- `git add <file>` → stage file for commit  
- `git commit -m "message"` → save changes to local repo  
- `git push origin <branch>` → send branch to GitHub  
- `git pull origin main` → update local `main`  
- `git merge origin/main` → bring main into current branch  
- `git rebase origin/main` → replay commits on top of main  

---

## 🎯 What You Learned

- How to create and push branches.  
- How to resolve conflicts with **merge** vs **rebase**.  
- How PRs fit into the workflow.  

Happy hacking! 🎉
