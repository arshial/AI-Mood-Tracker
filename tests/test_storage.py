from tracker import config as tracker_config
import tracker.storage as storage


def test_db_path_respects_config(monkeypatch, tmp_path):
    custom_db = tmp_path / "custom.db"
    monkeypatch.setattr(storage, "CFG", tracker_config.Config(DB_PATH=str(custom_db)))

    storage.init_db()
    entry_id = storage.insert_entry(text="happy", lang=None, sentiment="positive", score=0.8)
    entries = storage.fetch_entries()

    assert entry_id > 0
    assert entries[0]["text"] == "happy"
    assert custom_db.exists()
