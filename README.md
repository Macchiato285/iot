# 🌱 Hệ thống quản lý dữ liệu môi trường  

## 📌 Giới thiệu  
Dự án này là một ứng dụng web nhỏ được xây dựng bằng **Flask** và **Firebase Firestore** để nhập, lưu trữ và hiển thị dữ liệu môi trường.  
Người dùng có thể nhập dữ liệu từ các trạm quan trắc (ID, tên, thời gian, nhiệt độ, độ ẩm, gió, áp suất) và lưu trực tiếp vào Firestore. Ngoài ra, hệ thống hỗ trợ lọc dữ liệu theo ngày để dễ dàng quản lý và theo dõi.  

## 🛠️ Công nghệ sử dụng  
- **Flask (Python)** – Xây dựng backend và routing  
- **Firebase Firestore** – Lưu trữ dữ liệu thời gian thực  
- **Bootstrap 5** – Thiết kế giao diện web  
- **HTML/CSS** – Form nhập liệu & hiển thị dữ liệu  

## 🚀 Tính năng chính  
- Nhập dữ liệu môi trường từ form web  
- Lưu trữ vào Firestore với thời gian chính xác  
- Xem danh sách dữ liệu theo thứ tự thời gian giảm dần  
- Lọc dữ liệu theo khoảng ngày  

## 📷 Giao diện cơ bản  
### 1. Trang nhập dữ liệu  
- Form nhập **ID trạm**, **tên trạm**, **thời gian**, và các thông số môi trường  

### 2. Trang xem dữ liệu  
- Danh sách dữ liệu đã lưu, có thể lọc theo ngày  
<img width="1808" height="806" alt="image" src="https://github.com/user-attachments/assets/8f26b92d-a683-4e50-88bb-e3a8058deb29" />
