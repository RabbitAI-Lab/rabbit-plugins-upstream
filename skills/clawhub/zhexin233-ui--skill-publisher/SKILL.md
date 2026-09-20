---
name: ClawHub 技能一键发布器
description: 将本地技能一键打包、生成中文 PDF 说明文档、发布到 ClawHub，并自动截取发布页截图与链接，形成「创建→发布→文档→留证」的完整闭环。
version: 1.0.3
tags:
  - clawhub
  - publish
  - automation
  - documentation
  - pdf
---

# ClawHub 技能一键发布器

> 激活词：发布技能 / 上传到 ClawHub / 技能发布流水线 / publish skill

## 何时使用
- 你需要把一个本地技能（含 `SKILL.md` 的文件夹）发布到 [ClawHub](https://clawhub.ai) 公开市场。
- 你希望同时生成一份中文 PDF 说明文档，并在发布后留存「网页链接 + 页面截图」作为证据。
- 你想要把「创建技能 → 写文档 → 上传平台 → 留证」这一整套流程自动化，而不是逐步手工操作。

## 核心功能
1. **技能包校验**：检查目标文件夹是否包含 `SKILL.md`，并校验 frontmatter 中的 `name` / `description` / `version` 等关键字段。
2. **PDF 说明文档生成**：调用 Python + reportlab（内置 `STSong-Light` 中文字体）生成一份结构化的中文 PDF，包含技能简介、功能说明、使用示例与发布命令。
3. **ClawHub 发布**：通过 `clawhub` CLI 以 API Token 非交互方式登录并发布，支持 `--json` 输出，自动解析出技能展示网址。
4. **页面截图留证**：用无头浏览器（Playwright / 浏览器工具）打开发布页并截图，形成可视化证据。
5. **汇总输出**：把 PDF、技能 URL、截图路径一并交给用户，完成全流程闭环。

## 前置条件
- 已安装 Node.js，可执行 `clawhub` CLI（或本包内的 `scripts/` 脚本自动安装）。
- 拥有一个 ClawHub 账号，并取得 **API Token**（在 ClawHub 网站设置中获取）。
- 本地文件系统写入权限（用于生成 PDF 与截图）。

## 使用方法
```bash
# 1. 准备技能文件夹 skill-dir/（含 SKILL.md）
# 2. 设置 Token（或从 ClawHub 网站复制）
export CLAWHUB_TOKEN="你的_API_Token"

# e. 运行发布脚本（校验 + PDF + 发布 + 截图）
python scripts/publish.py --skill ./skill-dir --slug my-skill --name "我的技能" --token "$CLAWHUB_TOKEN"
```

仅生成 PDF（不发布）：
```bash
python scripts/publish.py --skill ./skill-dir --pdf-only
```

仅校验 + 预览发布（不真正上传）：
```bash
clawhub skill publish ./skill-dir --slug my-skill --name "我的技能" --dry-run --json
```

## 发布命令参考
```bash
clawhub login --token <API_TOKEN>          # 非交互登录
clawhub skill publish ./skill-dir \
  --slug <slug> --name "<名称>" --version 1.0.0 \
  --tags "tag1,tag2" --json
# 成功后 JSON 中包含展示网址：https://clawhub.ai/<owner>/skills/<slug>
```

## 使用示例
假设你要把「Excel 考勤颜色解析」技能发布出去：
```python
from publish import publish_skill

result = publish_skill(
    skill_dir="./xlsx-attendance-color",
    slug="xlsx-attendance-color",
    name="Excel 考勤颜色解析",
    token="<API_TOKEN>",
)
print(result["url"])   # https://clawhub.ai/<owner>/skills/xlsx-attendance-color
```

## 最佳实践
- **描述清晰**：SKILL.md 的 `description` 要让用户一眼看懂用途，直接影响 ClawHub 搜索曝光。
- **示例完整**：提供可直接复制运行的命令与代码片段。
- **标签准确**：使用 `--tags` 标注领域，便于被发现。
- **版本规范**：遵循 semver（如 1.0.0）。
- **排除产物**：用 `.clawhubignore` 排除构建产物（如 `dist/`），避免把 PDF/截图等生成文件发布到平台。`clawhub skill publish` 没有 `--exclude` 参数，但会自动读取 `.clawhubignore` / `.clawdhubignore` / `.gitignore` 忽略规则。**本技能的 `publish.py` 已内置 `ensure_ignore()`，发布前会自动创建/补全 `.clawhubignore`（默认排除 `dist/`、`*.pdf`、`*.png` 等），无需手动维护。** 每次重新发布 ClawHub 会在原版本号上自动 bump patch。
- **留证完整**：发布后务必保存 URL 与截图，便于后续复核与回滚。
