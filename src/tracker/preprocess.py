import re

URL_RE = re.compile(r"https?://\S+|www\.\S+")
EMOJI_RE = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)

def normalize_text(text: str) -> str:
    """
    Minimal, language-agnostic normalization:
    - trim, remove URLs
    - strip emojis (for rule-based simplicity)
    - collapse whitespace
    - lowercase
    """
    if not text:
        return ""
    t = text.strip()
    t = URL_RE.sub("", t)
    t = EMOJI_RE.sub("", t)
    t = re.sub(r"\s+", " ", t)
    return t.lower()