# Kích hoạt gói thành viên và thanh toán — powpow-register

## Kết luận (trả lời trước)

**Kênh Alipay đã lên sóng (từ 2026-10-07), là phương thức thanh toán chính của skill này, và agent thao tác hộ
được việc đặt đơn cùng theo dõi tiền về.** Người dùng ở nước ngoài / không có Alipay thì lùi về PayPal;
quét mã WeChat (xác nhận thủ công) và Huawei IAP cũng có mặt, nhưng skill không thao tác hộ các kênh đó.

Ranh giới trách nhiệm khi thanh toán: agent **tạo được đơn, mở được trang thu ngân, tra được tiền về**;
tuyệt đối không đụng vào tài khoản Alipay / chứng từ thanh toán của người dùng, tuyệt đối không hứa «trả tiền
hộ». Hành động thanh toán mãi mãi do người dùng tự thực hiện tại trang thu ngân chính thức của Alipay.

## Kênh Alipay (vibepay, chính)

Mô hình mua đứt: trả tiền một lần, mở thời hạn tương ứng, **không tự động gia hạn**. Các gói được định nghĩa
trong `src/lib/alipay-vibepay.ts` (`ALIPAY_PACKAGES`):

| key | planId | Tên | Giá | Thời hạn |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Thành viên tháng | ¥6.99 | 30 ngày |
| `quarterly` | alipay-quarterly | Thành viên quý | ¥19.99 | 90 ngày |
| `yearly` | alipay-yearly | Thành viên năm | ¥69.99 | 365 ngày |

### Hợp đồng giao diện (script của skill đã bọc sẵn, agent không tự ghép request)

| Giao diện | Method | Mô tả |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | Cần `Authorization: Bearer <JWT>` (người dùng pending cũng chạy được). body `{package}` → trả `{paymentHtml, outTradeNo, amount, planName}`; `paymentHtml` là trang biểu mẫu tự nộp lên cổng Alipay |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Cùng Bearer đó. Trả `paid` / `pending` / `closed` / `unknown` |
| `/api/payment/alipay/notify` | POST (callback từ máy chủ Alipay) | Kiểm tra chữ ký đủ năm mặt (chữ ký, app_id, khớp số tiền, TRADE_SUCCESS/TRADE_FINISHED, tính duy nhất của đơn thương gia) → cập nhật đơn **idempotent** + tạo gói thành viên + kích hoạt tài khoản. Skill tuyệt đối không đụng giao diện này |
| `/payment/alipay/return` | Trang trình duyệt quay về | Đường dẫn công khai, sau khi thanh toán hiển thị 「支付成功」, trong trang có luân phiên lấy trạng thái thật từ backend |

- Đơn chưa thanh toán **tự đóng sau 2 giờ**; người dùng bỏ giữa chừng → cứ `create-order` lại thẳng,
  khỏi bận tâm đơn cũ.
- Script ghi `paymentHtml` vào file HTML tạm, agent mở bằng lệnh hệ thống là rơi thẳng trang thu ngân
  Alipay (quét QR hoặc đăng nhập Alipay để trả tiền).

### Chuỗi kích hoạt (tự động, không cần thao tác tay)

Chữ ký của notify hợp lệ → đơn `paymentOrders` được đánh dấu đã trả → tạo/tăng hạn `user_subscriptions`
(`planId`, `currentPeriodEnd` tính theo durationDays; gia hạn chỉ cộng trên thời hạn cũ chưa hết) →
`users.accountStatus: active` + `subscriptionStatus: ACTIVE` → trang quay về bắt được paid, hiển thị thành công.

## Sau thanh toán phải lấy trạng thái đăng nhập mới (quan trọng)

JWT có nhúng tuyên bố gói (tài khoản pending là `NONE`). **Tiền về sau thanh toán chỉ cập nhật DB, JWT đã phát
không đổi theo** — tuyên bố của token cũ vẫn là NONE, dùng nó tạo link đăng nhập sẽ thể hiện thành «không có
gói». Vì vậy khi xác nhận `paid`, skill trước tiên chạy `refresh-login` (đăng nhập lại, JWT mới, tuyên bố ACTIVE)
rồi mới tạo link 2. Đây là hành vi của thiết kế, không phải bug cần sửa.

## Bốn kênh trên trang gói thành viên

Trang gói `src/app/(public)/subscription/page.tsx` hiển thị theo môi trường chạy:

| Kênh | Môi trường | Cơ chế | Cách kích hoạt |
|---|---|---|---|
| **Alipay (chính)** | Web | `AlipayPaymentSection` nối với giao diện vibepay (bảng trên) | notify kích hoạt tự động phía máy chủ, tính bằng giây |
| Gói PayPal | Web (không có trên HarmonyOS) | `/api/subscription/create` → ủy quyền PayPal; hàng tháng tự gia hạn, hủy bất cứ lúc nào (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) tự bật active |
| Gói quét mã WeChat | Web (không có trên HarmonyOS) | Cuối trang 「微信扫码订阅」: quét QR chuyển tiền | **Xác nhận thủ công**, tiền về có thể trễ; đừng vội coi là thất bại ngay sau khi trả |
| Mua trong ứng dụng Huawei | Trong app HarmonyOS | Gọi native `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` kiểm tra đơn Huawei rồi kích hoạt |

Gói và giá PayPal do `/api/subscription/plans` trả về động; chữ tĩnh trên trang: Auto-renews. Cancel anytime.

## Trạng thái và chuyển hướng

- Alipay hoàn tất → trang quay về hiển thị thành công; PayPal thành công → `/subscription/success` → tài khoản
  active → theo tham số `next` tự động quay về trang gốc lúc vào (không có thì về trang chủ).
- Người đã là thành viên từ trước mở trang gói → thấy "You're All Set!", 3 giây sau tự về trang chủ.
- Thanh toán thất bại / hủy (PayPal) → `/subscription/cancel`, có thể thử lại.

## Xử lý sự cố

| Hiện tượng | Xử lý |
|---|---|
| Sau khi Alipay trả tiền `query` vẫn pending | notify hiếm khi bị trễ; chờ 30 giây rồi tra lại. Vẫn không được thì nhờ người dùng xem trạng thái trang quay về trong trình duyệt, vẫn không xong thì liên hệ hỗ trợ nền tảng (dongtao@outlook.com) kèm `outTradeNo` |
| Alipay đã trừ tiền nhưng vào link 2 vẫn bị chặn | `refresh-login` bị bỏ sót (tuyên bố của JWT cũ chưa được cập nhật) — trước tiên `refresh-login`, rồi `login-link` |
| Sau thanh toán vẫn 403 (PayPal) | Webhook đôi khi trễ; đăng nhập lại để tải mới trạng thái |
| Trả tiền qua WeChat mà gói không mở | Xác nhận thủ công là bất đồng bộ; vài giờ sau chưa mở thì liên hệ hỗ trợ nền tảng |
| Trang gói hiện "No subscription plans available" | `/api/subscription/plans` không có gói PayPal nào, là trục trặc cấu hình phía nền tảng; người dùng nội địa Trung Quốc có thể tạm dùng Alipay trước |

## Ghi chú lịch sử

Trong code còn một bộ Alipay web thanh toán **cũ** (`src/lib/alipay.ts`, `/api/payment/create-order`,
mua đứt ¥9.90/¥99, khi không có khóa sandbox thì chạy thanh toán mô phỏng), bộ này từ trước đến nay chưa từng
nối vào UI trang gói và không liên quan đến vibepay. Skill tuyệt đối không đụng đến đó; `alipay-vibepay.ts`
mới là kênh hiện hành.
