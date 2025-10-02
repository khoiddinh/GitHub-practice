# Git Exercise: Merge vs Rebase (Feature-First Workflow)

This exercise will help you practice three real-world Git workflows:

1. **Edit & Push** – make a small code change, commit, push, and open a PR.  
2. **Merge Workflow** – merge `main` into your feature branch to resolve conflicts, then PR the feature branch back into `main`.  
3. **Rebase Workflow** – rebase your feature branch onto `main`, then PR it back into `main`.  

You’ll do this in your **own fork of the repo**, just like in real open-source projects.  

---

## 🚀 Setup

1. Fork this repository into your GitHub account.  
2. Clone your fork:

   ```bash
   git clone https://github.com/<your-username>/<this-repo>.git
   cd <this-repo>
   ```

3. Make sure you’re on `main` and up to date:

   ```bash
   git switch main
   git pull origin main
   ```

---

## 📝 Task 1 — Edit & Push

In this task you’ll add a simple utility function and push it on a new branch.

1. Open `app/utils.py`.  
2. Add this new function at the top:

   ```python
   def slugify(text: str) -> str:
       return text.lower().replace(" ", "-")
   ```

3. Commit and push:

   ```bash
   git switch -c chore/add-slugify
   git add app/utils.py
   git commit -m "Add slugify util"
   git push -u origin chore/add-slugify
   ```

4. Open a **Pull Request** from `chore/add-slugify` → `main` in your fork.  

---

## 🔀 Task 2 — Merge Workflow

In this task you’ll create a conflict between `main` and a feature branch, then **merge `main` into the feature branch** to resolve it. Finally, you’ll open a PR from that branch back into `main`.

1. On `main`, apply the MAIN-side change:

   ```bash
   git switch main
   cp variants/silly_math_main_variant.py app/silly_math.py
   git add app/silly_math.py
   git commit -m "main: make fancy_add round down"
   git push
   ```

2. Create the feature branch and apply the FEATURE-MERGE change:

   ```bash
   git switch -c feature-merge
   cp variants/silly_math_feature_merge_variant.py app/silly_math.py
   git add app/silly_math.py
   git commit -m "feature-merge: fancy_add adds a bonus point"
   git push -u origin feature-merge
   ```

3. Merge `main` **into the feature branch**:

   ```bash
   git merge origin/main
   ```

   - You’ll see a merge conflict in `app/silly_math.py`.  
   - Open the file, resolve the conflict however you want (choose one version or combine them).  

   Then finish the merge:

   ```bash
   git add app/silly_math.py
   git commit
   git push
   ```

4. Open a **PR feature-merge → main** in your fork.  

---

## 🪄 Task 3 — Rebase Workflow

Now you’ll try the same scenario, but instead of merging `main` into the feature branch, you’ll **rebase the feature branch onto `main`**.

1. On `main`, apply the MAIN-side change again:

   ```bash
   git switch main
   cp variants/silly_math_main_variant.py app/silly_math.py
   git add app/silly_math.py
   git commit -m "main: make fancy_add round down"
   git push
   ```

2. Create the feature branch and apply the FEATURE-REBASE change:

   ```bash
   git switch -c feature-rebase
   cp variants/silly_math_feature_rebase_variant.py app/silly_math.py
   git add app/silly_math.py
   git commit -m "feature-rebase: fancy_add returns a string with emoji"
   git push -u origin feature-rebase
   ```

3. Rebase the feature branch onto `main`:

   ```bash
   git fetch origin
   git rebase origin/main
   ```

   - You’ll hit a conflict in `app/silly_math.py`.  
   - Resolve it manually, then continue:

   ```bash
   git add app/silly_math.py
   git rebase --continue
   ```

4. Push the rebased branch:

   ```bash
   git push --force-with-lease
   ```

5. Open a **PR feature-rebase → main** in your fork.  

---

## ✅ Validation

Run the provided validator script locally to check your work:

```bash
python3 scripts/validate.py
```

It verifies:
- Task 1: `slugify()` exists and is correct.  
- Task 2: `feature-merge` includes `main` with a merge commit.  
- Task 3: `feature-rebase` is linear on top of `main` (fast-forwardable, no merge commits).  

---

## 🛟 Stuck?

If you get stuck, you can generate the correct end state:

```bash
bash scripts/solution_create_state.sh
python3 scripts/validate.py
```

---

## 🎯 What You’ll Learn

- How to **push a feature branch and open a PR**.  
- How to **merge `main` into a feature branch** to handle conflicts before PR.  
- How to **rebase a feature branch onto `main`** for a clean, linear history.  
- How these different strategies affect your Git history and PR workflow.

---

Happy hacking! 🎉
