# gbrain-guide

指导 AI agent **规范操作 GBrain 本地知识库**的 WorkBuddy skill（实操层）。

> 配合市场 skill `build-a-self-updating-agent-memory-graph-with-gbrain`（概念/安装层）使用：那个讲 GBrain 是什么、怎么装；这个讲 agent 具体怎么调工具、怎么分类、怎么治理健康度。

## GBrain 是什么

开源「个人知识大脑」（由 Y Combinator 总裁 Garry Tan 构建），用于运行 AI 代理的生产知识底座。通过 MCP 接入 WorkBuddy 后，所有工具以 `mcp__gbrain__` 前缀暴露（70+ 工具），负责存储、解析、embedding、混合检索（向量+关键词+图谱+RRF 融合）、实体链接与关联图。

支持：Markdown / Word / PDF / Excel·CSV / Org-mode / 图片。**视频/音频暂不支持**（需先 Whisper 转写文本再入库）。

## 安装（WorkBuddy）

把本仓库的 `SKILL.md` 放到用户级技能目录后刷新即可自动加载：

```bash
mkdir -p ~/.workbuddy/skills/gbrain-guide
cp SKILL.md ~/.workbuddy/skills/gbrain-guide/SKILL.md
```

## 核心：分类规范（最重要）

GBrain 通过 **schema pack** 把「页面 slug 的路径前缀 → page 类型」写死映射（默认 `gbrain-base`：**27 种 page 类型 + 12 种 link 类型**）。

**入库铁律：资料放进什么前缀文件夹，就自动归哪类。** 别丢无规范前缀的原始路径（如 `6.ros2系列教程/...`），否则全部被标成 `source` 原始资料桶，分类/关联能力完全不触发。

常用类型与路径前缀：

| 类型 | 路径前缀 | 用途 |
|---|---|---|
| source | source/, sources/ | 原始资料（兜底） |
| note | note/, notes/ | 笔记 |
| project | project/, projects/ | 项目 |
| person | person/, people/ | 人物 |
| company | company/, companies/ | 公司 |
| deal | deal/, deals/ | 交易/投资 |
| concept | wiki/concept/, wiki/concepts/ | 概念 |
| guide | wiki/guide/, wiki/guides/ | 指南 |
| analysis | wiki/analysis/ | 分析 |
| hardware | wiki/hardware/ | 硬件 |
| architecture | wiki/architecture/ | 架构 |
| writing | writing/ | 写作 |
| media | media/ | 媒体 |
| email | email/, emails/ | 邮件 |
| meeting | meeting/, meetings/ | 会议 |
| conversation | conversation/, conversations/ | 对话 |
| atom | atom/, atoms/ | 原子笔记 |
| extract_receipt | extracts/ | 抽取/收据 |
| calendar-event | cal/, calendar/ | 日历事件 |
| event | life/events/ | 生活事件 |
| diary | life/diary/ | 日记 |
| yc / civic / slack | yc/, civic/, slack/ | YC / 市政 / Slack |

完整 27 种类型用 `mcp__gbrain__schema_explain_type(type=xxx)` 或 `mcp__gbrain__schema_stats` 查询。

## 入库工作流

1. 定位本地资料根目录（确保磁盘空间充足，索引+资料需预留数倍空间）
2. 按前缀规整：移动文件到对应前缀路径，GBrain 自动分类
3. 触发入库：`sources_add` / `entry_import_content` / `put_page`（Markdown 用 put_page，PDF/Word 走 sources_add）
4. 验证：`get_stats` / `get_health` 看 embed_coverage（应=1）与 orphan 数（趋近 0）
5. 分批：大规模资料按 5–10G 小批，先 pilot 验证再全量

## 建关联（GBrain 真正价值）

- `add_link`（12 种 link type）连接「教程 → 项目 → 概念」
- `add_tag` 打标签
- `get_links` / `traverse_graph` 验证网络是否形成

## Schema Pack 切换

默认只用 base；另有 `gbrain-engineer`（代码/硬件更贴）、`gbrain-creator`、`gbrain-everything`。

- `list_schema_packs` 看可选
- `reload_schema_pack` 切换

## 健康度治理（定期跑）

- `get_health`：brain_score / embed_coverage / orphan / link 覆盖率
- `schema_review_orphans`：列出无类型匹配的页面
- `schema_lint`：lint 当前 pack
- `run_onboard`：自动体检/修复（admin 权限）

目标：brain_score 向 100 收敛、orphan→0、link_coverage 显著提升。

## WorkBuddy MCP 工具速查

- 检索：`search` / `query` / `recall` / `get_chunks`
- 写入：`put_page` / `entry_import_content` / `sources_add`
- 图遍历：`traverse_graph` / `get_links`
- 治理：`get_health` / `schema_review_orphans` / `run_onboard`
- 分类规范：`schema_explain_type` / `schema_stats` / `get_active_schema_pack`

## 与 Obsidian 联动（可选）

GBrain 检索层（查得到）+ Obsidian 下游笔记沉淀（理得清）：检索片段 → agent 产出结构化笔记 → 存 Obsidian（纯 Markdown，易读易维护）。少量视频先 Whisper-GPU（有 NVIDIA 独显）转写再入库。

## License

MIT —— 可自由复用、改造。
