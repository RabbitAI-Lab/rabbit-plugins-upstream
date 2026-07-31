# xhs-image-note-release

> 通过 ego-browser 自动化发布小红书图文笔记，核心解决 closed Shadow DOM 发布按钮无法点击的问题。

## Features

- 全自动 9 步流程：打开创作平台 → 上传图片 → 填标题/正文 → 发布 → 清理
- CDP 批量上传图片（绕过 uploadFile 逗号分隔不生效的坑）
- **穿透 closed Shadow DOM 点击发布按钮**（`_onPublish()` 方法调用）
- 附带一键发布脚本，改 4 个参数即可复用
- 完整技术文档含 5 种失败方案对比表

## Quick Start

```bash
# Install (clawhub)
clawhub install xhs-image-note-release

# Or clone from monorepo
git clone https://github.com/Songhonglei/better-office-work-flow.git
cp -r better-office-work-flow/skills/xhs-image-note-release ~/.workbuddy/skills/
```

## Usage

详细使用方法见 [SKILL.md](./SKILL.md)。

## Install in your AI agent

| Agent | Install |
|---|---|
| OpenClaw | `clawhub install xhs-image-note-release` |
| Claude Code | Manual: copy to `~/.claude/skills/` |
| Cursor | Manual: copy to `.cursor/skills/` |

## License

MIT (see [LICENSE](./LICENSE))

## Author

Evan Song · [github.com/Songhonglei](https://github.com/Songhonglei)

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for the full version history.
