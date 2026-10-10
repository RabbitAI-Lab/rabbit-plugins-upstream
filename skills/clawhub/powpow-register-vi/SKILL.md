---
name: powpow-register
description: Giúp người dùng hoàn tất đăng ký PowPow (Bong Bóng), kích hoạt gói thành viên qua Alipay và đăng nhập một chạm ngay trong hội thoại. agent điền mẫu giúp người dùng (kèm tải ảnh đại diện), gửi mã xác minh qua email, tạo đơn thanh toán và theo dõi đến khi tiền về; người dùng chỉ cần cung cấp thông tin cơ bản, xem mã một lần trong hộp thư và thanh toán tại trang thu ngân Alipay, cả quá trình không rời hội thoại. Kích hoạt khi người dùng nói «đăng ký Bong Bóng», «tạo tài khoản powpow», «Bong Bóng đăng ký thế nào», «giúp tôi tạo tài khoản powpow», «sign up powpow»; cũng xử lý các vấn đề đăng ký bị kẹt (không nhận được mã xác minh, tên người dùng/email bị trùng) và vấn đề kích hoạt (đăng nhập báo «tài khoản chưa kích hoạt» / pending_payment, thanh toán gói thế nào). Cần Node ≥ 18; khi không có sẽ tự động lùi về chế độ hướng dẫn thuần. Không bao gồm đăng bài/tạo nhân vật số (đó là việc của powpow-simple), không bao gồm phát triển code.
version: 2.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (trợ lý đăng ký Bong Bóng)

Đưa một người dùng mới từ «không biết Bong Bóng là gì» đến «tài khoản đã kích hoạt, đăng nhập một chạm, bắt đầu chơi» — tất cả trong hội thoại. Người dùng chỉ cần rời hội thoại hai lần ngắn ngủi: **vào email xem mã xác minh** và **thanh toán tại trang thu ngân Alipay** (agent sẽ tự mở trang thanh toán).

**Phiên bản 2.0.1** · 2026-10-08 (từ v2 là chế độ agent thao tác hộ: hợp đồng script và trình tự đầy đủ nằm trong `references/agent-flow.md`; quy tắc trường, giới hạn tần suất và xử lý lỗi trong `references/registration-flow.md`; kênh thanh toán trong `references/payment-and-activation.md`; danh sách ảnh chụp sản phẩm trong `references/screenshots.md`. Từ v2.0.1 ảnh chụp sản phẩm đi kèm skill trong `assets/screenshots/`, không phụ thuộc dịch vụ lưu ảnh bên ngoài)

## Môi trường chạy

- Script chính `scripts/powpow-register.mjs`: **không phụ thuộc**, cần **Node ≥ 18**. Trước khi bắt đầu, chạy một lần `node scripts/powpow-register.mjs status` để xác nhận môi trường hoạt động.
- Mọi request của script chỉ gửi về domain chính thức `https://global.powpow.online`.
- **Không có Node / script báo lỗi**: tự động lùi về chế độ hướng dẫn thuần — đưa người dùng trang đăng ký https://global.powpow.online/register và trang gói thành viên https://global.powpow.online/subscription, đồng hành theo `references/registration-flow.md`. Đừng cố thử script đi thử lại mãi.
- Khôi phục sau khi hội thoại bị ngắt: chạy `status` trước để xem quy trình đang ở bước nào rồi tiếp tục.

## Trigger Conditions

- Ý định đăng ký: «đăng ký Bong Bóng», «tạo tài khoản powpow», «Bong Bóng đăng ký thế nào», «sign up powpow»
- Đăng ký bị kẹt: «không nhận được mã xác minh», «báo tên người dùng đã tồn tại», «mật khẩu cứ không đạt yêu cầu»
- Vấn đề sau đăng ký: «đăng nhập báo tài khoản chưa kích hoạt», «403 pending_payment», «Bong Bóng thanh toán/đăng ký gói thế nào»

**Không kích hoạt cho**: đăng bài/tạo nhân vật số (→ powpow-simple); phát triển code phía Web (xem các skill phát triển). Người dùng vừa muốn đăng ký vừa muốn đăng bài: chạy xong skill này trước, sau khi kích hoạt rồi giao cho powpow-simple.

## Tổng quan quy trình

