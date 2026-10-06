import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path


def log_event(path: str, event_type: str, payload: dict) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    row = {"timestamp": datetime.now(timezone.utc).isoformat(), "event_type": event_type, "payload": payload}
    with target.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
