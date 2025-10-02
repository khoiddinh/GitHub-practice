# Task 2 — MERGE workflow (sync main → feature, then PR)

Goal: Create `feature-merge`, introduce a conflicting change in `app/silly_math.py`,
then **merge `main` into `feature-merge`** to resolve conflicts there. Finally, open a PR `feature-merge → main`.

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

# Create feature branch and apply FEATURE-MERGE change
git switch -c feature-merge
cp ../variants/silly_math_feature_merge_variant.py app/silly_math.py
git add app/silly_math.py
git commit -m "feature-merge: fancy_add adds a bonus point"
git push -u origin feature-merge

# Sync main INTO the feature branch via MERGE (no need for --no-ff)
git merge origin/main

# Resolve conflict in app/silly_math.py (choose your final implementation)
git add app/silly_math.py
git commit   # completes the merge
git push
```
Now open a PR **feature-merge → main** on your remote. (Locally you can stop here.)
