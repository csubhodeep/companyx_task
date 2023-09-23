from pathlib import Path


BASE_PATH = Path(__file__).parent.parent.parent.parent

DATA_PATH = BASE_PATH / "data"
DATA_PATH.mkdir(exist_ok=True)

MODEL_PATH = BASE_PATH / "models"