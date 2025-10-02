\
#!/usr/bin/env python3
import os, re, subprocess, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "work")

def run(cmd):
    return subprocess.check_output(cmd, shell=True, cwd=WORK, text=True).strip()

def file_contains(path, pattern):
    with open(os.path.join(WORK, path), "r", encoding="utf-8") as f:
        return re.search(pattern, f.read()) is not None

def branch_exists(name):
    try:
        run(f"git rev-parse --verify {name}")
        return True
    except subprocess.CalledProcessError:
        return False

def is_descendant(child, parent):
    try:
        run(f"git merge-base --is-ancestor {parent} {child}")
        return True
    except subprocess.CalledProcessError:
        return False

def has_merge_commit_in_range(range_spec):
    out = run(f"git rev-list {range_spec} --merges || true")
    return bool(out)

def unique_commits_without_merges(range_spec):
    out = run(f"git rev-list {range_spec} --no-merges || true")
    return [c for c in out.splitlines() if c]

def assert_task1():
    ok_slug_fn = file_contains("app/utils.py", r"def\s+slugify\(")
    ok_slug_logic = file_contains("app/utils.py", r"return\s+text\.lower\(\)\.replace\(\s*[\"']\s*\s*[\"'],\s*['\"]-['\"]\s*\)")
    return {"task": "Task 1 (slugify)", "passed": ok_slug_fn and ok_slug_logic}

def assert_task2():
    # MERGE workflow: feature-merge exists; merged origin/main into it; conflict resolved
    if not branch_exists("feature-merge"):
        return {"task": "Task 2 (feature-merge branch)", "passed": False, "msg": "feature-merge branch missing"}
    main_tip = run("git rev-parse origin/main || git rev-parse main")
    # feature-merge should include main (main is ancestor)
    includes_main = is_descendant("feature-merge", main_tip)
    # and have at least one merge commit unique to feature-merge vs main
    has_merge = has_merge_commit_in_range(f"{main_tip}..feature-merge")
    # silly_math modified (any variant; just ensure file exists and fancy_add present)
    changed = file_contains("app/silly_math.py", r"def\s+fancy_add\(")
    return {"task": "Task 2 (merge into feature-merge)", "passed": includes_main and has_merge and changed}

def assert_task3():
    # REBASE workflow: feature-rebase exists; rebased onto main (linear, no merges in unique commits)
    if not branch_exists("feature-rebase"):
        return {"task": "Task 3 (feature-rebase branch)", "passed": False, "msg": "feature-rebase branch missing"}
    main_tip = run("git rev-parse origin/main || git rev-parse main")
    # feature-rebase should be descendant of main (fast-forwardable)
    linear_on_main = is_descendant("feature-rebase", main_tip)
    # and have no merge commits in unique commits
    merges = has_merge_commit_in_range(f"{main_tip}..feature-rebase")
    no_merges = not merges
    # silly_math modified
    changed = file_contains("app/silly_math.py", r"def\s+fancy_add\(")
    return {"task": "Task 3 (rebase onto main in feature-rebase)", "passed": linear_on_main and no_merges and changed}

def main():
    results = [assert_task1(), assert_task2(), assert_task3()]
    all_ok = all(r.get("passed") for r in results)
    print(json.dumps({"passed": all_ok, "checks": results}, indent=2))

if __name__ == "__main__":
    main()
