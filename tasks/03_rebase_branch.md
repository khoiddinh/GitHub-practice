# Task 3 — REBASE workflow (sync main → feature via rebase, then PR)

Goal: Create `feature-rebase`, make a conflicting change, then **rebase `feature-rebase` onto latest `main`**.
Resolve conflicts during rebase, push, and open PR `feature-rebase → main`.

## Steps
```bash
cd work

# Ensure main has the MAIN-side change to create divergence
git switch main
git pull --ff-only
cp ../variants/silly_math_main_variant.py app/silly_math.py
git add app/silly_math.py
git commit -m "main: make fancy_add round down"
git push

# Create feature-rebase branch and apply REBASE-side change
git switch -c feature-rebase
cp ../variants/silly_math_feature_rebase_variant.py app/silly_math.py
git add app/silly_math.py
git commit -m "feature-rebase: fancy_add returns a string with emoji"
git push -u origin feature-rebase

# Rebase feature branch onto latest main
git fetch origin
git rebase origin/main

# Resolve conflicts
# edit app/silly_math.py to the desired final implementation
git add app/silly_math.py
git rebase --continue

# Push the rewritten branch
git push --force-with-lease
```
Now open a PR **feature-rebase → main** on your remote. (Locally you can stop here.)
