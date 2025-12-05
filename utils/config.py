# utils/config.py
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_CONFIG = {
    "server": "DESKTOP-09UU83A",
    "database": "FaceAttendanceDB",
    "auth": "windows",
    "username": None,
    "password": None
}

CSV_PATH = str(PROJECT_ROOT / "data" / "attendance.csv")
FACES_DIR = str(PROJECT_ROOT / "data" / "faces")   # sửa lại thành path tuyệt đối
LANDMARK_PATH = str(PROJECT_ROOT / "shape_predictor_68_face_landmarks.dat")
