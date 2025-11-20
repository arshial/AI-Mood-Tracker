from tracker.preprocess import normalize_text


def test_normalize_text_strips_urls_emojis_and_whitespace():
    raw = "  Check https://example.com 😄 great   day  "
    assert normalize_text(raw) == "check great day"


def test_normalize_text_empty_input_returns_empty():
    assert normalize_text("") == ""
    assert normalize_text("   ") == ""