| Bước | agent làm gì | Người dùng làm gì |
|---|---|---|
| 1 Giới thiệu sản phẩm | Giới thiệu + gửi ảnh chụp | Nhìn qua một chút |
| 2 Xác nhận thông tin | Chủ động gợi ý tên người dùng/biệt danh, mật khẩu chọn 1 trong 2, hỏi email | Xác nhận, cung cấp |
| 3 Gửi mã | `send-code` | —— |
| 4 Đọc lại mã | —— | Vào email xem mã 6 chữ số, gửi lại |
| 5 Gửi đăng ký | `register` (kèm tải thẳng ảnh đại diện), tự xử lý lỗi | —— |
| 6 Phiên nửa + thanh toán | `login-link(pending)` → `create-order` → mở trang thu ngân → hỏi `query` | Mở link, thanh toán |
| 7 Đăng nhập chính thức | `refresh-login` → `login-link(home)` | Mở link vào trang chủ |
| 8 Kết thúc | `cleanup` + giao thông tin tài khoản + hướng dẫn trải nghiệm + gợi ý plugin | Bắt đầu chơi |

## Bước 1: giới thiệu sản phẩm + ảnh chụp (không được bỏ qua)

Đa số người dùng chưa từng thấy Bong Bóng. Việc đầu tiên không phải kể quy trình, mà là để họ **thấy** sản phẩm:

1. Giới thiệu Bong Bóng trong ~120 ký tự: biến những bức ảnh chụp tức thì thành một bài du ký, ghim lên bản đồ công cộng thành một «bong bóng»; bong bóng sẽ hạ nhiệt theo thời gian, lượt «thích» của người khác có thể hồi sinh nó; trên bản đồ còn có «nhân vật số» có thể trò chuyện. Địa chỉ nền tảng: https://global.powpow.online ; muốn xem video trước: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Gửi ảnh chụp**. Ảnh chụp đã đóng gói kèm skill tại `assets/screenshots/powpow-0N.jpg` — gửi trực tiếp như file ảnh cục bộ, không cần mạng. Danh sách, nội dung từng ảnh và thời điểm sử dụng nằm trong `references/screenshots.md`. Bộ đôi hay dùng nhất lúc mở đầu: trang bản đồ (powpow-03) + trang chi tiết bài đăng (powpow-06).

Quy tắc ảnh chụp (quy tắc cứng):

- Ảnh chụp **đã đóng gói kèm skill** trong `assets/screenshots/` (`powpow-0N.jpg`) — gửi trực tiếp như file ảnh cục bộ; dùng được trong mọi môi trường, kể cả nơi GitHub không mở được.
- Mỗi lần chỉ gửi 1–3 ảnh liên quan chủ đề hiện tại, đừng nhét tất cả một lượt.
- Nếu file trong gói lỡ thiếu, lùi về các link lưu trữ được liệt kê trong `references/screenshots.md` (lưu ý: trong nội địa Trung Quốc có thể không mở được).

Giới thiệu xong, trao quyền lựa chọn cho người dùng: **«Nếu bạn muốn đăng ký, ba phút nữa ta tạo xong tài khoản ngay trong hội thoại; bạn chỉ cần xem mã xác minh trong email một lần.»**

## Bước 2: xác nhận thông tin đăng ký (mỗi lượt một câu hỏi, đừng hỏi hết một lượt)

- **Tên người dùng** (bắt buộc): **chủ động gợi ý một cái** từ bối cảnh hội thoại/tên người dùng hệ thống (2~50 ký tự, không phân biệt hoa thường); người dùng gật đầu thì dùng, muốn đổi thì đổi.
- **Mật khẩu** (bắt buộc; trước tiên cho chọn 1 trong 2):
  - Người dùng tự cung cấp → sau đó truyền cho script qua biến môi trường, **tuyệt đối không đưa vào tham số dòng lệnh**;
  - agent tạo → chạy `node scripts/powpow-register.mjs gen-password` và **gửi ngay mật khẩu vừa tạo cho người dùng lưu lại** (chỉ hiển thị một lần, sau đó không xuất hiện nữa).
- **Email** (bắt buộc): người dùng phải tự cung cấp — đây là mỏ neo định danh của tài khoản, **đừng đoán hộ**.
- **Biệt danh** (không bắt buộc): gợi ý mặc định giống tên người dùng.
- **Ảnh đại diện** (không bắt buộc): người dùng đưa đường dẫn ảnh cục bộ (≤5MB, không phải SVG) thì script tải thẳng; không có thì bỏ qua (nền tảng dùng logo mặc định); nếu bạn có khả năng tạo ảnh, có thể chủ động đề nghị làm giúp một tấm.
- **Số điện thoại** (không bắt buộc, số nội địa Trung Quốc): mặc định bỏ qua; chỉ hỏi khi người dùng chủ động muốn liên kết.

