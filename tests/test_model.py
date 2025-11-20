from tracker.model import score_rule


def test_score_rule_positive_detection():
    label, score, meta = score_rule("I feel good and happy today")
    assert label == "positive"
    assert score > 0
    assert meta["pos_hits"] >= 2


def test_score_rule_negative_detection():
    label, score, meta = score_rule("I am sad and exhausted")
    assert label == "negative"
    assert score < 0
    assert meta["neg_hits"] >= 2


def test_score_rule_neutral_when_no_hits():
    label, score, meta = score_rule("walking outside with friends")
    assert label == "neutral"
    assert score == 0
    assert meta["total_hits"] == 0
