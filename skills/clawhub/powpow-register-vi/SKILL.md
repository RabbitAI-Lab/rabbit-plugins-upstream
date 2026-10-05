---
name: powpow-register
description: Hỗ trợ người dùng đăng ký tài khoản PowPow (Bong Bóng) và hoàn tất kích hoạt gói đăng ký. Kích hoạt khi người dùng nói "đăng ký Bong Bóng", "đăng ký tài khoản powpow", "đăng ký powpow bằng cách nào", "giúp tôi đăng ký tài khoản powpow", "sign up powpow"; cũng xử lý các vấn đề trong quá trình đăng ký (không nhận được mã xác minh, tên đăng nhập/email đã bị dùng, sai định dạng mật khẩu) và vấn đề kích hoạt sau đăng ký (đăng nhập báo "tài khoản chưa kích hoạt" / pending_payment, cách đăng ký gói/thanh toán). Skill thuần hướng dẫn: giới thiệu sản phẩm (kèm ảnh chụp màn hình) → hướng dẫn đăng ký từng bước → tra cứu lỗi → kích hoạt gói đăng ký. Không bao gồm đăng bài/tạo nhân vật số (việc đó thuộc về powpow-simple), không bao gồm phát triển mã.
version: 1.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Trợ lý đăng ký Bong Bóng)

Đưa người dùng mới từ "không biết Bong Bóng là gì" đến "đã kích hoạt tài khoản, dùng được bình thường".

**Phiên bản 1.0.0** · 2026-09-23 (chi tiết quy trình đăng ký và tra cứu lỗi xem `references/registration-flow.md`; kích hoạt gói và kênh thanh toán xem `references/payment-and-activation.md`; danh sách ảnh chụp sản phẩm xem `references/screenshots.md`)

## Môi trường chạy

Skill này thuộc loại **thuần hướng dẫn**: không có bất kỳ script nào, không cần Node hay phụ thuộc nào khác. Toàn bộ thao tác (điền biểu mẫu, nhận mã xác minh, thanh toán) do người dùng thực hiện trong trình duyệt/App, bạn chỉ giới thiệu, chỉ đường và tra cứu lỗi.

## Trigger Conditions

- Ý định đăng ký: "đăng ký Bong Bóng", "đăng ký một tài khoản powpow", "đăng ký powpow bằng cách nào", "sign up powpow"
- Kẹt khi đăng ký: "không nhận được mã xác minh", "báo tên đăng nhập đã tồn tại", "mật khẩu mãi không hợp lệ"
- Vấn đề sau đăng ký: "đăng nhập báo tài khoản chưa kích hoạt", "403 pending_payment", "powpow thanh toán/đăng ký gói bằng cách nào"

**Không kích hoạt**: đăng bài/tạo nhân vật số (→ powpow-simple); phát triển mã phía Web (xem các skill phát triển khác).
Người dùng vừa muốn đăng ký vừa muốn đăng bài: đi hết skill này trước, sau khi kích hoạt tài khoản rồi chuyển cho powpow-simple.

## Giới thiệu sản phẩm + trình bày ảnh chụp màn hình (bước một, không được bỏ qua)

Hầu hết người dùng chưa từng thấy Bong Bóng. Điều đầu tiên không phải nói quy trình, mà là để họ **nhìn thấy** sản phẩm:

1. Giới thiệu Bong Bóng trong ~120 từ: biến ảnh chụp ngẫu nhiên thành một bài du ký, ghim lên bản đồ công khai thành một
   "bong bóng"; bong bóng sẽ cũ đi theo thời gian, người khác thả tim có thể làm nó sống lại; trên bản đồ còn có "nhân vật số" có thể trò chuyện.
   Địa chỉ nền tảng https://global.powpow.online , muốn xem video trước thì:
   https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Gửi link ảnh chụp màn hình** (ảnh Markdown hoặc link trần đều được). Danh sách, nội dung từng ảnh và thời điểm dùng xem
   `references/screenshots.md`. Tổ hợp dùng nhiều nhất khi mở đầu: trang bản đồ (powpow-03) + trang chi tiết bài đăng (powpow-06).

Quy tắc ảnh chụp (quy tắc cứng):

- Ảnh được lưu trữ trong repo công khai `durenzidu/durenzidu` thư mục `screenshots/` (`powpow-0N.jpg`),
   **không** tải ảnh vào thư mục skill, cũng không gửi đường dẫn local thay cho ảnh.
- Nếu `raw.githubusercontent.com` không mở được, dùng mirror jsdelivr (xem `references/screenshots.md`).
- Mỗi lần chỉ gửi 1–3 ảnh liên quan đến chủ đề hiện tại, đừng dồn hết tất cả lên một lúc.
- Không rõ là ảnh nào thì đừng đoán — đối chiếu mô tả trong `references/screenshots.md` để chọn.

Giới thiệu xong, trao "bước tiếp theo" cho người dùng: **"Sẵn sàng đăng ký thì chúng ta mất ba phút để lập xong tài khoản."**

## Quy trình đăng ký (bước hai)

Đăng ký hoàn toàn trên trang web: **https://global.powpow.online/register**. Để người dùng mở trang,
bạn hướng dẫn đồng hành theo các điểm dưới đây (quy tắc đầy đủ về trường dữ liệu, tham số giới hạn và bảng tra cứu lỗi ở
`references/registration-flow.md`, gặp vấn đề thì tra ở đó):