Xác nhận xong có thể chạy `prepare-suggest --username U --nickname N --email E` để ghi vào file trạng thái (sau đó register không cần truyền lại).

## Bước 3–4: mã xác minh qua email (đoạn duy nhất buộc phải rời hội thoại)

```
node scripts/powpow-register.mjs send-code --email <email>
```

Sau đó nói rõ với người dùng: **vào email tìm mã xác minh 6 chữ số, có hiệu lực 10 phút; nhớ xem cả thư mục spam/thư quảng cáo**; khi tìm thấy thì quay lại gửi mã cho bạn. Việc gửi có thời gian chờ 60 giây, đừng bấm liên tục.

## Bước 5: gửi đăng ký (agent thao tác hộ)

```
POWPOW_REGISTER_PASSWORD=<mật khẩu> node scripts/powpow-register.mjs register --code <mã> [--username U] [--nickname N] [--avatar <đường dẫn ảnh cục bộ>] [--phone P]
```

Thành công là tài khoản được tạo (trạng thái pending, kèm 3 huy hiệu khởi đầu). Các lỗi thường gặp được xử lý tự động, không làm gián đoạn người dùng:

| Lỗi | Xử lý |
|---|---|
| 「用户名已存在」 (tên người dùng đã tồn tại) | Tự động gợi ý biến thể (tên người dùng + số), khi người dùng xác nhận thì thử lại ngay (mã vẫn còn hiệu lực, không cần gửi lại) |
| 「邮箱已被使用」 (email đã được dùng) | Hỏi người dùng: đổi email, hay thật ra đã có tài khoản? (chuyển sang đăng nhập/quên mật khẩu) |
| 「邮箱验证码错误或已过期」 (mã xác minh sai hoặc hết hạn) | Quá 10 phút → chạy lại `send-code` |
| Gửi/đăng ký quá dày (429) | Chờ 1 phút rồi thử lại; chỉ cần báo người dùng một tiếng |

## Bước 6: đăng nhập một chạm (link 1) + thanh toán

1. Ngay khi đăng ký thành công:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Gửi link cho người dùng: **mở ra trình duyệt rơi thẳng vào trang gói thành viên, đã ở trạng thái đăng nhập** — nhờ vậy khi thanh toán xong, trang hoàn tất hiển thị đúng «thanh toán thành công». (Ở trạng thái này các trang nội dung vẫn bị chặn về trang gói thành viên: đó là hoạt động bình thường của bức tường phí của nền tảng, không phải bug, cũng không cần giải thích cơ chế bên trong cho người dùng.)
2. Ba gói để chọn, khi giới thiệu kèm giá:
   - Tháng **¥6.99** (khuyên dùng khi mới thử) / Quý **¥19.99** / Năm **¥69.99** — Alipay mua đứt thời gian tương ứng một lần, **không tự động gia hạn**
3. Khi người dùng chọn xong:
   ```
   node scripts/powpow-register.mjs create-order --package monthly
   ```
   Script trả về đường dẫn file trang thanh toán; **dùng lệnh hệ thống mở thẳng** (Windows: `start <tệp>`; macOS: `open <tệp>`; Linux: `xdg-open <tệp>`). Trình duyệt tự nhảy sang trang thu ngân chính thức của Alipay; người dùng quét mã QR hoặc đăng nhập Alipay để thanh toán.
4. Cứ 10–15 giây chạy `query` một lần cho đến khi trả về `paid` (tiền về thường từ vài giây đến một phút). Người dùng đóng trang thanh toán giữa chừng → chạy lại `create-order` luôn (đơn cũ tự đóng sau 2 tiếng, khỏi bận tâm).
5. Người dùng ở nước ngoài/không có Alipay: hướng dẫn dùng kênh PayPal trên trang gói thành viên (skill không thao tác hộ, chỉ dẫn đường); kênh quét mã WeChat cần xác nhận thủ công, tiền về bị trễ. Sau khi thanh toán xong vẫn quay về bước 7 như thường.

## Bước 7: đăng nhập chính thức (link 2)

Xác nhận tiền đã về, trước tiên đổi sang trạng thái đăng nhập mang tuyên bố gói mới nhất, rồi sinh link thẳng tới trang chủ:

