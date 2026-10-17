---
name: "ent-zalo-bridge"
description: "Dựng bridge nhận tin Zalo Bot vào OpenClaw: viết service webhook (node, port 8787), cấu hình token + secret, trỏ domain HTTPS, đăng ký setWebhook với Zalo. Kèm script gửi tin."
---

# ent-zalo-bridge — Dựng bridge WEBHOOK Zalo Bot (nhận tin vào)

Skill này giúp agent **dựng hạ tầng nhận tin từ Zalo Bot vào OpenClaw**: viết service webhook (node), cấu hình token + secret, trỏ domain HTTPS của máy, rồi **đăng ký webhook với Zalo**.

> 🔒 **Phạm vi:** tạo service node nghe webhook + đăng ký webhook với Zalo + cấu hình env. KHÔNG đụng dữ liệu khác, KHÔNG mở port công khai ra ngoài (chỉ 127.0.0.1 + domain trỏ vào), KHÔNG xoá webhook/dữ liệu của bot khác.

## 0. KÍCH HOẠT — câu lệnh người dùng

Khi người dùng nói kiểu:
```
Dựng bridge Zalo cho anh. Token bot: <TOKEN>. Secret: <SECRET>. Domain: https://<host>/zalo/webhook
```
hoặc
```
Cài bridge nhận tin Zalo Bot
```

Agent PHẢI hiểu: **dựng service webhook + đăng ký với Zalo**.

### Quy trình tự động
1. Trích `ZALO_BOT_TOKEN`, `ZALO_SECRET` (nếu có), `DOMAIN` (URL public HTTPS của máy) từ tin nhắn.
2. Kiểm tra token sống: `getMe` (mục 3.1). Lỗi → DỪNG.
3. Tạo service webhook (dùng code mục 4, hoặc copy `zalo_webhook.js`).
4. Cấu hình env: `ZALO_BOT_TOKEN`, `ZALO_SECRET`, `PORT=8787`.
5. Chạy service như **systemd service** (mục 6) để chạy 24/7.
6. **Đăng ký webhook với Zalo:** `setWebhook` (mục 3.3) trỏ tới `https://<domain>/zalo/webhook`.
7. Test: gửi 1 tin vào nhóm → kiểm tra webhook nhận được (log `events.ndjson`).
8. Báo kết quả ngắn: service chạy, webhook set, nhận tin OK.

> ⚠️ Thiếu token hoặc domain → hỏi lại đúng cái thiếu, KHÔNG đoán.
> ⚠️ Chỉ thực thi khi người gửi là **owner**.

## 1. Kiến trúc bridge (hiểu đúng)

```
Zalo Bot Platform ──(HTTPS POST)──▶ https://<domain>/zalo/webhook
                                          │
                                   (reverse proxy / tunnel)
                                          ▼
                              node service (127.0.0.1:8787)
                                          │
                              ✔ xác thực Secret Token (header)
                              ✔ log event → logs/events.ndjson
                              ✔ trả 200 OK
```

- **Service node** chỉ nghe `127.0.0.1:8787` (an toàn, không lộ trực tiếp).
- **Domain HTTPS** trỏ về port đó (qua reverse proxy nginx/caddy, hoặc tunnel free như `tino.page`/`ngrok`/`cloudflared`).
- **Zalo** phải gọi được URL public HTTPS → nếu không có, webhook không set được.

## 2. Yêu cầu hạ tầng

| Thứ | Bắt buộc | Ghi chú |
|---|---|---|
| Node.js ≥ 18 | ✅ | Service webhook (dùng `fetch` built-in) |
| `ZALO_BOT_TOKEN` | ✅ | Dạng `<bot_id>:<secret>` |
| `ZALO_SECRET` | Khuyến nghị | Secret Token đặt trên dashboard Zalo Bot |
| Domain HTTPS public | ✅ | Trỏ về port 8787. Có thể: domain riêng + nginx/caddy, hoặc tunnel free |
| Port 8787 | ✅ | Mặc định; đổi qua env `PORT` |

## 3. Lệnh API Zalo Bot

Base: `https://bot-api.zaloplatforms.com/bot<TOKEN>`

