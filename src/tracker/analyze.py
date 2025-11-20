from typing import Optional
import json

from .preprocess import normalize_text
from .model import score_rule, HFModel
from . import storage, config

hf_model = None


def analyze_text(text: str, lang: Optional[str] = None) -> dict:
    storage.init_db()
    clean = normalize_text(text)

    backend = config.CFG.MODEL_BACKEND.lower()
    global hf_model

    if backend == "hf":
        if hf_model is None:
            hf_model = HFModel()
        label, score, meta = hf_model.predict(clean)
    else:
        label, score, meta = score_rule(clean)

    meta_s = json.dumps(meta, ensure_ascii=False)
    row_id = storage.insert_entry(text=clean, lang=lang, sentiment=label, score=score, meta=meta_s)
    return {"id": row_id, "label": label, "score": score, "meta": meta, "backend": backend}