```
POWPOW_REGISTER_PASSWORD=<mật khẩu> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Gửi link cho người dùng: **mở ra rơi thẳng trang chủ, trạng thái thành viên đầy đủ**; đến đây toàn bộ quy trình đăng ký hoàn tất.

## Bước 8: kết thúc

1. `node scripts/powpow-register.mjs cleanup` dọn file trạng thái tạm trên máy (thông tin phiên đăng nhập).
2. Đưa người dùng một «thẻ tài khoản»: tên người dùng, email và ngày hết hạn thành viên (mật khẩu không hiển thị lại — chế độ tạo mật khẩu đã nhờ người dùng lưu ngay lúc tạo; mật khẩu họ tự đặt thì họ vốn biết).
3. Hướng dẫn trải nghiệm đầu tiên: dạo bản đồ, đăng bài du ký đầu tiên (→ giao cho powpow-simple).
4. Gợi ý tiện ích mở rộng: skill `@durenzidu/powpow-integration` và plugin `@durenzidu/openclaw-channel-powpow` — kết nối Bong Bóng vào agent của chính người dùng; nếu quan tâm thì đưa lệnh cài đặt.
5. Kết thúc bằng khối «bước tiếp theo».

## Conversation UX

Giữ đúng tông phục vụ quen thuộc của powpow:

- **Người dùng là chủ ngữ của câu**; «bạn có thể…» tốt hơn «tôi cần bạn…»; không giảng đạo, không đứng trên nhìn xuống.
- **Mỗi lượt chỉ tiến một quyết định**; trước khi xin thông tin, nêu lý do trước.
- **Cuối mỗi câu trả lời** là một khối «bước tiếp theo» cố định (dấu phân cách + 👉 + một hành động duy nhất + một câu «khi bạn làm xong, tôi sẽ…»), ví dụ:
  ```
  ────────────────────
  👉 Đến lượt bạn: vào email tìm mã 6 chữ số và gửi thẳng cho tôi
     (ngay khi nhận được, tôi tạo tài khoản cho bạn)
  ```
- **Không chủ động giảng bài bảo mật về mật khẩu**; không giải thích cơ chế bên trong, giới hạn tần suất hay thiết kế an toàn, trừ khi người dùng hỏi.
- Khi agent thao tác hộ càng phải báo tiến độ: sau mỗi bước script, nói một câu cho người dùng biết vừa xảy ra chuyện gì («tài khoản đã tạo xong», «trang thanh toán đã mở cho bạn rồi»).

## Quy tắc cứng

- **An toàn thông tin đăng nhập**: mật khẩu chỉ truyền cho script qua biến môi trường `POWPOW_REGISTER_PASSWORD`, **tuyệt đối không** đưa vào tham số dòng lệnh (nhìn thấy trong danh sách tiến trình), không ghi vào bất kỳ file nào (chế độ tạo mật khẩu hiển thị một lần để người dùng lưu, sau đó không nhắc lại). Mã xác minh chỉ dùng cho giao diện đăng ký chính thức và vứt bỏ sau khi dùng.
- **Ranh giới chính thức**: mọi request chỉ gửi về `https://global.powpow.online` (đã tích hợp sẵn trong script); tuyệt đối không gửi thông tin người dùng tới địa chỉ bên thứ ba nào.
- **Ranh giới thanh toán**: agent chỉ tạo đơn, mở trang thu ngân, tra tiền về; **tuyệt đối không** đụng vào tài khoản Alipay/chứng từ thanh toán của người dùng, cũng tuyệt đối không hứa «trả tiền hộ».
- **Bức tường phí không phải bug**: trạng thái pending vào được trang gói thành viên/trang hoàn tất là lỗ hổng cho phép có chủ đích trong thiết kế; các trang nội dung bị chặn là bức tường phí hoạt động bình thường; đừng tìm cách vòng qua.
- **Tự do lùi lại**: nếu ở bất kỳ bước nào người dùng muốn tự làm, hoặc môi trường không chạy được script, cứ lùi về chế độ hướng dẫn thuần bất cứ lúc nào — đưa link, giảng quy tắc, cùng xử lý lỗi.
- Đừng bịa quy tắc của nền tảng: quy tắc trường, nội dung lỗi, tham số giới hạn đều đến từ code nền tảng (`references/registration-flow.md` có ghi nguồn); nền tảng cập nhật thì lấy hành vi thực tế làm chuẩn.
- Khi trình bày ảnh chỉ dùng ảnh chụp trong gói `assets/screenshots/` (công dụng từng ảnh xem trong `references/screenshots.md`).
- Mỗi lượt kết thúc bằng khối «bước tiếp theo», để người dùng luôn biết mình cần làm gì lúc này.
