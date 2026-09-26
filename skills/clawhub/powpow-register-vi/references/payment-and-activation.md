# Kích hoạt gói đăng ký và thanh toán — powpow-register

## Kết luận (nói đáp án trước)

**Phương thức thanh toán sẵn có dùng lại được ngay, skill trợ lý đăng ký không phải phát triển thanh toán gì cả.**

Lý do:

1. Giao diện đăng ký (`src/app/api/auth/register/route.ts`) khi tạo tài khoản pending đã cấp sẵn
   JWT cookie + pendingUserToken HttpOnly cookie, người dùng đáp xuống `/subscription` là đã
   ở trạng thái đăng nhập — ba kênh thanh toán đều treo trên trang đăng ký gói này, kích hoạt đều là cùng một tài khoản pending.
2. Giao diện đăng nhập với tài khoản pending trả về 403 + `redirectTo: '/subscription'`, cũng trồng sẵn
   cookie — người dùng bổ sung thanh toán bất cứ lúc nào cũng được dẫn về cùng một trang.
3. Vì vậy ranh giới trách nhiệm của skill hướng dẫn đăng ký là "dẫn người dùng tới /subscription"; không cần giao diện
   thanh toán mới, không cần mô hình đơn hàng mới, không cần sửa bất kỳ backend nào.

Đồng thời cần lưu ý: khâu thanh toán (nút PayPal JS SDK, WeChat quét mã xác nhận thủ công, Huawei IAP gốc)
**quyết định rằng nó không thể và không nên được skill dòng lệnh/chat thay trả**. Đừng thử dùng script gọi giao diện thanh toán
thay người dùng trả tiền, cũng đừng xin chứng từ thanh toán của người dùng.

## Ba kênh trên trang đăng ký gói

Trang đăng ký gói `src/app/(public)/subscription/page.tsx` tự hiển thị theo môi trường chạy:

| Kênh | Môi trường | Cơ chế | Cách kích hoạt |
|---|---|---|---|
| Gói đăng ký PayPal | Web (không phải HarmonyOS) | `/api/subscription/create` tạo gói đăng ký PayPal → nhảy PayPal cấp quyền; tự động gia hạn theo tháng, có thể hủy bất cứ lúc nào (`/api/subscription/manage`) | PayPal Webhook (`BILLING.SUBSCRIPTION.*`) tự đặt `accountStatus` thành active |
| WeChat quét mã đăng ký gói | Web (không phải HarmonyOS) | khối "WeChat quét mã đăng ký gói" cuối trang: quét mã chuyển khoản, **mở sau khi xác nhận thủ công** (`WechatQrPaymentSection`) | xác nhận thủ công, tiền về có thể trễ; người dùng thanh toán xong đừng vội kết luận thất bại |
| Mua trong ứng dụng Huawei (IAP) | Trong App HarmonyOS | trong WebView HarmonyOS không dùng được PayPal/WeChat Pay, trang chuyển qua `NativeBridge.purchaseSubscription()` gốc | `/api/subscription/activate-huawei` xác minh đơn hàng Huawei rồi kích hoạt |

Kế hoạch và giá đọc động từ `/api/subscription/plans` (kế hoạch PayPal); văn bản cố định trên trang:
Auto-renews. Cancel anytime.

## Trạng thái và chuyển trang

- Thanh toán thành công → `/subscription/success` (callback PayPal kèm `subscriptionId`) → tài khoản
  active → tự nhảy về trang gốc do `next` chỉ định (không có thì về trang chủ).
- Người dùng đã đăng ký gói vào lại trang đăng ký gói → hiện "You're All Set!", sau 3 giây tự về trang chủ.
- Thanh toán thất bại/hủy → `/subscription/cancel`, có thể phát lại.

## Tra cứu

| Hiện tượng | Xử lý |
|---|---|
| Thanh toán xong vẫn 403 | PayPal: Webhook thỉnh thoảng trễ, đăng nhập lại làm mới trạng thái (khi đăng nhập sẽ tra lại trạng thái mới nhất từ DB); WeChat: xác nhận thủ công chưa xong, chờ chút; Huawei: kiểm tra trang thành công thanh toán trong App có hiện không |
| Trang đăng ký gói báo "No subscription plans available" | `/api/subscription/plans` không có kế hoạch PayPal khả dụng, thuộc vấn đề cấu hình phía nền tảng, bảo người dùng thử lại sau |
| WeChat đã trả chưa mở | xác nhận thủ công là bất đồng bộ, vài giờ chưa mở thì liên hệ hỗ trợ nền tảng (dongtao@outlook.com) |

## Ghi chú: Alipay

Trong mã có sẵn một bộ thanh toán web Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`,
mô hình mua đứt một lần thành viên thường ¥9.90 / thành viên cao cấp ¥99, khi sandbox chưa cấu hình khóa sẽ tự hạ cấp
thành thanh toán mô phỏng), **nhưng chưa nối vào UI trang đăng ký gói**, thuộc mã để không/dự phòng. Nếu sau này muốn
bật Alipay trên trang đăng ký gói, nối theo bộ mã sẵn có này là được — chuyện này không liên quan đến skill này, chỉ để
tham khảo quyết định phía nền tảng.