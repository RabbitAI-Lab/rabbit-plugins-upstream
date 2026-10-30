# text-to-infographic

把文本变成**可编辑、可校验、可安全分享**的单页信息图。

- **结构化 plan**：信息图先写成 JSON（schema 见 `schemas/`），改一个块 = 重渲染，不推倒重来；
- **信息正确校验**：布局语义（飞轮必须闭环、鱼骨只能单头、桑基必须守恒、仪表盘必须有单位）+ 数值可溯源；
- **chart_family 六布局**：flywheel / fishbone / sankey / pyramid / timeline / dashboard —— 通用模板库不覆盖的专用布局；
- **安全渲染**：产物为单文件静态 HTML，零 JavaScript、零外部请求、零依赖安装，离线可用、可打印。

## 快速开始

```bash
python3 scripts/validate_infographic_plan.py examples/flywheel-demo.json
python3 scripts/render_infographic_html.py examples/flywheel-demo.json out.html
```

仅需 Python 3.10+ 标准库。

## 文档

- SKILL.md —— agent 调用契约
- docs/校验规则规格 —— A/B/C 三层校验设计
- CHANGELOG.md —— 版本历史
