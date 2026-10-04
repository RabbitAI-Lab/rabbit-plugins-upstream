# powpow-register

Trợ lý đăng ký PowPow Bong Bóng (bản OpenClaw): đưa người dùng mới từ "không biết Bong Bóng là gì" đến
"đã kích hoạt tài khoản, dùng được bình thường" — giới thiệu sản phẩm (kèm ảnh chụp giao diện), hướng dẫn đăng ký từng bước,
tra cứu lỗi, hướng dẫn kích hoạt gói đăng ký.

Skill thuần hướng dẫn, không script, không phụ thuộc; mọi thao tác đăng ký do người dùng thực hiện trong trình duyệt/App.

## Cài đặt

```
openclaw skills install @durenzidu/powpow-register
```

## Tính năng

1. **Giới thiệu sản phẩm**: mở đầu ~120 từ + link ảnh chụp giao diện lưu trữ trong repo công khai GitHub
   (trang bản đồ, trang chi tiết bài đăng v.v. 6 ảnh, chọn gửi 1–3 ảnh theo tình huống).
2. **Hướng dẫn đăng ký**: quy tắc trường dữ liệu (tên đăng nhập/mật khẩu/mã xác minh email/số điện thoại/ảnh đại diện), đăng nhập bên thứ ba
   (Google/Watcha/Huawei), tham số giới hạn, tất cả đều từ mã nguồn nền tảng và ghi rõ nguồn.
3. **Tra cứu lỗi**: không nhận được mã xác minh, tên đăng nhập/email bị dùng, 403 chưa kích hoạt, tài khoản bị khóa v.v.
   13 vấn đề thường gặp.
4. **Kích hoạt gói đăng ký**: giải thích và tra cứu ba kênh PayPal (web) / WeChat quét mã (xác nhận thủ công) / Huawei IAP (HarmonyOS);
   chuỗi thanh toán sẵn có dùng lại được ngay, skill chỉ chịu trách nhiệm dẫn đường.

## Cấu trúc tệp

```
powpow-register/
├── SKILL.md                            # Hướng dẫn chính (điều kiện kích hoạt, quy trình, chuẩn giọng văn)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Quy tắc trường dữ liệu, giới hạn, bảng tra cứu lỗi (kèm nguồn mã)
    ├── payment-and-activation.md       # Kích hoạt gói đăng ký, kênh thanh toán, kết luận tái sử dụng
    └── screenshots.md                  # Danh sách ảnh lưu trữ + tra cứu nhanh theo tình huống
```

## Bảo mật

- Không chứa bất kỳ khóa nào; không script, không đụng đến thông tin xác thực của người dùng.
- **Không bao giờ xin** mật khẩu, mã xác minh hay chứng từ thanh toán của người dùng; đăng ký và thanh toán hoàn toàn trên trang nền tảng.

## Giấy phép

MIT-0 (giấy phép thống nhất ClawHub).

## Liên kết

- Trang chủ: https://global.powpow.online
- Đăng ký: https://global.powpow.online/register
- Tìm hiểu Bong Bóng (video): https://www.bilibili.com/video/BV1Wu826UEVz/