### 3.1 Kiểm tra bot
```bash
curl -s "https://bot-api.zaloplatforms.com/bot$ZALO_BOT_TOKEN/getMe"
```

### 3.2 Gửi tin (kiểm thử / nhắc việc)
```bash
curl -s -X POST "https://bot-api.zaloplatforms.com/bot$ZALO_BOT_TOKEN/sendMessage" \
  -H "Content-Type: application/json" \
  -d "{\"chat_id\":\"$ZALO_CHAT_ID\",\"text\":\"Nội dung\"}"
```

### 3.3 Đăng ký webhook
```bash
curl -s -X POST "https://bot-api.zaloplatforms.com/bot$ZALO_BOT_TOKEN/setWebhook" \
  -H "Content-Type: application/json" \
  -d "{\"url\":\"https://<DOMAIN>/zalo/webhook\",\"secret_token\":\"$ZALO_SECRET\"}"
```
- `ok: true` → webhook đã đăng ký.
- Sau khi set webhook: **`getUpdates` KHÔNG dùng được nữa** (lỗi 400). Bình thường.

### 3.4 Xem webhook hiện tại / gỡ webhook
```bash
# Xem
curl -s "https://bot-api.zaloplatforms.com/bot$ZALO_BOT_TOKEN/getWebhookInfo"
# Gỡ (nếu muốn quay lại getUpdates)
curl -s -X POST "https://bot-api.zaloplatforms.com/bot$ZALO_BOT_TOKEN/deleteWebhook"
```

## 4. Code service webhook (node, không dependency)

Đặt tại `zalo-bridge/zalo_webhook.js`:

```javascript
#!/usr/bin/env node
'use strict';
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = parseInt(process.env.PORT || '8787', 10);
const TOKEN = process.env.ZALO_BOT_TOKEN || '';
const SECRET = process.env.ZALO_SECRET || '';
const API_BASE = 'https://bot-api.zaloplatforms.com/bot' + TOKEN;

const LOG_DIR = path.join(__dirname, 'logs');
const EVENT_LOG = path.join(LOG_DIR, 'events.ndjson');
fs.mkdirSync(LOG_DIR, { recursive: true });

function log(level, msg, extra) {
  const line = JSON.stringify({ t: new Date().toISOString(), level, msg, ...(extra || {}) });
  console.log(line);
  fs.appendFileSync(EVENT_LOG, line + '\n');
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = []; let size = 0;
    req.on('data', (c) => {
      size += c.length;
      if (size > 2 * 1024 * 1024) { reject(new Error('body too large')); req.destroy(); return; }
      chunks.push(c);
    });
    req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    req.on('error', reject);
  });
}

function secretFromHeaders(h) {
  return h['x-bot-api-secret-token'] || h['x-zalo-secret'] || h['x-secret-token'] ||
         h['secret-token'] || h['x-zalo-signature'] || '';
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, 'http://localhost');
  const p = url.pathname;

  if (req.method === 'GET' && ['/', '/health', '/zalo', '/zalo/health'].includes(p)) {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ ok: true, service: 'zalo-bridge', ts: new Date().toISOString() }));
    return;
  }
  if (req.method === 'GET' && (p === '/zalo/webhook' || p === '/webhook')) {
    const ch = url.searchParams.get('challenge') || url.searchParams.get('hub.challenge') || 'ok';
    res.writeHead(200, { 'Content-Type': 'text/plain' }); res.end(ch); return;
  }
  if (req.method === 'POST' && (p === '/zalo/webhook' || p === '/webhook')) {
    try {
      const raw = await readBody(req);
      const got = secretFromHeaders(req.headers);
      let payload = null;
      try { payload = JSON.parse(raw); } catch (_) {}
      if (SECRET && got && got !== SECRET) {
        log('warn', 'secret mismatch', {}); res.writeHead(401); res.end('unauthorized'); return;
      }
      log('info', 'webhook received', { secretPresent: !!got, payload });
      if (payload) fs.writeFileSync(path.join(LOG_DIR, 'last_event.json'), JSON.stringify(payload, null, 2));
      res.writeHead(200, { 'Content-Type': 'application/json' }); res.end(JSON.stringify({ ok: true }));
    } catch (e) {
      log('error', 'webhook error', { err: String(e) });
      res.writeHead(500); res.end('error');
    }
    return;
  }
  res.writeHead(404); res.end('not found');
});

server.listen(PORT, '127.0.0.1', () => {
  log('info', 'zalo-bridge listening', { port: PORT, hasToken: !!TOKEN, hasSecret: !!SECRET });
});
```

