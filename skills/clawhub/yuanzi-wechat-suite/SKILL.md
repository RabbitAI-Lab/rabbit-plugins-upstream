---
name: yuanzi-wechat-suite
description: 元子公众号图文系列整合版。一键装 = 4 站流水线（读稿 → 写作 → 配图 → 发布）+ 11 段知识库 + 全套脚本。Use when user needs end-to-end WeChat Official Account article production: article scraping (mp.weixin.qq.com), copywriting (散文体铁律 v7), image generation (covers/comparisons/charts), publishing (一键草稿). v2.1.2 整合 5 yuanzi- 技能为 1，含 master v7 自动校验 + 总调度 + 4 站包装 + 11 段 KB。
tags: [yuanzi, gzh, articles, wechat, suite, master, extractor, image, publisher, kb, suite:yuanzi-wechat-series, mega-package]
version: 2.1.4
metadata:
  series: yuanzi-wechat-series
  series-position: 整合舵 (v2 升级: 吸收 5 同侪)
  total-stations: 4
  supersedes:
    - yuanzi-article-master@1.0.0
    - yuanzi-article-extractor@1.0.1
    - yuanzi-image-generator@1.0.3
    - yuanzi-wechat-publisher@2.1.0
    - yuanzi-wechat-kb@1.0.0
---

# 元子公众号图文系列 · 整合版 v2

> 🦞 yuanzi-wechat-series · v2.1.2
> **1 装即用** — 4 站流水线 + 知识库 + 全套脚本

## 一句话

5 个独立 yuanzi-* 技能 → **1 个整合技能**。装 1 个 = 装 5 个的功能。

## 包含（原 5 技能 = 现 1 技能）

| 站 | 原独立技能 | 现整合路径 | 职能 |
|---|---|---|---|
| 1/4 写作舵 | yuanzi-article-master | `references/写作舵-master v7 散文体铁律.md` | 散文体铁律 v7 + 三问定调 |
| 2/4 读稿锚 | yuanzi-article-extractor | `scripts/extractor/` | mp.weixin.qq.com 解析 |
| 3/4 配图帆 | yuanzi-image-generator | `scripts/image-gen/` | 零 token 封面/对比/数据图 |
| 4/4 发布桨 | yuanzi-wechat-publisher | `scripts/publisher/` | Markdown/HTML → 草稿箱 |
| 知识 | yuanzi-wechat-kb | `references/00~10*.md` | 11 段 Markdown 知识库 |

> 注：5 个独立 yuanzi-* 技能已在 clawhub 隐藏。用户升级装本整合版即可。

## 装后目录结构

```
yuanzi-wechat-suite/                              <- 装到这里
├── SKILL.md                                      # 本文件（主入口）
├──                                              # 一键调用脚本
│   ├── yuanzi-extract                            # → node scripts/extractor/...
│   ├── yuanzi-image                              # → python scripts/image-gen/...
│   └── yuanzi-publish                            # → python scripts/publisher/...
├── references/                                   # 11 段 + 写作舵
│   ├── 00-quick-reference.md
│   ├── 01-v7-master-4-laws.md
│   ├── 02-v8-prose-8-laws.md
│   ├── 03-tail-structure.md
│   ├── 04-image-publish-iron-laws.md
│   ├── 05-ip-whitelist-pitfalls.md
│   ├── 06-end-to-end-workflow.md
│   ├── 07-prose-word-count.md
│   ├── 08-publish-pitfalls.md
│   ├── 09-case-hugou-xiebian.md
│   ├── 10-clawhub-publish-pitfalls.md
│   └── 写作舵-master v7 散文体铁律.md
├── scripts/
│   ├── extractor/                                # 读稿锚 (Node.js)
│   │   ├── extract.js                            # 主解析器
│   │   ├── errors.js                             # 错误码
│   │   ├── package.json                          # npm 依赖
│   │   └── README.md
│   ├── image-gen/                                # 配图帆 (Python)
│   │   ├── generate.py                           # 主生成器
│   │   ├── serve.py                              # 本地预览服务
│   │   ├── auto_screenshot.py                    # 自动截图
│   │   ├── assets/                               # 3 模板
│   │   ├── output/                               # 3 样例
│   │   └── README.md
│   └── publisher/                                # 发布桨 (Python)
│       ├── publish_wechat.py                     # 主脚本
│       ├── config.json                           # app_id + USE_KEYRING
│       ├── requirements.txt                      # pip 依赖
│       └── assets/                               # 默认封面兜底
├── install-requirements.sh                        # macOS/Linux 一键装依赖
├── install-requirements.ps1                       # Windows 一键装依赖
└── agents/
    └── openai.yaml                                # OpenAI agent 接口
```