1. **(Tùy chọn) Ảnh đại diện**: ảnh ≤5MB, không hỗ trợ SVG.
2. **Tên đăng nhập**: 2~50 ký tự; không phân biệt hoa thường (Tom và tom là cùng một tài khoản).
3. **Mật khẩu**: tối thiểu 8 ký tự, phải chứa đồng thời chữ in hoa, chữ thường và số; nhập lại lần nữa để xác nhận.
4. **Biệt danh**: tùy chọn, không điền thì mặc định dùng tên đăng nhập.
5. **Email (bắt buộc)**: bấm "Gửi mã xác minh" → vào hộp thư tìm **mã xác minh 6 chữ số** (có hiệu lực trong 10 phút,
   chú ý thư mục thư rác/thư quảng cáo); nút có đếm ngược 60 giây.
6. **Số điện thoại**: tùy chọn, đúng định dạng số điện thoại Trung Quốc đại lục; một số điện thoại chỉ ràng buộc một tài khoản.
7. Gửi biểu mẫu.

Phía dưới trang còn có **Google / Watcha / tài khoản Huawei** ba nút đăng nhập bên thứ ba — nếu người dùng quen dùng
tài khoản bên thứ ba, bấm thẳng nút là được, không cần đi đăng ký bằng email.

**Sau khi gửi sẽ xảy ra chuyện gì**: tài khoản được tạo ngay lập tức (trạng thái pending, ban đầu 3 huy hiệu), trang tự động nhảy tới
trang đăng ký gói `/subscription`. **Sau khi hoàn tất đăng ký gói tài khoản mới được kích hoạt**, mới dùng được feed, bản đồ, trò chuyện với nhân vật số
—— bước này xem phần tiếp theo.

Khi hướng dẫn không được bịa thông tin thay người dùng; mỗi lượt trả lời kết thúc bằng một khối "bước tiếp theo" rõ ràng.

## Kích hoạt gói đăng ký (bước ba)

Đăng ký chỉ tạo tài khoản pending, **phải thanh toán gói đăng ký mới kích hoạt**. Skill này không đụng vào bất kỳ khâu thanh toán nào,
chỉ cần dẫn người dùng tới trang đăng ký gói: **https://global.powpow.online/subscription**

Tùy theo môi trường của người dùng, trên trang sẽ xuất hiện một trong ba kênh:

| Kênh | Môi trường | Ghi chú |
|---|---|---|
| Gói đăng ký PayPal | Web | Tự động gia hạn, thanh toán xong sẽ tự kích hoạt qua Webhook, có thể hủy bất cứ lúc nào |
| Quét mã WeChat đăng ký gói | Web | Quét mã chuyển khoản, **mở sau khi được xác nhận thủ công**, tiền về có thể bị trễ |
| Mua trong ứng dụng Huawei | Trong App HarmonyOS | Trên HarmonyOS không dùng được PayPal/WeChat Pay, đi qua Huawei IAP gốc |

Thanh toán xong tài khoản chuyển sang active, tự động nhảy về trang chủ (hoặc trang người dùng muốn xem trước khi đăng ký).
Chi tiết kênh, chuỗi kích hoạt và kết luận "phương thức thanh toán sẵn có dùng lại được ngay" xem
`references/payment-and-activation.md`.

**Lời nói với người dùng**: "Đăng ký xong trang sẽ đưa bạn tới trang đăng ký gói; trên web có thể dùng PayPal hoặc quét mã WeChat,
trong App HarmonyOS dùng thanh toán Huawei. Thanh toán xong là tài khoản kích hoạt."

## Conversation UX

Giữ phong cách phục vụ quen thuộc của powpow:

- **Người dùng là chủ ngữ của câu**, "bạn có thể…" tốt hơn "tôi cần bạn…"; không giảng đạo, không bề trên.
- **Mỗi lượt chỉ tiến một quyết định**; trước khi xin thông tin hãy nêu lý do.
- **Cuối mỗi lượt trả lời** là một khối "bước tiếp theo" cố định (đường kẻ + 👉 + một thao tác duy nhất + một câu
  "xong tôi sẽ…"), ví dụ:
  ```
  ────────────────────
  👉 Việc cần bạn làm bây giờ: mở trang đăng ký, điền tên đăng nhập và mật khẩu
     (điền xong báo tôi, chúng ta tiếp tục gửi mã xác minh)
  ```
- **Không chủ động giảng đạo về bảo mật mật khẩu**; không giải thích cơ chế nội bộ, giới hạn hay thiết kế bảo mật, trừ khi người dùng hỏi.

## Quy tắc cứng

- Đăng ký thực hiện trên trang web, skill này chỉ giới thiệu, chỉ đường, tra cứu lỗi — **không bao giờ** xin mật khẩu
  hoặc mã xác minh của người dùng, cũng không cố gửi biểu mẫu thay người dùng.
- Không bịa quy tắc nền tảng: quy tắc trường dữ liệu, thông báo lỗi, tham số giới hạn đều từ mã nguồn nền tảng
  (`references/registration-flow.md` ghi rõ nguồn mã), nền tảng cập nhật lấy hành vi thực tế làm chuẩn.
- Hiển thị ảnh chỉ dùng link lưu trữ trong `references/screenshots.md`, tuân thủ quy tắc ảnh chụp.
- Mỗi lượt đều kết thúc bằng khối "bước tiếp theo", để người dùng luôn biết bây giờ cần làm gì.