## 5. Biến môi trường

| Biến | Mô tả |
|---|---|
| `ZALO_BOT_TOKEN` | Token bot (`<bot_id>:<secret>`) |
| `ZALO_SECRET` | Secret Token đặt trên dashboard Zalo (để xác thực webhook) |
| `PORT` | Cổng nghe (mặc định `8787`) |

**Lưu ý:** token nằm trong path API Zalo (khác Meta). KHÔNG echo token ra chat/log.

## 6. Chạy 24/7 bằng systemd (khuyến nghị)

Tạo file `/etc/systemd/system/zalo-bridge.service`:
```ini
[Unit]
Description=Zalo Bot webhook bridge
After=network.target

[Service]
Type=simple
WorkingDirectory=/opt/zalo-bridge
Environment=ZALO_BOT_TOKEN=<TOKEN>
Environment=ZALO_SECRET=<SECRET>
Environment=PORT=8787
ExecStart=/usr/bin/node /opt/zalo-bridge/zalo_webhook.js
Restart=always
RestartSec=5
User=<user>

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now zalo-bridge
sudo systemctl status zalo-bridge
```

## 7. Trỏ domain HTTPS về port 8787

### 7A. ⭐ LẤY DOMAIN FREE (tino.page / tunnel) — cách đã dùng thật

> 💡 **Domain KHÔNG đi kèm VPS.** Mua VPS không tự có domain. Phải tự lấy 1 subdomain public HTTPS rồi trỏ về máy. Cách đã dùng thật ở hệ thống này: **subdomain free của `tino.page` + Caddy**.

**Bước 1 — Lấy subdomain free:**
- **tino.page** cấp subdomain HTTPS free theo **tên máy** (vd host `pttsnagb8` → `pttsnagb8.tino.page`). Có HTTPS sẵn, không cần mua/mua cert thủ công.
- Tương đương: **cloudflared** (`cloudflared tunnel --url http://127.0.0.1:8787`), **ngrok**, **localhost.run**... — đều trỏ subdomain HTTPS về `127.0.0.1`.
- ⚠️ Tunnel free thường **gắn với máy/phiên** — agent mới ở máy khác phải lấy tunnel **riêng của nó**.

**Bước 2 — Caddy đẩy domain vào port 8787** (xem 7B).

**Bước 3 — Kiểm tra + setWebhook:**
```bash
curl -s https://<domain>/zalo/health
# {"ok":true,"service":"zalo-bridge",...}
```
Rồi `setWebhook` với `https://<domain>/zalo/webhook` (mục 3.3).

### 7B. ⭐ CADDY làm reverse proxy (cấu hình mẫu đã dùng thật)

Caddy giúp: nhận HTTPS từ domain → đẩy vào port nội bộ. File `/opt/openclaw/Caddyfile` mẫu:
```caddyfile
{$DOMAIN:localhost} {
    {$CADDY_TLS:tls internal}

    # Zalo Bot webhook -> zalo-bridge (local)
    handle /zalo/* {
        reverse_proxy 127.0.0.1:8787
    }

    # Login page + auth API -> Management API on host
    handle /login {
        reverse_proxy 127.0.0.1:9998
    }
    handle /api/auth/* {
        reverse_proxy 127.0.0.1:9998
    }

    reverse_proxy 127.0.0.1:18789 {
        header_up Host {host}
        header_up X-Forwarded-For {remote_host}
        header_up X-Forwarded-Host {host}
        header_up X-Forwarded-Proto {scheme}
        header_up X-Real-IP {remote_host}
    }
}
```
Chạy: `caddy run --config /opt/openclaw/Caddyfile` (hoặc để systemd quản lý). Biến `DOMAIN` truyền qua env; nếu chưa có domain riêng, Caddy tự cấp **`tls internal`** (cert nội bộ).

