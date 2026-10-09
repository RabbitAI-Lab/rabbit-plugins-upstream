# powpow-register

Trợ lý đăng ký PowPow Bong Bóng (bản OpenClaw): đưa một người dùng mới từ «không biết Bong Bóng là gì» đến
«tài khoản kích hoạt, đăng nhập một chạm, bắt đầu chơi» — giới thiệu sản phẩm (kèm ảnh chụp giao diện),
agent thao tác hộ việc đăng ký (kèm tải ảnh đại diện), đặt đơn gói thành viên qua Alipay và theo dõi tiền về,
đăng nhập một chạm bằng link kép, xử lý lỗi.

**Từ v2.0.0 là chế độ agent thao tác hộ**: script chính `scripts/powpow-register.mjs` không phụ thuộc
(Node ≥ 18), người dùng cả quá trình không rời hội thoại, chỉ hai lần tạm biệt: vào email xem mã xác minh,
thanh toán tại trang thu ngân Alipay. Không có Node hoặc người dùng muốn tự tay làm thì tự động lùi về
chế độ hướng dẫn thuần.

## Cài đặt

```
openclaw skills install @durenzidu/powpow-register
```

## Tính năng

1. **Giới thiệu sản phẩm**: mở đầu ~120 ký tự + ảnh chụp giao diện đóng gói kèm skill (`assets/screenshots/`
   có 6 tấm: trang bản đồ, trang chi tiết bài đăng v.v., chọn gửi 1–3 tấm theo tình huống; không cần dịch vụ
   lưu ảnh bên ngoài, dùng được khi ngoại tuyến).
2. **Đăng ký hộ**: agent chủ động gợi ý tên người dùng/biệt danh, mật khẩu chọn 1 trong 2 (người dùng cung cấp
   hoặc agent tạo), gửi và nộp mã xác minh, tải thẳng ảnh đại diện (≤5MB, không phải SVG), tự xử lý lỗi thường
   gặp (bị trùng/hết hạn/giới hạn tần suất).
3. **Đăng nhập một chạm (link kép)**: đăng ký thành công là đưa link «phiên nửa» rơi thẳng trang gói thành viên;
   sau khi tiền về, đổi sang trạng thái đăng nhập mới rồi đưa link thành viên đầy đủ rơi thẳng trang chủ (đi qua
   cầu `me?token=` chính thức của nền tảng, tự gieo cookie HttpOnly).
4. **Thanh toán gói**: kênh Alipay agent thao tác hộ đặt đơn (tháng ¥6.99 / quý ¥19.99 / năm ¥69.99,
   mua đứt một lần không tự động gia hạn) + luân phiên tra tiền về; người dùng ở nước ngoài lùi về PayPal;
   quét mã WeChat / Huawei IAP thì chỉ dẫn đường.
5. **Xử lý lỗi**: không nhận được mã xác minh, tên người dùng/email bị trùng, 403 chưa kích hoạt, tài khoản
   bị khóa    v.v. — các vấn đề thường gặp, tất cả đến từ mã nguồn nền tảng và có ghi rõ xuất xứ.

## Cấu trúc file

```
powpow-register/
├── SKILL.md                            # Chỉ dẫn chính (điều kiện kích hoạt, quy trình 8 bước, chuẩn tông giọng, quy tắc cứng)
├── README.md
├── .clawhubignore
├── assets/
│   └── screenshots/                    # Ảnh chụp sản phẩm đóng gói kèm (powpow-01~06.jpg)
├── scripts/
│   └── powpow-register.mjs             # Script chính (không phụ thuộc Node≥18, 11 lệnh con)
└── references/
    ├── agent-flow.md                   # Hợp đồng script, trình tự đầy đủ, cơ chế link kép, thiết kế an toàn
    ├── registration-flow.md            # Quy tắc trường, giới hạn tần suất, bảng xử lý lỗi (kèm nguồn mã)
    ├── payment-and-activation.md       # Hợp đồng Alipay vibepay, chuỗi kích hoạt, xử lý từng kênh
    └── screenshots.md                  # Danh sách ảnh chụp trong gói + tra nhanh theo tình huống
```

## An toàn

- **Mật khẩu** chỉ truyền vào tiến trình script qua biến môi trường, tuyệt đối không đưa vào tham số dòng lệnh,
  không ghi vào đĩa, không vào file trạng thái; mật khẩu do agent tạo chỉ hiển thị một lần để người dùng lưu.
- **Mã xác minh** chỉ dùng cho giao diện đăng ký chính thức, vứt bỏ sau khi dùng; file trạng thái
  (email/tên người dùng/token/số đơn) nằm trong thư mục tạm của hệ thống, kết thúc quy trình `cleanup`
  dọn sạch một phím.
- **Thanh toán**: agent chỉ tạo đơn, mở trang thu ngân, tra tiền về; tuyệt đối không đụng vào tài khoản Alipay
  hay chứng từ thanh toán của người dùng, tuyệt đối không trả tiền hộ. Việc thanh toán luôn diễn ra giữa người
  dùng và trang thu ngân chính thức của Alipay.
- Mọi request chỉ gửi domain chính thức `https://global.powpow.online`; không chứa bất kỳ khóa nào.

## Giấy phép

MIT-0 (giấy phép thống nhất ClawHub).

## Liên kết

- Trang chủ: https://global.powpow.online
- Đăng ký: https://global.powpow.online/register
- Tìm hiểu Bong Bóng (video): https://www.bilibili.com/video/BV1Wu826UEVz/
