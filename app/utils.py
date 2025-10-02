# app/utils.py
# TODO: In Task 1, add a new function: def slugify(text: str) -> str
# Keep it simple: lowercase and replace spaces with hyphens.
def slugify(text: str) -> str:
    return text.lower().replace(" ", "-")

