# 懂我记忆策略

## 层级

1. `myprofile.md`：用户明确确认的事实和偏好。
2. `.dongwo/memory/preferences.md` 的 `active`：明确或长期表达的自动偏好。
3. `.dongwo/memory/preferences.md` 的 `soft`：跨独立会话重复出现的观察。
4. `.dongwo/memory/review.md`：单次候选或冲突，不注入执行上下文。
5. `.dongwo/memory/inbox/`：经过敏感信息遮蔽的用户原始表达。

旧版 Obsidian Vault 可以继续使用
`03_Projects/15_懂我/memory/`，由 `DONGWO_HOME` 或自动兼容逻辑选择。

## 优先级

当前提示 > 项目要求 > 用户确认档案 > 自动明确偏好 > 稳定观察。

## 自动化原则

- 自动采集每轮用户提示。
- 临时措辞不进入长期偏好。
- 同一语义键出现新旧值时，最新明确表达取代旧值。
- 无法确定新旧关系时不注入，写入待复核。
- 敏感提示经遮蔽后只留作交互审计，不参与偏好提取。
- 自动生成文件必须由脚本重建；改进归纳时修改脚本和测试。
- 用户画像和 Inbox 默认只保存在本机；不要把它们包含进 Skill 发布包。
