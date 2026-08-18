from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path

app = Flask(__name__)

# ============================================================
# 🎓 CHỈNH THÔNG TIN WEBSITE Ở ĐÂY
# ============================================================

GRADUATE_NAME = "Phan Thị Ngọc Mai"
GRADUATION_DATE = "23 • 08 • 2026"

# ✨ Sửa lời chúc ngay trong code
MESSAGE = """Chúc mừng người của tư bản nha!
Mong rằng chặng đường phía trước sẽ luôn ngập tràn
cơ hội, thành công và những điều tuyệt vời nhất.
Hãy tự tin tỏa sáng nhé! ✨"""

# 📸 ẢNH CỦA BẠN:
# Đặt ảnh vào thư mục static/images/
# rồi sửa tên file ở đây.
PHOTOS = [
    "Mai4.jpg",
    "Mai7.jpg",
    "Mai6.jpg",
    "Mai1.jpg",
    "Mai5.jpg",
]

# 🎵 NHẠC: nếu muốn dùng nhạc MP3 riêng, đặt file vào static/music/
# rồi ghi tên file, ví dụ: MUSIC_FILE = "graduation.mp3"
# Để trống ("") thì website dùng nhạc chúc mừng tạo trực tiếp bằng trình duyệt.
MUSIC_FILE = "tỉnh đê.mp3.mp3"

app.config["GRADUATE_NAME"] = GRADUATE_NAME
app.config["GRADUATION_DATE"] = GRADUATION_DATE
app.config["MESSAGE"] = MESSAGE
app.config["PHOTOS"] = PHOTOS
app.config["MUSIC_FILE"] = MUSIC_FILE


@app.route("/")
def home():
    return render_template(
        "index.html",
        name=app.config["GRADUATE_NAME"],
        date=app.config["GRADUATION_DATE"],
        message=app.config["MESSAGE"],
        photos=app.config["PHOTOS"],
        music_file=app.config["MUSIC_FILE"],
    )


if __name__ == "__main__":
    app.run(debug=True)
