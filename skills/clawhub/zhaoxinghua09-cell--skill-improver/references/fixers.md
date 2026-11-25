# 修复器清单

每个修复器都遵循三条约定：**先重读文件、幂等、只说做了什么**。

## 已实现的五个

| 修复器 | 触发键 | 判定条件 | 产出 | 幂等 |
|---|---|---|---|---|
| `fix_license` | `licensing:no-license` | 包根无 `LICENSE` | MIT 全文，作者取 frontmatter `author` | 有文件即跳过 |
| `fix_ai_index` | `discoverable:no-ai-index` | 无 `ai-index.json` | 从 description 切出 intents，标 `_generated_by` | 有文件即跳过 |
| `fix_tags` | `discoverable:no-tags` | frontmatter `tags` 少于 3 项 | 补到 4 项：包名 + description 中的长词 | 已有 ≥3 项即跳过 |
| `fix_triggers` | `discoverable:no-triggers` | 正文无 `## Triggers` / `## 触发` | 从 description 的引号短语补一段 | 已有标题即跳过 |
| `fix_links` | `discoverable:no-links` | 正文不含 `同系列` / `生态` / `系列技能` | 追加 `## Related skills`，写明「同系列技能」 | 已有标识即跳过 |

## 第六个（默认关闭）

`fix_doc_drift` — 处理"文档声明了但没实现"的阻断项。

- **只在 `--fix-doc-drift` 时启用**：它会改动既有内容。
- 做法是**移除**含未实现参数的那行示例，替换为一句不含参数名的说明行。
- 为什么不注释掉：因为检测器不跳注释，注释行里仍含 `--xxx` 就会继续命中——实测第 4 轮就是这样卡住的。
- 为什么留说明行：静默删除等于替作者做决定，原示例可能是他的规划。

## 为什么必须"先重读"

串联修复器如果共用一次读进来的 `body`，后一个修复器会把前一个的成果写回旧内容：

实测顺序 `tags → triggers` 时，`fix_tags` 写入了 tags，`fix_triggers` 用主函数里那份**旧的** `body` 写回，tags 就丢了。分数从 54 反降到 50。

所以每个修复器开头都重新读一次 `SKILL.md`。这不是防御性冗余，是实测教训。

## 返回值约定

| 返回 | 含义 |
|---|---|
| 字符串 | 做了这个改动（内容会被打印） |
| `None` | 无需改动（已有或条件不满足） |
| 列表（仅 `fix_doc_drift`） | 被替换的行号 |

打印时如实显示 `（已有，跳过）`，不假装做了事。
