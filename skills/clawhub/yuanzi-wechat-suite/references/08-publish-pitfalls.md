# 08. 公众号发布教训（keyring / 缓存 / 错误码）

> 来源：MEMORY.md「微信公众号发布教训」+「微信凭据存储」

## 核心经验（5 条）

### 1. 图片子目录路径

```python
# ❌ 错误：用 os.path.basename() 丢层级
img_src = os.path.basename(src)  # imgs/fig1.png → fig1.png

# ✅ 正确：用 os.path.join() 保留完整路径
img_src = os.path.join(base_dir, src)  # 保留 imgs/fig1.png
```

### 2. 40002 频率限制

- 3 次重试 + 5 秒延迟
- 图片上传每张间隔 3 秒
- 发现 40002 立即停等 10-15 秒再试

### 3. HTML body 提取

```python
# ❌ 错误：正则
import re
content = re.search(r'<body>(.*?)</body>', html).group(1)

# ✅ 正确：BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
content = str(soup.find('body'))
```

### 4. 正文图片

**用 `material/add_material` 永久素材接口**（临时接口无 `url` 字段）

### 5. 配置修改后必实测

> **不信 MEMORY.md 记录** — 实测为准 — 老板 2026-06-29

## 半自动工作流

- **草稿自动**：`publish_wechat.py` 创建草稿
- **群发手动**：老板去微信公众平台后台（订阅号无 freepublish API 权限）

## 关键脚本

| 脚本 | 路径 |
|---|---|
| `publish_wechat.py` | `skills/wechat-article-publisher/scripts/publish_wechat.py` |
| Token 缓存 | `skills/wechat-article-publisher/.token_cache.json`（2h 过期） |

## leantalk 部署踩坑（参考）

> 不属于公众号，但同属发布链路

- 部署前用脚本验 magic bytes（JPEG `FF D8` / PNG `89 50 4E 47`）
- JSON 文案禁用 ASCII 直引号（用全角「」/『』）

## token_cache.json 教训

- **位置：** `skills/wechat-article-publisher/.token_cache.json`
- **格式：** `{"access_token": "***", "expires_at": <timestamp>}`
- **风险：** 含真实 access_token，**发布到 ClawHub 前必须删除**
- **生成：** 首次 `--dry-run` 时自动创建

## User env 残留踩坑（2026-06-24）

老板最初设置 `WECHAT_APP_SECRET` 为旧密钥在 User 环境变量中。PowerShell `unset` 后仅在当前进程生效；gateway 启动时继承的副本仍在，导致首次 `dry-run` 仍走 env。

**解决：优先级 keyring > env > config**，env 残留不再触达。

## publish_wechat.py 兜底缺馅（2026-07-02）

- **`--cover-image` 缺省时**：`publish_wechat.py` 默认 fallback 到 `skills/wechat-article-publisher/assets/generated_cover.jpg`（紫底黑字 + 软错图标）
- **无错误信息**：日志静默
- **改进方向**：发布前脚本格式验证 / `assert cover.exists() + print(f"封面 {size} KB")`

---

*🦞 元子公众号图文系列 · 知识舱 · 08 发布教训*