> Lưu ý: khối `handle /zalo/*` là **phần quan trọng** — nó trỏ webhook Zalo vào `127.0.0.1:8787`. Các khối khác (login, API, gateway) là của OpenClaw, giữ nguyên khi merge.

### 7C. Cách khác — Reverse proxy (nginx)
```nginx
server {
  listen 443 ssl;
  server_name <domain>;
  ssl_certificate     /etc/letsencrypt/live/<domain>/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/<domain>/privkey.pem;
  location /zalo/webhook {
    proxy_pass http://127.0.0.1:8787;
    proxy_set_header Host $host;
  }
}
```

### 7D. Cách khác — Tunnel free không cần proxy riêng
Khi chưa muốn dựng Caddy/nginx: dùng `cloudflared`, `ngrok`, hoặc `tino.page` — chúng tự trỏ subdomain HTTPS về `127.0.0.1:8787` (nhớ khớp đúng path `/zalo/webhook`).

## 8. Test end-to-end

1. Gửi 1 tin vào nhóm Zalo (hoặc nhắn bot).
2. Kiểm tra log:
   ```bash
   tail -5 logs/events.ndjson
   cat logs/last_event.json
   ```
3. Thấy event `webhook received` + payload → **bridge OK**.
4. Không thấy → kiểm tra: domain trỏ đúng chưa, service chạy chưa, webhook đã set chưa (`getWebhookInfo`).

## 9. GIỚI HẠN Zalo Bot — nhớ (đừng hứa sai)

| Giới hạn | Chi tiết |
|---|---|
| **KHÔNG tag/mention tên người** | `@Tên` chỉ là chữ thường → đẩy tên lên đầu tin |
| **Trần BASIC** | 3 bot · 50 user/bot · 3.000 tin/tháng · 3 nhóm |
| **Pro** | 129.000đ/tháng — trần cao hơn |
| **Webhook XOR getUpdates** | Set webhook thì `getUpdates` không dùng được |
| **Bot phải vào nhóm** | Add bot thủ công trước |
| **Không moi tin cũ** | Bot không đọc tin trước khi vào nhóm |
| **Rate limit** | Chưa công bố số tin/giây, tin/phút |

## 10. Xử lý sự cố

| Lỗi | Nguyên nhân | Cách xử lý |
|---|---|---|
| `setWebhook` lỗi URL | Domain chưa HTTPS / không public | Kiểm tra domain, cert, service chạy |
| `secret mismatch` trong log | Secret trên dashboard khác env | Đồng bộ `ZALO_SECRET` |
| Webhook 200 nhưng không log | Sai path | Đảm bảo Zalo trỏ `/zalo/webhook` |
| `getUpdates` lỗi 400 | Đã set webhook | Bình thường — dùng webhook |
| Service chết sau reboot | Chưa `systemctl enable` | `enable --now` |
| Không nhận tin | Bot chưa vào nhóm / sai chat | Add bot vào nhóm |

## 11. Bảo mật — BẮT BUỘC

- Chỉ nhận token/secret từ **owner**.
- KHÔNG echo token/secret ra chat/log.
- Service **chỉ nghe 127.0.0.1** (không mở trực tiếp ra ngoài); public qua proxy/tunnel có HTTPS.
- Đặt `ZALO_SECRET` để xác thực webhook; không nhận request không đúng secret.
- KHÔNG chia sẻ token sang máy/agent khác.

## 12. Ghi chú kỹ thuật

- Node ≥ 18 cần cho `fetch` built-in (hoặc thay bằng `https` module nếu Node cũ).
- Log event dạng NDJSON tại `logs/events.ndjson` — dễ `tail`/parse.
- Kết hợp với skill `ent-zalo-connect` (gửi tin) để thành bộ Zalo Bot đầy đủ: gửi + nhận.
- Muốn bỏ webhook, quay về polling → `deleteWebhook` rồi dùng `getUpdates`.
