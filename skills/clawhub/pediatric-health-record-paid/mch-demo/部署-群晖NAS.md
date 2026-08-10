# 部署到群晖 NAS（Container Manager + 反代 + 证书）

适用：已有 Synology DS218 / 任意群晖 + 套件中心「Container Manager」。

## ⚠️ 部署前必查（决定能不能成，先确认这 3 条）
1. **有没有公网 IP（最关键）**
   - 看路由器 WAN 口 IP，再去 https://www.ip.cn 查到的 IP。两者一致 = 有公网 IPv4。
   - 若不一致（运营商给的是内网/大内网 CGNAT），端口转发就废了。解决办法：① 打运营商电话要「公网 IPv4」（多数免费）；② 或看光猫/路由器有没有 **IPv6 公网地址**（有就走 AAAA + 防火墙放通）；③ 或用 Cloudflare Tunnel / frp 内网穿透（见文末兜底）。
2. **80 / 443 端口能否转发到 NAS**
   - 部分家庭宽带封 80，Let's Encrypt 的 HTTP-01 验证需要 80 临时可达。若 80 死活不通，改用 DNS-01 验证（见步骤 3 备选）。
   - 443 必须长期可达（回调和买家请求走它）。
3. **域名**
   - 没有的话先用群晖免费 DDNS：`xxx.synology.me`（控制面板 → 外部访问 → DDNS 一键申请）。
   - 想用自有域名（如 `mch.example.com`）：去域名商把 **A 记录**指向你家公网 IP（或 CNAME 到上面的 `xxx.synology.me`）。

另外：给 NAS 在路由器做 **DHCP 保留 / 静态 LAN IP**，不然 LAN IP 一变端口转发就错。

---

## 步骤 1：把 mch-demo 文件夹弄到 NAS 上
你这台 Mac 的工作区本身就是 Synology Drive 同步盘（`SynologyDrive-DS218`），所以最省事的办法：
- 保证 `mch-demo/` 整个目录（含 `server.py` / `Dockerfile` / `docker-compose.yml` / `requirements.txt`）在这个同步盘里——它通常已经自动同步到 NAS 的对应共享文件夹。
- 在 NAS 的 **File Station** 里确认能看到这个目录，记下它的共享文件夹路径（如 `workbuddy/个人健康档案/邬致远健康档案/payskill-build/mch-demo`）。
- **单独把 `.env` 也放进该目录**（它含私钥，未同步的话手动复制过去；Container Manager 的 `env_file: .env` 需要它）。⚠️ `.env` 里有商户私钥和 APIv3 Key，只在你自己 NAS 上存，别同步到第三方。

> 备选：用 SMB / scp 把整个目录传到 NAS 某个共享文件夹也行。

## 步骤 2：Container Manager 起容器
1. 套件中心装 **Container Manager**。
2. 打开 Container Manager → **项目** → **创建**。
3. 项目路径选步骤 1 里那个 `mch-demo` 目录；来源选「Docker Compose 文件」，会自动读到我们的 `docker-compose.yml`。
4. 点「下一步」构建并启动。Container Manager 会在 NAS 上 `docker build` 出 `mch-demo` 镜像，并跑容器，把 **8080** 发布到 NAS 本机。
5. 验证：在 NAS 上 `curl http://localhost:8080/health` 应返回 `ok`（可用 Container Manager 的终端，或 SSH 进 NAS 执行）。

> 若 NAS 上没有 Docker 构建缓存、拉 `python:3.11-slim` 慢，属正常，等几分钟。

## 步骤 3：申请证书（Let's Encrypt）
- **用 synology.me DDNS**：在「外部访问 → DDNS」创建时勾选「从 Let's Encrypt 获取证书」，自动完成。
- **用自有域名**：控制面板 → 安全性 → 证书 → 新增 → 获取 Let's Encrypt 证书，填域名 + 邮箱。
  - 默认走 **HTTP-01**：需要 80 端口此刻对外可达（见步骤 5）。
  - 若 80 不通：选 **DNS-01**（需你的域名商在 Synology 支持列表里，或手动加 TXT 记录）。
