---
name: oss-design
description: |
  penguin-oss-suite 设计层路由——当开源协作涉及 UI/UX 时（修带界面的 bug、
  贡献组件库、建仓需要 landing page/docs 站），路由到对应设计 skill 和
  组件库规范。三层调度：①设计系统选择（Apple 极简/TDesign 企业/WeUI 微信/
  Material/shadcn 现代）②组件库规范（目标仓用什么库就遵循什么规范）③
  设计审查（Web Interface Guidelines 合规）。
  触发：S2 涉及 UI 组件的 bug / S5 建仓需要 docs 站或 landing page /
  贡献 UI 组件库（TDesign/WeUI/QMUI/tdesign）/ 「开源项目要做界面」。
  不触发：纯后端/CLI 项目、与 GitHub 协作无关的设计咨询。
---

# 设计层 · UI/UX 路由

> 开源协作不只是代码——帮别人的项目修 UI bug、给组件库提 PR、
> 建仓做 docs 站，都需要设计能力。本 skill 是设计层的路由器。

## §1 设计系统选择（按项目气质）

| 气质 | 设计系统 | 关键词 | 参考 skill |
|---|---|---|---|
| 极简高端 | Apple Design | 负字距标题/单色调+一个强调色/大留白/无装饰渐变 | apple-design + DESIGN-apple.md |
| 企业中后台 | TDesign | 腾讯开源企业级/多框架(React/Vue/小程序)/主题定制 | ui-ux-pro-max |
| 微信生态 | WeUI | 微信原生体验/小程序规范/轻量 | — |
| 现代开发工具 | shadcn/ui | Tailwind/Radix/可组合/暗色主题 | shadcn |
| 创意表现 | Libraries.dev | Border beam/Thinking orbs/液体金属等效果 | libraries-dev |

**选择原则**：跟着目标仓走——目标仓用什么组件库，就遵循什么设计规范。
不要把自己的偏好强加到别人的项目。

## §2 组件库规范（贡献 UI 库时必读）

### TDesign 系列（腾讯开源企业级 UI）
- 仓库：Tencent/tdesign-{vue-next,react,mobile-vue,mobile-react,...}
- 贡献前读：仓内 CONTRIBUTING + design 目录的设计规范
- 组件 PR 要过：视觉还原度 + 交互规范 + 无障碍 + 主题变量

### WeUI（微信原生 UI）
- 仓库：Tencent/weui + weui-wxss
- 贡献前读：微信小程序设计指南（weui 是其官方实现）
- 小程序 UI 修改需确认：iOS/Android 双端表现一致

### QMUI（Android/iOS UI 框架）
- 仓库：Tencent/QMUI_Android + QMUI_iOS
- 贡献前读：各自平台的 QMUI 规范文档

## §3 设计审查（写完 UI 后过一遍）

用 web-design-guidelines skill 检查：
- [ ] 可访问性（对比度/键盘导航/ARIA 标签）
- [ ] 响应式（320px/768px/1024px/1440px 四档）
- [ ] 暗色模式兼容（prefers-color-scheme）
- [ ] 性能（首屏 <3s/图片 lazy/字体 subsetting）

## §4 S 场景集成

| 场景 | 什么时候调用 | 调什么 |
|---|---|---|
| S2 修 bug | issue 涉及 UI 组件（按钮/表单/弹窗渲染异常） | §2 对应组件库规范 + frontend-ui-engineering |
| S2 修 bug | bug 是视觉问题（间距/颜色/排版错乱） | §1 设计系统 + DESIGN-apple.md token |
| S3 文档 | 目标仓 README 有截图/logo | oss-format §徽章/图片规则 |
| S5 建仓 | 需要 docs 站（VitePress） | §1 选择设计系统 + vitepress 主题定制 |
| S5 建仓 | 需要 landing page | frontend-design + design-taste-frontend |

## §5 设计 token 快查（来自 DESIGN-apple.md）

```yaml
# Apple 极简系（高端产品/开发者工具/文档站首选）
primary: "#0066cc"        # 唯一交互色
ink: "#1d1d1f"           # 正文
canvas: "#ffffff"        # 画布
canvas-parchment: "#f5f5f7"  # 浅灰区块
font: "SF Pro Display, system-ui"  # 系统字体栈
hero-size: 56px / 600 / -0.28px letter-spacing  # 大标题
# 原则：UI 退后让产品说话——无装饰渐变、无 chrome 阴影、仅产品图一个 drop-shadow
```

完整 token 见 references/design-tokens-apple.md（562 行：颜色/字体/间距/组件/动效/深色模式全覆盖）

## §6 与其他层的关系

| 层 | 管什么 | 本层怎么配合 |
|---|---|---|
| oss-voice | 文档写什么 | 设计文档的文案过 oss-voice |
| oss-format | 文档怎么排 | 设计文档的排版过 oss-format |
| oss-workflow | 场景路由 | S2/S5 checklist 的 UI Gate 调用本 skill |
| frontend-* skills | 具体实现 | 本 skill 路由到它们执行 |

## §7 外部设计 skill 资源

**ui-skills.com** — UI 设计/前端体验/动效/可访问性/设计系统/界面质感优化能力合集，可直接给 AI Agent 调用。当本 skill §1-§3 的规则不够用时（需要更细的动效/无障碍/质感指导），从这个合集按需拉取对应 skill 补充。

覆盖：UI 设计基础 · 前端体验 · 动效（micro-interaction/transition） · 可访问性（WCAG/screen reader） · 设计系统（token/组件规范） · 界面质感（polish/refinement）

## 诚实边界

- 设计 token 来自 Apple 公开设计语言的分析，非 Apple 官方规范
- Tencent org 组件库的完整规范在各自仓库内，本 skill 只做路由不做复制
- 设计审美有主观性——最终裁决权在目标仓的维护者

