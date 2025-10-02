# Task 1 — Edit a file and push

Goal: Add `slugify()` to `app/utils.py`, commit, and push to a branch.

## Steps
```bash
# If you didn't run the setup yet:
bash scripts/setup_local_remote.sh

cd work
git switch -c chore/add-slugify

# Implement in app/utils.py:
# def slugify(text: str) -> str:
#     return text.lower().replace(" ", "-")

git add app/utils.py
git commit -m "Add slugify util"
git push -u origin chore/add-slugify

# (Optional) Open a PR chore/add-slugify -> main, or merge locally:
git switch main
git pull --ff-only
git merge chore/add-slugify -m "Merge chore/add-slugify"
git push
```
