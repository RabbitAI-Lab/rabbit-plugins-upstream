# meme-digger — 网络梗考古与科普（Agent Skill）

刨根问底式网络梗调查：连接贴吧与 B 站，从评论区挖线索做发散搜索，产出带证据链、时间线、梗图、来源介绍的单文件 Meme 百科 HTML。

遵循 [Agent Skills](https://agentskills.io) 开放标准，兼容 pi / Claude Code / Codex / OpenCode。

## 安装（各平台）

| 平台 | 方式 | 状态 |
|---|---|---|
| **pi** | 复制整个目录到 `~/.pi/agent/skills/meme-digger/` | ✅ 已安装 |
| **Claude Code** | `git clone https://github.com/SgtBaixiao/meme-digger ~/.claude/skills/meme-digger` | ✅ 可克隆 |
| **Codex / OpenCode** | 复制到 `~/.codex/skills/` / `~/.opencode/skills/` | ✅ 可克隆 |
| **Hugging Face CLI** | `hf skills add https://github.com/SgtBaixiao/meme-digger` | ⏳ 上架后 |
| **Agent Skill Hub** | `skhub add SgtBaixiao/meme-digger` | ⏳ 待导入（需账号） |
| **Skillstore** | `skillstore install meme-digger` | ⏳ 待提交（需账号） |

## 依赖

- Python ≥ 3.10，**仅标准库**，零第三方依赖
- B 站：免登录（搜索/详情/评论/图片全通）
- 贴吧：需 cookie（`python scripts/config_cookies.py` 配置向导，见 SKILL.md 第 4 步）

## 使用

直接问 agent"这是什么梗 / 这个梗什么来历"，或在支持 `/` 命令的客户端输入 `/meme-digger <梗名>`。

完整工作流（9 步：立项 → B站搜索 → 评论区深挖 → 贴吧采集 → 发散搜索 → 梗图收集 → 来源考证 → 整合报告 → Meme 百科 HTML）见 [SKILL.md](SKILL.md)。

## 结构

```
meme-digger/
├── SKILL.md                    # 方法论 + 9 步工作流 + 质量标准（入口）
├── scripts/                    # Python 标准库脚本套件
│   ├── bili_search.py          # B站搜索（免登录）
│   ├── bili_video.py           # 视频详情
│   ├── bili_comments.py        # 评论区深挖 + 梗图 URL 清单
│   ├── bili_memes.py           # 定向梗图挖掘（T1封面/T2高赞评分）
│   ├── bili_dl.py              # 图片下载（去重）
│   ├── tieba_search.py         # 贴吧搜索（需 cookie）
│   ├── config_cookies.py       # cookie 配置向导
│   ├── make_report.py          # 生成单文件 Meme 百科 HTML
│   └── common.py               # 共享模块
├── templates/encyclopedia.css  # 百科页样式模板
└── config/cookies.json.example # cookie 配置样例（真实 cookie 不入库）
```

## 安全与边界

- 不传播谣言、不教唆、不美化低俗内容；事实与网络传闻严格分标注
- 梗图仅下载用于分析，报告保留原图 URL 与出处，不声称版权
- 引用遵守"简短引用 + 链接"

## License

MIT © Sgt_BaiXiao
