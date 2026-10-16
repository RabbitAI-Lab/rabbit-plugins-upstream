---
name: "meta-long-lived-token"
description: "Đổi Meta short-lived token (~1-2h) sang long-lived token (~60 ngày) qua Graph API, kiểm tra hạn, lưu vào env gateway và nhắc gia hạn. READ-ONLY với ads."
---

# Meta Long-Lived Token — đổi & gia hạn token Meta Ads

Đổi **short-lived user token** (~1–2 giờ) thành **long-lived token** (~60 ngày) qua Graph API chính thức, kiểm tra hạn và lưu an toàn vào env của gateway.

> 🔒 **An toàn:** skill này CHỈ gọi endpoint `oauth/access_token` (đổi token) + `debug_token` (kiểm tra). KHÔNG đọc/sửa dữ liệu quảng cáo. KHÔNG gọi POST/DELETE tới ads.

## 0. KÍCH HOẠT — câu lệnh người dùng chỉ cần nhập

Khi người dùng gửi tin nhắn dạng:

```
Em gia hạn token thêm 60 ngày nhé.
ID App: <APP_ID>
Secrect key: <APP_SECRET>
```

Agent PHẢI hiểu là: **đổi token hiện tại (short-lived) sang long-lived** bằng App ID + App Secret đã cung cấp.

### Quy trình tự động khi nhận câu lệnh trên

1. **Trích xuất** `APP_ID` và `APP_SECRET` từ tin nhắn (chấp nhận ghi đúng/sai chính tả như "Secrect key", "Secret", "App Secret").
2. **Lấy token hiện tại** từ env gateway (`META_ACCESS_TOKEN`). Đây là `fb_exchange_token` đầu vào.
   - Dùng `exec`: `echo $META_ACCESS_TOKEN` — KHÔNG echo ra chat.
3. **Đổi sang long-lived** (mục 3 bên dưới).
4. **Kiểm tra** token mới bằng `debug_token` (mục 4).
5. **Lưu** token mới vào env gateway, **giữ nguyên env cũ**, rồi restart (mục 5).
6. **Test lại** sau restart + **báo ngắn gọn** cho owner: token hợp lệ, hạn mới (`expires_at`), số ngày còn lại.

> ⚠️ Nếu THIẾU `APP_ID` hoặc `APP_SECRET` → hỏi lại đúng cái còn thiếu, KHÔNG tự đoán.
> ⚠️ Nếu token hiện tại đã là long-lived (`expires_at=0` hoặc còn xa) → vẫn thực thi re-exchange để "gia hạn thêm 60 ngày" như yêu cầu, và báo rõ hạn mới.
> ⚠️ Chỉ thực thi khi người gửi là **owner**. Nếu không chắc → hỏi xác nhận trước khi ghi config.

## 1. Cần chuẩn bị

| Thứ | Lấy ở đâu |
|-----|-----------|
| `SHORT_LIVED_TOKEN` | Token tạm từ Graph API Explorer (xem mục 2) — sống ~1–2h |
| `APP_ID` | App ID của app Facebook (developers.facebook.com → App settings → Basic) |
| `APP_SECRET` | App Secret cùng trang (bấm "Show") |

⚠️ **Cần cả APP_SECRET** — không có secret thì KHÔNG đổi được sang long-lived. Nếu app chưa có secret → vào App settings → Basic để lấy.

## 2. Lấy short-lived token

1. Vào `developers.facebook.com/tools/explorer`
2. Chọn app (loại Business)
3. Thêm quyền cần dùng — tối thiểu `ads_read` (thêm `ads_management` nếu cần ghi; thêm `pages_manage_posts`, `pages_read_engagement` nếu dùng page)
4. **Generate Access Token** → đăng nhập → cho phép
5. Copy token (bắt đầu bằng `EAA...`) — token này chỉ sống ~1–2h

## 3. Đổi sang long-lived token

```bash
curl -s -G "https://graph.facebook.com/v21.0/oauth/access_token" \
  --data-urlencode "grant_type=fb_exchange_token" \
  --data-urlencode "client_id=$APP_ID" \
  --data-urlencode "client_secret=$APP_SECRET" \
  --data-urlencode "fb_exchange_token=$SHORT_LIVED_TOKEN"
```