## 一键安装

```bash
# CLI 装（推荐）
clawhub install yuanzi-wechat-suite
# → 自动到 ~/.openclaw/workspace/skills/yuanzi-wechat-suite/
```

## 一键装依赖

```bash
# macOS / Linux
bash install-requirements.sh

# Windows
powershell -ExecutionPolicy Bypass -File install-requirements.ps1

# 或手动
pip install markdown requests Pillow beautifulsoup4 pyyaml keyring
cd scripts/extractor && npm install
```

## 4 站流水线

```
[读稿锚]  →  [写作舵]  →  [配图帆]  →  [发布桨]
extractor    master       image-gen    publisher
   ↓          ↓            ↓            ↓
解析 URL   散文体 v7     封面/对比     草稿箱
提炼选题   800-3500 字   数据图        老板群发
```

## 入口命令（总调度）

```bash
# 4 站自检
python scripts/yuanzi.py --check

# 读稿
python scripts/yuanzi.py extract --url "<mp.weixin.qq.com URL>"

# 散文体自动校验
python scripts/yuanzi.py check article.md

# 配图（封面 / 对比 / 数据图）
python scripts/yuanzi.py image cover --title "标题" --output cover.png

# 发布
python scripts/yuanzi.py publish article.html --dry-run
```

## 5 yuanzi-* 替代关系

| 原独立技能 | 替代为 |
|---|---|
| yuanzi-article-master | `references/写作舵-master v7 散文体铁律.md` + `scripts/yuanzi.py check` |
| yuanzi-article-extractor | `scripts/extractor/extract.js` |
| yuanzi-image-generator | `scripts/image-gen/generate.py` |
| yuanzi-wechat-publisher | `scripts/publisher/publish_wechat.py` |
| yuanzi-wechat-kb | 11 段 `references/*.md` |

## 凭据配置（发布前 1 次）

```bash
# 推荐用 keyring (Windows Credential Manager)
python -c "import keyring; keyring.set_password('wechat-article-publisher', '<your-app-id>', '<your-app-secret>')"

# 或临时环境变量
export WECHAT_APP_ID=<your-app-id>
export WECHAT_APP_SECRET=<your-app-secret>
```

## 快速参考

- **快速参考卡**: `references/00-quick-reference.md`
- **v7 铁律**: `references/01-v7-master-4-laws.md` + `02-v8-prose-8-laws.md`
- **端到端工作流**: `references/06-end-to-end-workflow.md`

## 更新日志

### v2.1.2 (2026-07-05)
- 🐛 修两个 path bug：(1) `scripts/image-gen/generate.py` ASSETS_DIR 缺 `image-gen/` 层级；(2) `scripts/publisher/publish_wechat.py` skill_dir 多取一层
- 🔧 修 utf-8 编码（之前双重编码显示乱码）

### v2.1.1 (2026-07-05)
- 🔒 隐私修复：掩码 references/ 中的 AppID 与 IP（5 处 114.x.x.x、2 处占位符），config.json 中 AppID 改占位符
- 功能无变化

### v2.1.0 (2026-07-05)
- 🆕 `scripts/yuanzi.py` 总调度（extract/image/publish/check/all/--check/--help）
- 🆕 `scripts/master/v7_check.py` 散文体自动校验（句长/短句/字数/4 禁句/谁在说话）
- 🔧 修 install-requirements.sh/.ps1 路径

### v2.0.0 (2026-07-04)
- 🆕 整合版本（草创）

### v1.0.0 (2026-07-04)
- 🆕 元子公众号图文系列首发

---

*🦞 元子公众号图文系列 · 整合版 · MIT-0 协议 · 一键装即用*
