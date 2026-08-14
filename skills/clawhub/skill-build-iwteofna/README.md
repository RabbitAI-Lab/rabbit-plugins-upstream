# PDF阅读助手 · WorkBuddy Skill

"PDF 阅读助手技能 v2.0。支持文本提取、表格提取、扫描版OCR识别、智能问答、多文档对比、批量处理。触发词：PDF、阅读PDF、分析PDF、PDF摘要、提取PDF、研报、论文、文档分析。"

## 特性

- 请参考 SKILL.md 中的详细说明

## 安装

### WorkBuddy 技能市场（推荐）

在 WorkBuddy 中搜索「PDF阅读助手」一键安装。

### 手动安装

```bash
git clone https://github.com/guipi888/pdf-reader-assistant.git \
  ~/.workbuddy/skills/pdf-reader-assistant
```

### 环境依赖

请参考 SKILL.md 中的环境要求章节

## 使用

```bash
python3 scripts/pipeline.py <参数>
```

详细参数请参考 SKILL.md

## 输出

请参考 SKILL.md

## 项目结构

```
.gitignore
LICENSE
SKILL.md
assets
references
scripts
scripts/analyze_pdf.py
scripts/extract_pdf.py
```

## 关于作者

**桂皮 Guipi** — AI Agent 开发者 · 超级个体践行者
专注 AI 效率工具与一人公司方法论，帮普通人用 AI 成为超级个体

| 平台 | 账号 |
|------|------|
| 📱 小红书 | [桂皮AI实战](https://www.xiaohongshu.com/user/profile/5a409dda44363b313b9d7e15) |
| 🎬 抖音 | [桂皮AI实战](https://v.douyin.com/QJRjHGAtrvA/) |
| 📺 视频号 | 微信内搜「桂皮AI实战」|
| 💬 公众号 | 微信搜「桂皮AI实战」|
| 🐙 GitHub | [guipi888](https://github.com/guipi888) |
| 💬 微信 | guipi996（注明来意）|

## License

MIT License — 详见 [LICENSE](./LICENSE)
