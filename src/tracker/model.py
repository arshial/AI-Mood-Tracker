from typing import Tuple, Dict
from .preprocess import normalize_text
from transformers import pipeline
from functools import lru_cache
import logging

POS_WORDS = {
    "good", "great", "awesome", "happy", "love", "cool", "nice",
    "amazing", "fine", "calm", "energized", "confident", "optimistic",
    "excited", "proud"
}
NEG_WORDS = {
    "bad", "terrible", "angry", "sad", "tired", "anxious", "stress",
    "stressed", "fear", "hate", "awful", "depressed", "worried",
    "exhausted", "upset"
}


def score_rule(text: str) -> Tuple[str, float, Dict[str, int]]:
    t = normalize_text(text)
    tokens = t.split()
    pos = sum(1 for tok in tokens if tok in POS_WORDS)
    neg = sum(1 for tok in tokens if tok in NEG_WORDS)
    total = pos + neg
    if total == 0:
        label, s = "neutral", 0.0
    else:
        s = (pos - neg) / max(1, total)
        label = "positive" if s > 0.15 else ("negative" if s < -0.15 else "neutral")
    return label, s, {"pos_hits": pos, "neg_hits": neg, "total_hits": total}


# ---------- Transformer-based model ----------
@lru_cache(maxsize=1)
def _get_pipeline():

    logging.info("Loading Hugging Face sentiment pipeline...")
    return pipeline("sentiment-analysis", model="distilbert-base-multilingual-cased")


class HFModel:

    def __init__(self):
        self.pipe = _get_pipeline()

    def predict(self, text: str) -> Tuple[str, float, Dict]:
        t = normalize_text(text)
        result = self.pipe(t)[0]
        label_raw = result["label"].lower()
        score = float(result["score"])

        if "pos" in label_raw:
            label = "positive"
        elif "neg" in label_raw:
            label = "negative"
        else:
            label = "neutral"

        return label, score, {"model": "hf", "raw_label": label_raw}
