# ClawHub 发布指南 — design-to-code

## 1. 文件夹结构（已准备就绪）

```
design-to-code/
└── SKILL.md          # 必需，已包含完整 frontmatter
```

**文件夹位置**：`/workspace/design-to-code/`

**发布方式**：直接将 `design-to-code` 文件夹拖放到 ClawHub 的 "Drop a folder" 区域即可，系统会自动检测 `SKILL.md`。

---

## 2. ClawHub 表单填写对照表

| 表单字段 | 填写内容 | 说明 |
|---------|---------|------|
| **DISPLAY NAME** | `Design to Code` | 英文显示名，简洁明了 |
| **SLUG** | `design-to-code` | 已自动从文件夹名派生，全小写+短横线 |
| **SHORT SUMMARY** | `将设计稿、UI截图、Figma链接或手绘草图转换为可直接运行的本地全栈应用代码。支持解析设计结构、提取样式参数、生成多端响应式代码、自动推导数据库Schema与RESTful API，输出可立即启动的完整项目。` | 200字符以内 |
| **PUBLISHING AS** | `@JainWong` | 你的账号，保持默认即可 |
| **VERSION** | `1.0.0` | 已写入 SKILL.md frontmatter |
| **RELEASE TAGS** | `latest` | 默认即可 |
| **CATEGORIES** | `Development` / `Web` / `Productivity` | 建议勾选这3个分类 |
| **TOPICS** | `design-to-code` / `frontend` / `fullstack` / `react` / `nextjs` / `responsive-design` | 可添加这些主题标签 |

---

## 3. 关键注意事项

- **Slug 规则**：`design-to-code` 全为小写字母+短横线，无大写字母，符合 `^[a-z0-9][a-z0-9-]*$` 正则要求
- **SKILL.md 验证**：ClawHub 会自动检查 frontmatter 中是否包含 `name` 和 `description`，已满足
- **文件类型**：仅 `SKILL.md` 一个文本文件，无脚本/二进制文件，无需声明 `requires.env` 或 `requires.bins`
- **许可证**：ClawHub 所有 skill 默认使用 MIT-0 许可证，不可修改
- **总大小**：当前约 12KB，远小于 50MB 限制

---

## 4. 快速复制

以下是可以直接粘贴到 ClawHub 表单的内容：

**DISPLAY NAME**
```
Design to Code
```

**SHORT SUMMARY**
```
将设计稿、UI截图、Figma链接或手绘草图转换为可直接运行的本地全栈应用代码。支持解析设计结构、提取样式参数、生成多端响应式代码、自动推导数据库Schema与RESTful API，输出可立即启动的完整项目。
```

**VERSION**
```
1.0.0
```

**CATEGORIES 推荐选择**
- Development
- Web
- Productivity

**TOPICS 推荐标签**
- design-to-code
- frontend
- fullstack
- react
- nextjs
- responsive-design
