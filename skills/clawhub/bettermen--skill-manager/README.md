# Skill Manager — WorkBuddy Skill 全生命周期管理器

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.137-green.svg)](https://fastapi.tiangolo.com/)

一站式管理 WorkBuddy 本地和内置市场的所有 Skill。

## 功能

| 功能 | 说明 |
|------|------|
| 📋 列表 | 全量技能表格，含来源/版本/健康状态 |
| 👁 查看 | 展示 SKILL.md 完整内容与元信息 |
| ✨ 创建 | 调用 init_skill.py 初始化新技能 |
| 🗑 删除 | 二次确认删除自建技能 |
| 🔍 搜索 | Grep 搜索技能名和描述 |
| 🩺 审计 | 全量扫描，P0/P1/P2 三级报告 |
| 🔧 修复 | 自动清理 .zip 遗留 / .backup 重复 |
| 📦 打包 | 调用 package_skill.py 生成 .zip |
| ⬇ 安装 | 对接 BuiltinMarket 安装技能 |

## 快速开始

### CLI 模式

```bash
# 审计（最常用）
python scripts/audit.py --user ~/.workbuddy/skills/

# JSON 输出
python scripts/audit.py --user ~/.workbuddy/skills/ --json

# 自动修复
python scripts/audit.py --user ~/.workbuddy/skills/ --fix
```

### SaaS Dashboard 模式

```bash
# 安装依赖
pip install fastapi uvicorn

# 启动服务
python server.py --port 8765
```

浏览器打开 `http://localhost:8765` 即可使用 Web Dashboard。

API 文档：`http://localhost:8765/docs`

## 项目结构

```
skill-manager/
├── SKILL.md              # WorkBuddy Skill 定义文件
├── server.py             # FastAPI 后端 (SaaS Dashboard)
├── README.md
├── .gitignore
├── scripts/
│   └── audit.py          # 核心审计脚本
└── assets/
    └── index.html        # Dashboard 前端界面
```

## 技术栈

- **CLI**: Python 3.10+（纯标准库，零依赖）
- **后端**: FastAPI + Uvicorn
- **前端**: Vanilla HTML/CSS/JS + Chart.js (CDN)
- **数据源**: 文件系统（无需数据库）

## License

MIT
