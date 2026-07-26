# 05. IP 白名单 + 发布踩坑（40164 / 40002）

> 来源：MEMORY.md「公众号 IP 白名单 + 发布踩坑（2026-06-29 更新）」
> 来源：MEMORY.md「微信公众号发布教训」

## 当前有效 IP

**`114.x.x.x`**（每次家宽拨号可能变化，部署前查 ifconfig.me 实时获取）

## 历史 IP 链（均失效，掩码避免指纹）

| IP | 状态 |
|---|---|
| `49.x.x.x` | ❌ 失效 |
| `114.x.x.x` | ❌ 失效 |
| `180.x.x.x` | ❌ 失效 |
| `114.x.x.x` | ❌ 失效 |
| **`114.x.x.x`** | ✅ 当前有效（2026-06-29 起） |

## 白名单策略

1 IP 收窄（2026-06-19 老板精简：旧 6 IP 全删）

## 家宽换 IP 流程

```
家宽拨号 → 获新 IP → 老板手动加白 → 吾重跑 publish_wechat.py
```

## 40164 错误码

**含义：** IP 未在白名单

**排查：**
1. `curl ifconfig.me` → 获取当前公网 IP
2. 老板手动加白（微信公众平台 → 设置 → 基本配置 → IP 白名单）
3. `--dry-run` 验证凭据 → 真实入草稿箱

## 40164 关键教训

> 本机 curl 失败但 publish_wechat.py 成功是**假象**——以真实脚本运行为准，**先 --dry-run**

## 40002 错误码（频率限制）

**含义：** 调用微信 API 频率超限

**处理：**
- 3 次重试 + 5 秒延迟
- 图片上传每张间隔 3 秒
- 发现 40002 立即停等 10-15 秒再试

## 48001 错误码

**含义：** 没有发布权限

**处理：** 在微信后台手动发布（订阅号无 freepublish API 权限）

## 53401 错误码（封面尺寸）

**含义：** 封面图尺寸不合规

**处理：** 自动 resize 至 900×383（2.35:1）

## 40007 错误码（thumb_media_id 无效）

**含义：** 草稿 thumb_media_id 无效

**处理：** 用 `material/add_material` 永久素材接口上传封面，获取 media_id

## 凭据存储：Windows Credential Manager

**位置：** keyring library，service=`wechat-article-publisher` / username=`<your-app-id>`

**后端：** `keyring.backends.Windows.WinVaultKeyring`

**读取优先级：**
1. keyring → 2) env var WECHAT_APP_SECRET → 3) config.json fallback

**设置凭据：**
```powershell
python -c "import keyring; keyring.set_password('wechat-article-publisher', '<your-app-id>', '<your-app-secret>')"
```

**config.json 改为占位符** `USE_KEYRING`（含「USE_」前缀不会被作为 fallback）

## 老板教训

> IP 白名单换 IP 是家常便饭——**别凭印象记录**，必须 `curl ifconfig.me` 实时查 — 老板 2026-06-29

---

*🦞 元子公众号图文系列 · 知识舱 · 05 IP 白名单 + 发布踩坑*