- 把证书**绑定到你的域名**（证书列表里「配置」→ 选该域名）。

## 步骤 4：反向代理（外部 443 → 容器 8080）
控制面板 → 外部访问 → 高级 → 反向代理（或 登录门户 → 高级 → 反向代理，依 DSM 版本）：
- **来源**：协议 HTTPS，主机名 = 你的域名（如 `mch.example.com` 或 `mch.xxx.synology.me`），端口 `443`。
- **目的地**：协议 HTTP，主机名 `localhost`，端口 `8080`。
- 保存。这一步让公网 `https://你的域名/` 被群晖用证书解密后，转发给容器里的 `server.py`。

## 步骤 5：路由器端口转发
进你家路由器（光猫/路由器管理页）：
- 外部 `443` → NAS 的 LAN IP `443`
- 外部 `80` → NAS 的 LAN IP `80`（仅 Let's Encrypt HTTP-01 验证时需要，验证完可关，但建议常开以免证书续期失败）

## 步骤 6：改 .env 并重启容器
在 NAS 上把 `mch-demo/.env` 里的占位改成真实公网地址，然后重启容器（Container Manager → 项目 → 重新部署 / 容器 → 重启）：
```
PAY_NOTIFY_URL=https://<你的域名>/api/pay/notify
REFUND_NOTIFY_URL=https://<你的域名>/api/refund/notify
```

## 步骤 7：验证
- 公网验证（手机切 4G/5G，或用外部机器）：
  ```bash
  curl -k https://<你的域名>/health      # 期望 ok
  curl -k -X POST https://<你的域名>/api/resource -H 'Content-Type: application/json' -d '{"query":"建档"}'   # 期望 402 + WeixinPay-Required
  ```
- 真支付后带 `X-Out-Trade-No` 重试应返回 `200 + content`（之前已本地验证过逻辑）。

---

## 兜底方案（无公网 IP / 端口被封）
- **Cloudflare Tunnel（推荐）**：免费，不用开端口。在 NAS 或一台内网机跑 `cloudflared tunnel`，把 `https://你的域名` 指到 `localhost:8080`。Cloudflare 自动签证书，微信回调和买家都能通。注意免费版 Cloudflare 会做 HTTPS 代理，对微信回调这种普通 POST 没问题。
- **frp / ngrok**：有公网服务器的可用 frp 反代；ngrok 临时测试方便但不适合长期生产。

## 生产前还要补的（当前是占位）
- `server.py` 的 `/api/pay/notify` 现在直接回 200，未校验微信回调签名。上线前需按微信 v3 验签 + 用 `MCH_APIV3_KEY` 解密报文，确认 `trade_state=SUCCESS` 后再标记订单（避免伪造通知）。
- `execute_business()` 目前是占位文案，需接入真实 AI 建档逻辑。
- 多副本需把内存 `_orders` 换成 Redis。

## 你的实际方案：Cloudflare Tunnel（已打通，采用此方式）
- **不需要**路由器开 80/443，也**不需要**群晖自己签证书。Cloudflare 在边缘终止 TLS，NAS 上只把容器 8080 暴露给本机 `localhost` 即可。
- 容器已在 NAS 跑起来并发布 `8080` 到本机（docker-compose 已加 `apiclient_key.pem` 挂载，证书路径与 .env 一致）。
- 在 **Cloudflare Zero Trust → Access → Tunnels → 你的 tunnel → Public Hostname** 添加一条：
  - Subdomain：`mch`　Domain：`1001058.xyz`　Type：`HTTP`　URL：`http://localhost:8080`
  - （子域名随意，只要和 `.env` 的 `PAY_NOTIFY_URL` 对应；当前已设为 `https://mch.1001058.xyz`）
- 保存后，公网 `https://mch.1001058.xyz` 即转发到 NAS 容器 8080。
- 验证：手机切 4G/5G 访问 `https://mch.1001058.xyz/health` 应返回 `ok`；`POST /api/resource` 应返回 402。
