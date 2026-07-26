# PlantUML Skill for OpenClaw

使用 PlantUML 文本语法绘制 UML 图和其他图表类型。

## 支持的图表类型

- 时序图 (Sequence Diagram)
- 类图 (Class Diagram)
- 活动图 (Activity Diagram)
- 用例图 (Use Case Diagram)
- 状态图 (State Diagram)
- 组件图 (Component Diagram)
- 部署图 (Deployment Diagram)
- 定时图 (Timing Diagram)
- 思维导图 (MindMap)
- 甘特图 (Gantt Diagram)

## 安装

将此仓库克隆到 OpenClaw 的 skills 目录：

```bash
git clone https://github.com/holdyounger/plantuml-skill.git ~/.openclaw/workspace/skills/plantuml
```

## 文件结构

```
plantuml-skill/
├── SKILL.md              # 主技能文件（语法参考）
├── README.md             # 本文件
├── examples/             # 示例 .puml 文件
│   ├── activity.puml
│   ├── class.puml
│   ├── gantt.puml
│   ├── mindmap.puml
│   ├── sequence.puml
│   └── state.puml
└── references/
    └── cheatsheet.md     # 速查表
```

## 使用

在 OpenClaw 中直接请求绘制图表，例如：
- "画一个用户登录的时序图"
- "画一个订单系统的类图"
- "画一个审批流程的活动图"
