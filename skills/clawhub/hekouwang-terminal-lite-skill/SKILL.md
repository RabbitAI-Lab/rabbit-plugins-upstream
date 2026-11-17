---
name: hekouwang-terminal-lite-skill
description: "会勇禾口王·终端工作台（免费版）/ Hekouwang Terminal Lite：安装或迁移 macOS 终端/.zshrc、社区主题、doctor、CLI diff、卸载。不含多终端同步、光学校准、场景与工作区——那些在专业版 hekouwang-terminal-skill。"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
metadata:
  version: 3.0.0
  displayName: 会勇禾口王·终端工作台（免费版）
  openclaw:
    requires:
      bins:
        - bash
        - zsh
        - python3
---

# 会勇禾口王·终端工作台（免费版）

> **定位**：免费版 Agent 操作协议。人类看 [`README.md`](README.md)；深手册看 [`docs/manual.zh-CN.md`](docs/manual.zh-CN.md)。
> **英文名**：Hekouwang Terminal Lite · Skill 名：`hekouwang-terminal-lite-skill`
> **专业版**：`hekouwang-terminal-skill`（另一名字，装一个不会覆盖另一个）。

`<skill>` = 本文件所在目录。

## Agent 协议

1. 先 `./scripts/doctor.sh --status`；已有自定义 `.zshrc` 先 `./scripts/migrate.sh`，禁止直接 `install.sh`。
2. 换肤先 `./scripts/theme.sh --plan <name>`；写操作须用户明确要求。
3. 改色板只改源再生成；禁手改生成物。
4. Node 管理器只留一个。
5. **本包是免费版**：不要承诺多终端同步、光学校准、场景、工作区、色板推导、跟随系统深浅色；那些文件不在本树。

## 免费版有什么

- iTerm2：3 套社区主题、毛玻璃、Triggers、语义 Cmd-click、Shift+Enter
- 安装 / 迁移 / 卸载 / doctor / sync / update / node-mgr / setup-gui / setup-cli
- `theme.sh`：iTerm2 换肤 / 画廊 / 预览 / audit / P3
- `unlock.sh`：把专业版 zip 解压覆盖进本树

专业版能力缺席时，生成器仍出完整 iTerm2 主题，多终端行显示跳过——不报错、不留半成品。

## 脚本

| 脚本 | 用途 |
|---|---|
| `doctor.sh` | `--status` / `--parity` / `--profile` / `--fix` |
| `install.sh` / `migrate.sh` / `uninstall.sh` | 装 / 接管 / 卸（先 dry-run） |
| `theme.sh` | iTerm2 换肤；`--plan` / `--preview` / `--gallery` / `--audit` |
| `node-mgr.sh` / `setup-gui.sh` / `setup-cli.sh` | Node；GUI；AI CLI diff |
| `sync.sh` / `update.sh` / `unlock.sh` | 多机；更新；装专业版 zip |

## 常用命令

```bash
./scripts/install.sh --dry-run && ./scripts/install.sh
./scripts/migrate.sh && ./scripts/migrate.sh --apply
./scripts/theme.sh --plan tokyo-night && ./scripts/theme.sh tokyo-night
./scripts/doctor.sh --status
./scripts/uninstall.sh --dry-run
```

## 语言与文档层

站点 / README 默认中文。CLI 默认英文；`--lang zh` 可切。Agent 只读本协议；不要把 README 营销段复述成能力承诺。
