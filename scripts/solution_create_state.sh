#!/usr/bin/env bash
# Produces a correct end state for all three tasks in the local 'work' repo
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
cd "$ROOT/work"

git config user.name "Workshop User"
git config user.email "workshop@example.com"

# Ensure starting on main
git switch main || git checkout -b main

# Task 1: add slugify and merge to main
python3 - <<'PY'
p = 'app/utils.py'
import io,sys
with open(p,'r',encoding='utf-8') as f: s=f.read()
s = "def slugify(text: str) -> str:\n    return text.lower().replace(' ', '-')\n\n" + s
with open(p,'w',encoding='utf-8') as f: f.write(s)
PY
git add app/utils.py
git commit -m "Add slugify util"
git push -u origin main

# Prepare MAIN change for conflict tasks
cp ../variants/silly_math_main_variant.py app/silly_math.py
git add app/silly_math.py
git commit -m "main: make fancy_add round down"
git push

# Task 2: feature-merge branch, make change, then MERGE main into feature
git switch -c feature-merge || git switch feature-merge
cp ../variants/silly_math_feature_merge_variant.py app/silly_math.py
git add app/silly_math.py
git commit -m "feature-merge: fancy_add adds a bonus point"
git push -u origin feature-merge

# Merge main into feature-merge (resolve conflict by choosing merge variant)
set +e
git merge origin/main
if [ $? -ne 0 ]; then
  # auto-resolve: take current file version
  git checkout --ours app/silly_math.py || true
  git add app/silly_math.py
  git commit -m "Resolve conflict in silly_math.py on feature-merge"
fi
set -e
git push

# Task 3: feature-rebase branch, rebase onto main
git switch main
git switch -c feature-rebase || git switch feature-rebase
git reset --hard origin/main
cp ../variants/silly_math_feature_rebase_variant.py app/silly_math.py
git add app/silly_math.py
git commit -m "feature-rebase: fancy_add returns a string with emoji"
git push -u origin feature-rebase
git fetch origin
set +e
git rebase origin/main
if [ $? -ne 0 ]; then
  # resolve by keeping current branch version
  git checkout --theirs app/silly_math.py || true
  git add app/silly_math.py
  git rebase --continue
fi
set -e
git push --force-with-lease

echo "✅ Solution state created. Run: python3 scripts/validate.py"
