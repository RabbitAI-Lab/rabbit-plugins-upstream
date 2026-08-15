# Style Extractor

从 URL、截图或前端项目源码中逆向提取 UI 视觉风格，产出三层 Design Token 系统，封装为可复用的通用风格技能。

## 核心特性

- **三种输入源** — URL（自动抓取 CSS）、截图（多模态分析）、前端项目源码（解析 Tailwind/CSS/Theme）
- **三层 Token 架构** — Primitive（原材料）→ Semantic（设计角色）→ Component（组件特化），解耦值与角色
- **四级证据标注** — D（已定义）/ M（已测量）/ I（有依据归纳）/ A（暂时假设），每一条 token 都可追溯
- **多运行模式** — 审计（只盘点）/ 设计（建三层）/ 打包（生成技能）/ 验证（8 项检查 + demo 页）
- **通用输出格式** — 产出标准 WorkBuddy 风格技能，不限任何 AI 工具

## 快速开始

```
/style-extractor https://linear.app
/style-extractor ./my-nextjs-app
/style-extractor screenshot.png
```

## 工作流

| 阶段 | 模式 | 产物 |
|---|---|---|
| Phase 1 — 审计 | 审计模式 | 证据清单、原始值、冲突发现 |
| Phase 2 — 设计 | 设计模式 | 三层 Token（Primitive → Semantic → Component） |
| Phase 3 — 打包 | 生成模式 | 完整 WorkBuddy 风格技能 + 5 个参考文档 |
| Phase 4 — 验证 | 验证模式 | 格式/引用/层级/主题 8 项检查 + 可选 demo 页 |

## 输出技能结构

```
brand-style-{name}/
├── SKILL.md                    # 三层架构总览 + 快速参考
└── references/
    ├── colors.md               # Primitive 色阶 + Semantic 颜色角色 + 主题映射
    ├── typography.md            # Primitive 字号阶梯 + Semantic 文字角色
    ├── spacing.md               # Primitive 间距/圆角/阴影 + Semantic 布局角色
    ├── components.md            # Component 层 + 组件指纹
    └── known-gaps.md            # 来源冲突、待确认假设、设计例外、提取局限
```

## 内置参考

- `references/extraction-checklist.md` — 带证据标注的完整提取清单
- `references/output-format.md` — YAML + 三层 Token 输出格式规范
- `references/validation-checklist.md` — 8 项后验证检查
- `references/common-pitfalls.md` — 5 类常见翻车 + 避坑指南

## 设计理念

基于 [Kryon 的文章](https://mp.weixin.qq.com/s/SwzGgLLW9RC2fTDw1cWRZQ) 和 [skillui](https://www.npmjs.com/package/skillui) 的实践，融合了三层 Token 架构、证据分级系统和后验证闭环。

**不要做的事**比**应该做什么**更有价值——详见 `references/common-pitfalls.md`。

## 作者

- **Author**: [namepain](https://github.com/namepain)
- **GitHub**: https://github.com/namepain/style-extractor
