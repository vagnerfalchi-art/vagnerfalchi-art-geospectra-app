from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = (ROOT / "app.py").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")

REQUIRED_APP_MARKERS = [
    "Historical Prototype",
    "Scientific authority: NONE",
    "Runtime processing: DISABLED",
    "does not perform mineral detection",
]

FORBIDDEN_RUNTIME_MARKERS = [
    "import ee",
    "ee.Initialize",
    "ImageCollection(",
    "db_mineral",
    "EXECUTAR VARREDURA",
    "Detecção Mineral",
    "Alvos Detectados",
]

for marker in REQUIRED_APP_MARKERS:
    assert marker in APP, f"required quarantine marker missing: {marker}"

for marker in FORBIDDEN_RUNTIME_MARKERS:
    assert marker not in APP, f"forbidden legacy runtime marker present: {marker}"

assert "RETIRED / QUARANTINED" in README
assert "Scientific authority: NONE" in README
assert "Operational use: PROHIBITED" in README
assert "current ENGEOSPECTRA OMEGA system" in README

print("LEGACY_QUARANTINE_VALIDATION_PASS")
