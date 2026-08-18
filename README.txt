# 🎓 WEB CHÚC MỪNG TỐT NGHIỆP - PYTHON FLASK

## 1. Cài Python

Cài Python 3.10 trở lên.

Kiểm tra:

python --version

## 2. Cài Flask

Mở CMD/PowerShell tại thư mục dự án:

pip install flask

## 3. Thư mục ảnh

Đặt ảnh của bạn vào:

static/images/

Ví dụ:

static/images/anh1.jpg
static/images/anh2.jpg
static/images/anh3.jpg

## 4. Sửa thông tin

Mở:

app.py

Tìm phần:

GRADUATE_NAME = "Nguyễn Chí Khanh"
GRADUATION_DATE = "18 • 08 • 2026"

MESSAGE = """..."""

PHOTOS = [
    "anh1.jpg",
    "anh2.jpg",
    "anh3.jpg",
]

Bạn chỉ cần sửa những dòng này.

Không có ô chỉnh sửa trực tiếp trên website.

## 5. Chạy

Trong CMD:

python app.py

Sau đó mở:

http://127.0.0.1:5000

## 6. Đổi ảnh

Ví dụ bạn có:

khanh.jpg
mai.jpg
banbe.jpg

thì sửa:

PHOTOS = [
    "khanh.jpg",
    "mai.jpg",
    "banbe.jpg",
]

Lưu ý tên file phải đúng tuyệt đối.

## 7. Có thể thêm/bớt ảnh

Bạn có thể dùng 1, 2, 3 hoặc nhiều ảnh.

Ví dụ:

PHOTOS = [
    "anh1.jpg",
    "anh2.jpg",
    "anh3.jpg",
    "anh4.jpg",
    "anh5.jpg",
]

Website sẽ tự tạo thêm khung ảnh.



## 🎆 Hiệu ứng mới
- Nút 🎆 Bắn pháo hoa: pháo hoa nhiều màu + pháo giấy.
- Nút 🎵 Phát nhạc: nếu MUSIC_FILE để trống, website tự tạo giai điệu chúc mừng bằng Web Audio API.
- Muốn dùng nhạc MP3 riêng: tạo `static/music/`, đặt file vào đó, rồi sửa `MUSIC_FILE = "tennhac.mp3"` trong `app.py`.
- Nút 🌸 Hoa rơi: bật/tắt hoa rơi.
