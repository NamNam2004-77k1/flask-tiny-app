# 📌 Dự án Flask Blog

## 👤 Thông tin cá nhân
***Sinh viên 1***  
- *Họ và tên*: Nguyễn Gia Lâm 
- *Mã số sinh viên*: 22685611
- 
***Sinh viên 2***  
- *Họ và tên*: Trương Công Đạt
- *Mã số sinh viên*: 22685561
## 📝 Mô tả dự án  
- Dự án **Flask Blog** là một nền tảng blog đơn giản được xây dựng bằng ***flask***, ***html***, ***css*** và ***sqlite***.  
- Người dùng có thể thực hiện đăng ký tài khoản rồi đăng nhập. Sau khi đăng nhập người dùng có thể sử dụng các chức năng của ứng dụng như *tạo, chỉnh sửa và xóa bài viết nếu cần*.   

## ⚙️ Hướng dẫn cài đặt và chạy  
***Yêu cầu hệ thống***: Python *3.10* hoặc mới hơn, flask, sqlite  

 ***Để chạy được dự án, bạn cần mở **Windows PowerShell** lên và chạy lần lượt các lệnh dưới đây.***
1. Clone the repository
- Đầu tiên để bạn cần clone reposity.
```PowerShell
git clone https://github.com/NamNam2004-77k1/flask-tiny-app.git #Lệnh này dùng để clone repo 
```
```PowerShell
cd flask-tiny-app #Lệnh này dùng để di chuyển vào thư mục app
```
2. Khởi tạo môi trường ảo (vitural environments)
- Để khởi tạo môi trường ảo và đảm bảo cho việc chạy được ứng dụng, bạn hãy chạy lần lượt các lệnh dưới đây.
```PowerShell
python -m venv venv #Lệnh này dùng để tạo môi trường ảo có tên là venv
```
```PowerShell
venv\Scripts\activate  #Lệnh này dùng để kích hoạt môi trường ảo venv đã tạo
```
3. Tải các framework cần thiết
```PowerShell
python.exe -m pip install --upgrade pip #Lệnh này đảm bảo pip ở phiên bản mới nhất để tải được requirements.txt mà không gặp lỗi
```
```PowerShell
pip install -r requirements.txt #Lệnh này dùng để cài đặt các framework mà app sử dụng
```
4. Khởi tạo cơ sở dữ liệu
```PowerShell
flask --app flaskr init-db #Lệnh này dùng để khởi tạo database
```
5. Chạy ứng dụng 
```PowerShell
flask --app flaskr run --debug #Lệnh này dùng để chạy ứng dụng
```
  
## 🌍 Link triển khai  
- Sau khi đã thực hiện hết các bước bên trên, bạn hãy truy cập *[http://127.0.0.1:5000](http://127.0.0.1:5000)* trên trình duyệt để sử dụng ứng dụng.
