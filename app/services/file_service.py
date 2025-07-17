context = {"latest": ""}

def store_context(text: str):
    context["latest"] = text

def get_context():
    return context["latest"]
