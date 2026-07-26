# klyc-pmm 安全合规文档

本文档描述 klyc-pmm 技能包的安全加固措施，适用于昆仑 2026-07 安全标准。

## 传输安全
### HTTPS 强制
- 所有 API 通信走 HTTPS（TLSv1.3）
- curl 调用加 `--ssl-reqd` 参数，防 TLS 降级攻击
- 证书由 Let's Encrypt 签发，自动续期

### 客户端预加密（v5.1+）
- 推送记忆前在客户端侧加密：Gzip 压缩 → AES-256-GCM → Base64
- 存储格式：`__ENC__:base64(iv(12B) + tag(16B) + ciphertext)`
- 加密密钥通过瑶池 API（`yaochi/key`）获取，缓存1小时
- 密钥不落本地文件，不硬编码在脚本中
- 客户端加密不可用时降级为明文传输，服务端 AES-256-GCM 兜底
- 128位随机 IV per-encryption

### 身份认证
- Bearer Token：所有写操作带 `Authorization: Bearer <token>`
- Token 通过 `yaochi/auth/refresh` 自动续期（401 触发）
- 注册防重：机器指纹去重，已注册用户可通过瑶池 API 恢复 Token
- 密钥从冻层（`kl_frozen_memories`）读取，不落配置文件

## 频率限制

### 内置限流
| 端点 | 限制 | burrst |
|------|------|--------|
| 注册 | 5/min | — |
| 嵌入 | 30/min | — |
| 批量同步 | 3/hour | — |
| A2A RPC | 30/min | 10 |
| 恢复（recover） | 30/min | 5 |

### 客户端退避
- 429 响应自动指数退避：2s → 4s → 8s（最多3次）
- 401 响应自动 Token 刷新后重试一次

## 数据安全

### 加密存储
- DB 存储前走 AES-256-GCM + Gzip（服务端兜底）
- 前置 `__ENC__:` 标记区分新旧数据
- 旧明文数据向后兼容，读取时自动判断

### 昆仑令
- 昆仑令格式：`https://ai.syln.cn/klyc-pmm/{token}` 或 `KLYC-PMM-{token}`。由服务端 `random_bytes(8)` ×2 生成，2^64 熵空间
- 凭码恢复免登录，但首次恢复后24h宽限期内标记 `already_recovered`
- 恢复日志记录到 `kl_recovery_log`，含 IP/UA/时间
- /klyc-pmm/ 端点已启用 access_log off + rate-limit + no-store。建议人类将昆仑令离线保存（截图/备忘录），不通过网络传输

### 隐私保护
- 敏感信息（密码、密钥、Token）不写入本地日志
- 错误响应不泄露凭证或内部路径
- `content_preview` 最多 200 字符，避免完整内容出现在日志中
- 不收集用户行为数据，无第三方 tracker

## 生产环境清单

部署前确认以下项目：

- [ ] API Key 已生成（`kl_api_keys` 表）
- [ ] 加密密钥已写入冻层（`kl_frozen_memories`）
- [ ] HTTPS 证书有效（Let's Encrypt 自动续期确认）
- [ ] Nginx 流控配置生效（`limit_req_zone` 位于 `http{}` 块内）
- [ ] 恢复端点有流控保护（`recover_zone: 30r/m`）
- [ ] 昆仑令有效期策略已设置（默认30天）
- [ ] CORS 限制为 `https://ai.syln.cn`

