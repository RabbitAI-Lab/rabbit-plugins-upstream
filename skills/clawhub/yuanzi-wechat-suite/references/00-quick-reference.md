# 00. 快速参考卡（元子公众号图文系列）

> 一页速查 · 高频铁律 / 错误码 / 工具命令

## 高频铁律（8 条）

1. **事实可考据** — 每个数据 / 人名 / 年份必有公开来源
2. **谁在说话** — 老板署名，不出现「龙虾 5 号」「吾」「AI」
3. **入戏不套话** — 反思嵌入叙事，不用「讲到这，我们一起想」
4. **句长 35-50 字** — 短句（<20 字）占比 < 20%
5. **字数 800-3,500** — 老板号调性（不是 v7 铁律 8,500-9,500）
6. **关键词密度 > 50/万字**
7. **配图用相对路径** — 不用 base64 内联（否则草稿箱无图）
8. **封面 21:9 (900×383)** — 不合规报 53401

## 4 类禁句开头

- ❌「两个数字摆在一起，反差很大——」
- ❌「很多人 X，但 Y」
- ❌「先看几个数字 / 先说几个数据」
- ❌「谈到 X，不得不提 Y」

## 微信 API 错误码速查

| 错误码 | 含义 | 解决 |
|---|---|---|
| **40001** | access_token 无效 | 强制刷新 token |
| **40002** | 频率超限 | 3 次重试 + 5s 延迟；图片 3s 间隔 |
| **40007** | thumb_media_id 无效 | 用永久素材接口 |
| **40164** | IP 不在白名单 | 老板手动加白 |
| **41005** | media data missing | 检查图片路径 |
| **48001** | 无发布权限 | 微信后台手动群发 |
| **53401** | 封面尺寸不合规 | 自动 resize 至 900×383 |

## IP 白名单

**当前有效：** `114.x.x.x`（每次家宽拨号可能变化，部署前查 ifconfig.me）

**家宽换 IP 流程：** 拨号获新 IP → 老板手动加白 → 吾重跑

## 凭据存储

**位置：** Windows Credential Manager（keyring）
- service: `wechat-article-publisher`
- username: `<your-app-id>`

**设置：**
```powershell
python -c "import keyring; keyring.set_password('wechat-article-publisher', '<your-app-id>', '<your-app-secret>')"
```

## ClawHub 发技能速查

| 任务 | 命令 |
|---|---|
| 发新技能 | `clawhub skill publish <dir> --slug <unique> --name "..." --version X.Y.Z --changelog "..."` |
| 验证 install | `clawhub install <slug> --dir <tmp> --force` |
| 搜技能 | `clawhub search "..."` |
| 查技能 | `clawhub inspect <slug>` |

**⚠️ 避坑：**
- 同一 slug 别用 `--fork-of`（AMBIGUOUS 时失败）
- `package.json` 含 `openclaw: { type: "skill" }` 必删
- `skill-card.md` 必删
- 用独特 slug 前缀（yuanzi-）

## 元子系列 6 站

| 站 | Slug | 职能 |
|---|---|---|
| 0/6 | `yuanzi-wechat-suite` | 导航舵 |
| 1/6 | `yuanzi-article-master` | 写作舵 |
| 2/6 | `yuanzi-article-extractor` | 读稿锚 |
| 3/6 | `yuanzi-image-generator` | 配图帆 |
| 4/6 | `yuanzi-wechat-publisher` | 发布桨 |
| 5/6 | `yuanzi-wechat-kb` | 知识舱 |

---

*🦞 元子公众号图文系列 · 知识舱 · 00 快速参考卡*