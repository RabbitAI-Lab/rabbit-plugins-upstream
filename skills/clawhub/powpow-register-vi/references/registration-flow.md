# Chi tiết quy trình đăng ký — powpow-register

Dùng để tra cứu khi gặp vấn đề. Mọi quy tắc đều từ mã nguồn nền tảng (kiểm tra nhất quán frontend/backend Next.js), ghi rõ nguồn.
Khi nền tảng cập nhật, lấy hành vi thực tế trên mạng làm chuẩn.

## Điểm vào

- Trang đăng ký: https://global.powpow.online/register
- Trang đăng nhập: https://global.powpow.online/login
- Trang đăng ký gói: https://global.powpow.online/subscription
- Nếu vào từ link chia sẻ có `?next=...`, sau khi đăng ký + thanh toán xong sẽ tự nhảy về trang ban đầu.

## Các trường biểu mẫu và quy tắc

| Trường | Bắt buộc | Quy tắc | Nguồn mã |
|---|---|---|---|
| Ảnh đại diện | Tùy chọn | ảnh ≤5MB, không hỗ trợ SVG; server tự nén (khi >100KB nén về 400×400 / chất lượng 90) | `src/app/api/auth/register/route.ts` |
| Tên đăng nhập | Bắt buộc | 2~50 ký tự, sau trim chuyển **chữ thường** khi lưu (Tom và tom được xem là cùng tên đăng nhập, cả phía đăng ký lẫn đăng nhập đều không phân biệt hoa thường) | Như trên (zod schema) |
| Mật khẩu | Bắt buộc | 8~100 ký tự, phải đồng thời chứa chữ in hoa, chữ thường, chữ số | Như trên |
| Xác nhận mật khẩu | Bắt buộc | trùng với mật khẩu (chỉ kiểm tra phía frontend) | `src/app/(public)/register/page.tsx` |
| Biệt danh | Tùy chọn | ≤100 ký tự; không điền mặc định lấy tên đăng nhập | register route |
| Email | **Bắt buộc** | định dạng email hợp lệ, ≤255 ký tự; một email chỉ đăng ký được một tài khoản | register route |
| Mã xác minh email | **Bắt buộc** | 6 chữ số; **có hiệu lực 10 phút**; xác minh thành công là hủy; gửi lại sẽ đánh dấu mã cũ đã dùng | `src/lib/email-verification.ts` |
| Số điện thoại | Tùy chọn | số điện thoại Trung Quốc đại lục bắt đầu `1[3-9]` tổng 11 chữ số; một số điện thoại chỉ ràng buộc một tài khoản | register route |

Trang còn cung cấp ba nút đăng nhập bên thứ ba: **Google, Watcha, tài khoản Huawei** (`GoogleSignInButton` /
`WatchaLoginButton` / `HuaweiLoginButton`). Tài khoản bên thứ ba không có mật khẩu cục bộ, sau này đăng nhập bằng mật khẩu sẽ
nhận được "该账号未设置密码，请使用其他方式登录" (tài khoản này chưa đặt mật khẩu, vui lòng dùng cách khác để đăng nhập).

## Tham số giới hạn và chống bạo lực

| Hành vi | Giới hạn | Nguồn |
|---|---|---|
| Gửi đăng ký | **3 lần/phút/IP**, vượt là 429 | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Gửi mã xác minh | cùng IP 1 lần/phút **và** cùng email 1 lần/phút, vượt là 429; nút phía frontend đếm ngược 60 giây | `src/app/api/auth/register/send-code/route.ts` |
| Kiểm tra mã xác minh | mỗi email trong 10 phút tối đa thử **5 lần**, đạt trần dù mã đúng cũng từ chối, phải gửi lại mã | `src/lib/email-verification.ts` |
| Gửi mã quên mật khẩu | 1 lần/phút/IP | `src/app/api/auth/forgot-password/route.ts` |
| Đăng nhập | 5 lần/phút/IP; cùng tài khoản thất bại liên tiếp **5 lần khóa 30 phút** (423), trong lúc đó có nhắc số lần còn lại giảm dần | `src/app/api/auth/login/route.ts`、`rate-limit.ts` |

**Hành vi bảo vệ quyền riêng tư**: khi gửi mã xác minh / quên mật khẩu, dù email đã đăng ký hay không tồn tại, giao diện đều trả về
thông báo thành công thống nhất, không lộ email đã đăng ký hay chưa.

## Chuyển trạng thái sau khi đăng ký thành công

