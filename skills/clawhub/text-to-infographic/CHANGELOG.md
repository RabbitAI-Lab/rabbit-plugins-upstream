# Changelog

## 1.2.2 (2026-10-27)

- 安全修复：`visual_system.accent` 之前直接插值进 CSS/SVG，可被构造值注入脚本/事件处理器/外链，违背「零脚本、零外链」承诺
- 渲染器边界严格校验：accent 只接受十六进制颜色（#RGB / #RRGGBB），非法值拒绝渲染
- 校验器同步拦截非法 accent（与 schema、渲染器三处一致）
- 产物 `<head>` 增加 CSP（`default-src 'none'`）阻断脚本与外部请求，双保险
- 新增回归测试 `scripts/test_render_security.py`（闭合标签/属性 breakout/CSS URL 等注入用例）
- SKILL.md 声明 `allowed-tools: Read, Write, Bash` 澄清工具边界

## 1.2.1 (2026-10-24)

- 修复 pyramid 布局错位：CSS clip-path 方案改为内联 SVG，坐标精确计算
- 层级顺序回归「blocks 第一个 = 基座」，配色由基座向顶层渐浅，右侧注释固定横排不再竖挤
- 清理废弃 CSS

## 1.2.0 (2026-10-21)

- 新增内置渲染器 `scripts/render_infographic_html.py`：plan JSON → 自包含静态 HTML（6 种 chart_family 布局，零 JS / 零外链 / 零依赖）
- 新增校验器 `scripts/validate_infographic_plan.py`：布局语义校验（A 层）+ 数值溯源（B 层，需 --source）+ 文本预算（C 层）
- 新增 `schemas/infographic-plan.schema.json` 与 6 个示例 plan
- 差异化叙事正式升级：可编辑 plan + 信息正确校验 + 安全渲染（零安装/无网络导出）
- 说明：v1.1.3 及之前为纯提示词版本（仅输出规格/HTML 源码），本版本起携带可执行工具

## 1.1.3 (2026-09-15)

- 纯提示词版本：单页信息图规格 + 可复制的静态 HTML 源码输出
