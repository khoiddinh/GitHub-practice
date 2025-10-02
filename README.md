# Git & GitHub Exercise: Merge vs Rebase (Feature-First Workflow)

This exercise uses **only the commands from the lecture**:
`git clone`, `git checkout`, `git checkout -b`, `git add`, `git commit`, `git push`, `git pull`, `git merge`, `git rebase`, and the shell `cp` command.

You will:
1) Make a small change and push it.
2) **Merge `main` into your feature branch** (conflict guaranteed), then open a PR `feature-merge → main`.
3) **Rebase your feature branch onto `main`** (conflict guaranteed), then open a PR `feature-rebase → main`.

> Tip: `cp` means **copy** a file. Example: `cp A B` copies file A to B (overwriting B if it exists).

---

## 🚀 Setup (Fork & Clone)

1. Fork this repository on GitHub into your own account.
2. Clone your fork locally and enter the folder:

```bash
git clone https://github.com/<your-username>/<this-repo>.git
cd <this-repo>
```

3. Make sure `main` is current:

```bash
git checkout main
git pull origin main
```

---

## 📝 Task 1 — First Change and Push

1. Open `app/utils.py` and add:

```python
def slugify(text: str) -> str:
    return text.lower().replace(" ", "-")
```

2. Create a branch, commit, and push:

```bash
git checkout -b chore/add-slugify        # create/switch to a new branch
git add app/utils.py                    # stage your changes
git commit -m "Add slugify util"        # save your change locally
git push origin chore/add-slugify       # push branch to your fork
```

3. Open a Pull Request from `chore/add-slugify` → `main` on your fork (optional for grading, but realistic).

---

## 🔀 Task 2 — MERGE Workflow (Conflict Guaranteed)

In this task you will **branch first**, change `app/silly_math.py`, then later change the **same lines** on `main`. This guarantees a conflict when you merge `main` into your feature branch.

1) **Create the feature branch and make the feature change** (before touching `main`):

```bash
git checkout -b feature-merge
cp variants/silly_math_feature_merge_variant.py app/silly_math.py  # cp = copy the prepared variant into place
git add app/silly_math.py
git commit -m "feature-merge: fancy_add adds a bonus point"
git push origin feature-merge
```

2) **Switch to `main` and make a different change to the same file/lines:**

```bash
git checkout main
cp variants/silly_math_main_variant.py app/silly_math.py
git add app/silly_math.py
git commit -m "main: make fancy_add round down"
git push
```

3) **Merge `main` into the feature branch (conflict happens here):**

```bash
git checkout feature-merge
git merge origin/main
```

- Git will show a conflict in `app/silly_math.py`.
- Open the file, remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), and keep the code you want.
- Then complete the merge and push:

```bash
git add app/silly_math.py
git commit
git push
```

4) Open a Pull Request **feature-merge → main** on your fork.

---

## 🪄 Task 3 — REBASE Workflow (Conflict Guaranteed)

This time you will **rebase the feature branch onto `main`**. To avoid needing any advanced push flags, you will **not push the feature branch until after the rebase**.

1) **Create the feature branch and make the feature change** (do *not* push yet):

```bash
git checkout -b feature-rebase
cp variants/silly_math_feature_rebase_variant.py app/silly_math.py
git add app/silly_math.py
git commit -m "feature-rebase: fancy_add returns a string with emoji"
```

2) **Switch to `main` and make a different change to the same file/lines:**

```bash
git checkout main
cp variants/silly_math_main_variant.py app/silly_math.py
git add app/silly_math.py
git commit -m "main: make fancy_add round down"
git push
```

3) **Rebase the feature branch onto the latest `main`:**

```bash
git checkout feature-rebase
git pull origin main            # make sure your local main is up to date
git rebase main                 # replay your feature commits on top of main
```

- Git will pause on a conflict in `app/silly_math.py`.
- Edit the file to resolve the conflict, then continue the rebase:

```bash
git add app/silly_math.py
git rebase --continue
```

4) **Now push your rebased feature branch** (first push, so no special flags needed):

```bash
git push origin feature-rebase
```

5) Open a Pull Request **feature-rebase → main** on your fork.

---

## ✅ Commands Recap

- `git clone <url>` — copy a remote repo to your machine.
- `git checkout -b <branch>` — create/switch to a new branch.
- `git checkout <branch>` — switch branches.
- `git add <file>` — stage changes for commit.
- `git commit -m "message"` — save a snapshot to your local repo.
- `git push origin <branch>` — upload your branch to your fork on GitHub.
- `git pull origin main` — bring remote `main` into your local `main`.
- `git merge origin/main` — merge `main` into your current branch.
- `git rebase main` — replay your current branch’s commits on top of `main`.
- `cp A B` — copy file A to B (used here to apply prepared variants).

---

## 🎯 What You’ll Learn

- The basic loop: `add` → `commit` → `push`.
- How to **merge `main` into a feature branch** and resolve conflicts.
- How to **rebase a feature branch onto `main`** and resolve conflicts.
- How PRs fit into a clean, safe workflow.