1. Người dùng được lưu với `accountStatus: 'pending'`, ban đầu **3 huy hiệu** (register route).
2. Cùng lúc server trồng hai cookie HttpOnly: JWT (truy cập thẳng được `/subscription`) và
   pendingUserToken (chứng nhận danh tính trong quy trình đăng ký gói).
3. Trang đăng ký phát hiện `pending_payment` → nhảy `/subscription` (giữ tham số quay lại `next`).
4. Thanh toán xong → `accountStatus` chuyển `active` (PayPal qua Webhook tự kích hoạt; WeChat quét mã
   xác nhận thủ công; Huawei IAP qua `activate-huawei`). Chi tiết xem `payment-and-activation.md`.

Người dùng chưa kích hoạt (pending) gọi API cốt lõi (feed, bản đồ, trò chuyện nhân vật số, chấm công v.v.) đều bị 403;
trừ link bài đăng chia sẻ (giữ công khai truy cập được).

## Bảng tra cứu lỗi thường gặp

| Hiện tượng (thông báo gốc tiếng Trung) | Nguyên nhân | Xử lý |
|---|---|---|
| 「用户名已存在」 (Tên đăng nhập đã tồn tại) | tên đăng nhập đã bị dùng (không phân biệt hoa thường) | đổi tên đăng nhập khác |
| 「邮箱已被使用」 (Email đã được sử dụng) | email đã đăng ký rồi | đổi email khác; hoặc đi đăng nhập + "quên mật khẩu" để lấy lại tài khoản cũ |
| 「邮箱验证码错误或已过期」 (Mã xác minh email sai hoặc đã hết hạn) | nhập sai mã / quá 10 phút / thử sai quá 5 lần bị từ chối | bấm "Gửi lại", dùng mã trong **email mới nhất** |
| Không nhận được mã xác minh | bị giới hạn 60 giây; hoặc rơi vào thư rác/thư quảng cáo | đợi hết đếm ngược rồi gửi lại; lật thư mục thư rác |
| 「手机号已被使用」 (Số điện thoại đã được sử dụng) | số điện thoại đã ràng buộc tài khoản khác | bỏ số điện thoại (tùy chọn) hoặc đổi số khác |
| 「注册请求过于频繁」/ 429 (Yêu cầu đăng ký quá thường xuyên) | chạm trần đăng ký 3 lần/phút/IP | đợi vài phút rồi thử lại |
| 409「用户名或邮箱已被注册」 (Tên đăng nhập hoặc email đã được đăng ký) | trùng tên với người khác ngay lúc gửi (phòng va chạm đồng thời) | đổi tên đăng nhập hoặc email rồi thử lại |
| 「图片大小不能超过5MB」/「不支持 SVG」 (Ảnh không được quá 5MB / Không hỗ trợ SVG) | ảnh đại diện không hợp lệ | đổi ảnh hoặc bỏ qua ảnh đại diện |
| Đăng ký thành công nhưng đăng nhập 403「请完成订阅以激活账户」 (Vui lòng hoàn tất đăng ký gói để kích hoạt tài khoản) | tài khoản vẫn là pending | sau khi đăng nhập theo nhắc trên trang đi `/subscription` hoàn tất đăng ký gói |
| Đăng nhập 423「账户已锁定」 (Tài khoản đã bị khóa) | nhập sai mật khẩu 5 lần liên tiếp | đợi 30 phút |
| Đăng nhập 401「还剩 N 次尝试机会」 (Còn N lần thử) | sai mật khẩu, sắp bị khóa | nghĩ kỹ rồi thử, hoặc đi thẳng "quên mật khẩu" |
| 「该账号未设置密码，请使用其他方式登录」 (Tài khoản này chưa đặt mật khẩu, vui lòng dùng cách khác để đăng nhập) | tài khoản bên thứ ba (Google/Watcha/Huawei) | dùng nút bên thứ ba ban đầu để đăng nhập |
| 「该账号已注销」 (Tài khoản này đã bị hủy) | tài khoản đã deactivate | cần đăng ký lại |

## Mẹo nhỏ về đăng nhập (tiện tra cứu)

Đăng nhập hỗ trợ nhập gộp ba trong một **tên đăng nhập / email / số điện thoại** (bất kỳ cái nào cũng được dùng làm tên tài khoản).
Quên mật khẩu: trang đăng nhập → "quên mật khẩu" → nhập email đã đăng ký nhận mã xác minh 6 chữ số → đặt lại.