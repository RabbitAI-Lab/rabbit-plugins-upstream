# weread-socrates · 纯离线跨书伴读

v1.4.0 是一个可通过 `file://` 直接打开的自包含 HTML。它不连接微信读书账号或任何模型；用户手动粘贴片段，在浏览器中完成苏格拉底式提问、Reader Memory v2、继续思考和跨书对照。

## 快速使用

1. 用现代浏览器打开 `assets/ai-reading-companion.html`。
2. 明确点击 `中文` 或 `English`；页面不会读取浏览器语言或记忆上次选择。
3. 选择内置《苏格拉底的申辩》/《沉思录》Demo，或粘贴自己的片段。
4. 生成五个问题并按需保存反思、概念、立场或未解问题。
5. 在“跨书对照”中检查本地候选，选择 `支持 / 冲突 / 扩展 / 例证`，编辑理由并确认。
6. 主动下载所选已确认关系的 Markdown 或 Canvas PNG 对照卡。

## 关键行为

- 单文件、零依赖、无外链、无服务器，可通过 `file://` 使用。
- CSP 声明 `connect-src 'none'`；没有网络、API、模型、Key、环境变量或 shell。
- `allowed-tools` 只有 `Read`。
- Reader Memory 仅使用浏览器 `localStorage`。
- v1 数据首次打开自动迁移为 `{version:2, entries, relations}`，保留合法 entry ID 与内容。
- 跨书候选只由共同标签/关键词在本地生成，不持久化。
- 关系只有经过复选框和确认对话两步用户确认后才保存。
- 删除节点会清理悬空关系；清空操作需用户确认。
- Markdown/PNG 仅由用户点击生成，不自动写文件或发送。

## 双书 Demo

Demo 提供两段公版主题的改写文本，便于无账号、无 Key 体验完整流程。加载 Demo 不会保存任何节点。确认 Demo 关系时，所需的两个 Demo 节点与关系才一起进入 Memory。

## Memory v2

```json
{
  "version": 2,
  "entries": [],
  "relations": []
}
```

entry 支持 `concept / stance / question / reflection`；relation 支持 `supports / conflicts / extends / exemplifies`。语言偏好不进入 Memory，初始 HTML 始终为 `lang="und"`。

## 项目结构

```text
weread-socrates/
├── assets/ai-reading-companion.html
├── test/static.test.js
├── README.md
├── SKILL.md
├── skill-card.md
├── _meta.json
└── LICENSE
```

## 静态验证

```text
node --test test/static.test.js
```

测试覆盖版本、只读权限、单文件/CSP、禁止网络与高权限文件、显式中英语言门、Memory v2 迁移、四种关系、候选不持久化、双书 Demo、继续思考、用户确认，以及 Markdown/Canvas PNG 下载。

## 隐私与版权

清除该 `file://` 页面对应的浏览器站点数据会删除 Reader Memory。请只粘贴有权用于个人学习的内容；下载内容可能包含受版权保护文本，不应未经许可公开传播。本工具不是微信读书官方产品。
