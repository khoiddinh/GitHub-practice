#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

# Create a bare remote to act as 'origin'
mkdir -p "$ROOT/local-remote"
cd "$ROOT/local-remote"
if [ ! -d origin.git ]; then
  git init --bare origin.git
fi

# Create working clone
cd "$ROOT"
if [ ! -d work ]; then
  git clone local-remote/origin.git work
fi

# Seed initial files on main
cd work
git config user.name "Workshop User"
git config user.email "workshop@example.com"

if [ ! -f app/hello.py ]; then
  mkdir -p app
  cp -r ../app/* app/
  cp ../README.md README.md
  git add .
  git commit -m "Initial: add hello, silly_math, utils, README"
  git branch -M main
  git remote set-url origin "$ROOT/local-remote/origin.git"
  git push -u origin main
fi

echo "✅ Local remote set up at: $ROOT/local-remote/origin.git"
echo "✅ Working repo at: $ROOT/work"
echo "Next: open tasks in $ROOT/tasks"