Kết quả trả JSON: `{"access_token":"EAA...","token_type":"bearer","expires_in":5184000}`
→ `expires_in` ~**5.184.000 giây ≈ 60 ngày**. Đây là token long-lived cần lưu.

> ⚠️ **Không bao giờ nhét token thẳng vào URL bằng dấu ngoặc kép** → shell cắt chuỗi → lỗi 4xx GIẢ. Luôn dùng `curl -G --data-urlencode "...=$TOKEN"`.

## 4. Kiểm tra token vừa đổi (bắt buộc)

```bash
curl -s -G "https://graph.facebook.com/v21.0/debug_token" \
  --data-urlencode "input_token=$LONG_LIVED_TOKEN" \
  --data-urlencode "access_token=$LONG_LIVED_TOKEN"
```

Đọc `data`:
- `is_valid: true` → OK
- `expires_at`: epoch giây **ngày hết hạn** (~60 ngày tới). Nếu `0` → token không đặt ngày hết hạn (một số app dev/test).
- `data_access_expires_at`: mốc chặn truy cập dữ liệu (thường xa hơn `expires_at`) — **theo dõi mốc này làm mốc phụ**.
- `scopes`: phải có quyền cần dùng (`ads_read`...).

## 5. Lưu vào env gateway (không hardcode)

- Đọc config hiện tại, **giữ nguyên toàn bộ env cũ**, chỉ cập nhật khóa `META_ACCESS_TOKEN` (và `META_AD_ACCOUNT_ID` nếu có).
- Dùng merge (không ghi đè cả file config).
- Sau khi lưu → **restart gateway** để env nạp lại, rồi chạy lại `debug_token` với `$META_ACCESS_TOKEN` để xác nhận.
- **KHÔNG echo token ra chat/log**, KHÔNG commit token vào git.

## 6. Theo dõi hạn & nhắc gia hạn

- Long-lived token hết hạn sau **~60 ngày** → phải **đổi lại** (lặp lại mục 2–4) trước khi hết.
- Đặt lịch kiểm tra định kỳ (cron preflight hằng ngày) gọi `debug_token`, tính số ngày còn lại:
  - Còn **< 14 ngày** → **nhắc owner** đổi token mới.
  - `is_valid: false` hoặc lỗi `190` → token chết, báo owner lấy token mới ngay.
- Lưu ý: **không có cơ chế tự gia hạn hoàn toàn** cho token user — vẫn cần thao tác đăng nhập để lấy short-lived mới. (System User token mới là loại có thể không hết hạn.)

## 7. Trả lời nhanh câu hỏi thường gặp

| Câu hỏi | Trả lời |
|---|---|
| Đổi long-lived gia hạn thêm bao nhiêu? | Từ ~1–2h lên **~60 ngày** → thêm **~59 ngày** |
| Trần tối đa được bao nhiêu? | **~60 ngày** cho token user, không vượt được |
| Hết 60 ngày thì sao? | Đổi lại (re-exchange) → **thêm ~60 ngày/lần** |
| Có loại nào không hết hạn? | **System User token** (Business Manager) — tuỳ cấu hình |

## Xử lý sự cố

| Lỗi | Nguyên nhân | Cách xử lý |
|---|---|---|
| `(#190) Error validating access token` | Token chết/sai | Lấy short-lived mới ở Graph Explorer, đổi lại từ mục 3 |
| `(#200) Provide valid app ID` | Thiếu `access_token` hoặc sai `client_id` | Kiểm tra lại `APP_ID` + có truyền `access_token` |
| Lỗi 4xx "giả" dù token đúng | Token nhét thẳng vào URL bị shell cắt | Dùng `curl -G --data-urlencode` |
| `expires_in` trả về rất ngắn | Đang đổi từ token đã là long-lived, hoặc app chưa cấu hình đúng | Thử lại với short-lived token mới |
| Không có APP_SECRET | App thiếu secret | App settings → Basic → Show secret |

## Bảo mật — BẮT BUỘC

- Chỉ nhận token từ **owner** của máy/agent.
- KHÔNG ghi token ra file log, KHÔNG echo token ra chat.
- KHÔNG chia sẻ token sang máy/agent khác.
- Token trong lịch sử chat là rủi ro → cân nhắc rotate sau khi dùng xong với token quan trọng.
