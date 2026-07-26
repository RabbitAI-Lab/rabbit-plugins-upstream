<p align="center">
  <img src="assets/icon-large.svg" alt="Agent Subtitle Translator Logo" width="180">
</p>

# Agent Subtitle Translator Skill

[English](README.md)

安全翻译单个 SRT、VTT 或 ASS 字幕文件：时间轴在本地处理，字幕 ID 严格校验，并尽可能完整保留 ASS 结构。

本仓库首先是一个 Skill。内置 CLI 负责确定性的解码、解析、分批、校验和合成；执行 Agent 使用自身可用的翻译模型，因此 CLI 不需要外部 LLM API Key。

> ⭐ 如果这个 Skill 对你有帮助，请为[本仓库点一个 Star](https://github.com/Lumen01/agent-subtitle-translator)。你的支持能让更多人发现这个项目，也会鼓励项目持续改进。

## 安装 Skill

### 让 Agent 执行安装

将下面这段 Prompt 交给有终端权限的 Agent：

```text
请阅读 https://github.com/Lumen01/agent-subtitle-translator/blob/main/README.md，并按照其中“Install Manually”章节安装 Agent Subtitle Translator Skill。修改前先检查现有安装并保留无关文件。除非我明确要求仅安装到一个运行时，否则优先在 ~/.agents/skills 下安装一份供多个 Agent 共享的版本，并在不制造冲突副本的前提下将它暴露给我指定的各个运行时。在适当的用户环境或托管环境中安装声明的 Python 依赖，然后确认运行时能够发现已安装的 SKILL.md。不要在未比较并报告冲突前覆盖或删除现有安装。
```

### 手工安装

#### 多 Agent 共用

为 Codex、Claude、OpenCode 等兼容运行时安装一份共享副本：

```bash
git clone https://github.com/Lumen01/agent-subtitle-translator.git ~/.agents/skills/agent-subtitle-translator
python3 -m pip install --user -r ~/.agents/skills/agent-subtitle-translator/requirements.txt
```

如果运行时要求使用自己的 Skill 目录，将其指向共享副本：

```bash
mkdir -p ~/.codex/skills ~/.claude/skills
ln -s ~/.agents/skills/agent-subtitle-translator ~/.codex/skills/agent-subtitle-translator
ln -s ~/.agents/skills/agent-subtitle-translator ~/.claude/skills/agent-subtitle-translator
```

执行前先检查每个目标位置；不要盲目替换已有文件、目录或链接。

#### 仅供一个运行时使用

直接克隆到该运行时文档约定的 Skill 目录。例如：

```bash
git clone https://github.com/Lumen01/agent-subtitle-translator.git ~/.codex/skills/agent-subtitle-translator
python3 -m pip install --user -r ~/.codex/skills/agent-subtitle-translator/requirements.txt
```

安装后的 Skill 根目录必须包含可发现的 `SKILL.md`。

## 提示 Agent 使用

在 Prompt 中写明 Skill、一个输入文件和必填的目标语言；源语言可省略。

```text
使用 $agent-subtitle-translator 将 ~/Movies/movie.en.srt 翻译为简体中文（zh-Hans）。保留原时间轴，不覆盖已有输出，并报告所有降级项。
```

```text
使用 $agent-subtitle-translator 将 ~/Movies/signs.ass 从英语翻译为巴西葡萄牙语（pt-BR）。尽可能保留 ASS 样式和事件元数据。
```

Agent 会以每批最多 32 条字幕准备任务，使用自身可用模型翻译，重试结构无效的批次，严格校验稳定 ID 和标记，并只在全部批次都能安全映射后合成。Skill 不设置并发上限；批次结果按稳定 ID 合并，不按完成先后合并。

## 支持格式与输出

| 输入 | 输出 | 行为 |
| --- | --- | --- |
| SRT | SRT | 保留时间轴；规范化编号和时间顺序。 |
| VTT/WebVTT | SRT | 在本地转换为规范化 SRT。 |
| ASS | ASS | 保留文档和事件结构，只替换 Dialogue 的可见正文。 |

默认输出名为 `<stem>.<规范化-BCP47>.<ext>`，例如 `movie.zh-Hans.srt` 或 `movie.pt-BR.ass`。除非使用对应的显式覆盖参数，否则不会覆盖已有工作目录、已校验响应、字幕输出或报告。SRT 与 ASS 输出使用 UTF-8 BOM。

CLI 可直接识别 UTF BOM 和 UTF-8，并通过 `charset-normalizer` 检测常见旧编码；检测结果过于含糊时会停止，以免错误映射。准备报告会列出条目数、时间范围、排序、空正文、格式转换和 ASS 专属保留信息。

## ASS 样式保持与卡拉 OK 降级

原始 ASS 标签不会提交给翻译模型。行内样式范围会转换为 `⟦S1⟧...⟦/S1⟧` 这类成对中性标记，标记可随对应语义在目标语言中移动。硬换行会转换为唯一、可移动的 `BR` 标记。翻译完成后，CLI 会校验标记数量、身份、闭合和嵌套，再恢复原标签。

例如，以下原文：

```text
What date is {\b1\c&H00FFFF&}today{\r}?
```

可以安全得到：

```text
{\b1\c&H00FFFF&}今天{\r}是几号？
```

如果重试后仍无法恢复某条字幕的行内样式，Agent 可显式地只把该条降级为静态文本，并必须报告其 ID。条数、ID、外层结构、硬换行或固定结构不匹配仍是致命错误；Skill 绝不会借用相邻译文，也不会根据字符位置猜测样式。

含 `\k`、`\K`、`\kf` 或 `\ko` 卡拉 OK 计时的条目会按条明确降级。输出保留事件时间轴、基础 Style、其他字段和安全的整行位置，但移除逐音节计时和不再适用的字符动画。该情况会作为降级报告，而不是翻译失败。同一文件中的其他普通 ASS 条目仍保留受支持的样式。

## 典型 Agent 工作流

Agent 通常在已安装的 Skill 目录运行以下命令：

```bash
python3 scripts/subtitle_tool.py prepare /path/movie.ass --target-language zh-Hans --source-language en

python3 scripts/subtitle_tool.py validate-response \
  --manifest /path/.movie.zh-Hans.subtitle-work/manifest.json \
  --batch 1 \
  --response /path/responses/batch-0001.txt

python3 scripts/subtitle_tool.py compose \
  --manifest /path/.movie.zh-Hans.subtitle-work/manifest.json
```

运行 `python3 scripts/subtitle_tool.py --help` 及各子命令的 `--help` 可查看碰撞与重试参数。生成的批次 Prompt 只包含正文和稳定 ID，不包含时间轴或原始 ASS override 标签。

## 自动发布到 ClawHub

`.github/workflows/clawhub-publish.yml` 会在相关文件推送到 `main` 时自动发布本技能。它使用 ClawHub 官方可复用工作流：未变更内容会被跳过；技能有变更时会自动发布下一个 patch 版本。

首次运行前，请添加名为 `CLAWHUB_TOKEN` 的仓库 Actions Secret：

1. 以该技能所有者身份登录 ClawHub，在网页中创建 ClawHub API token。
2. 在 GitHub 仓库打开 **Settings → Secrets and variables → Actions**，新建名为 `CLAWHUB_TOKEN` 的 Secret，并填入该 token。
3. 在 Actions 页面手动运行一次 **Publish Subtitle Translator to ClawHub**，或向 `main` 推送相关改动。

该 token 只会传给发布工作流，绝不能提交到仓库。

## 开发与测试

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
python3 -m py_compile scripts/subtitle_tool.py tests/test_subtitle_tool.py
python3 /path/to/skill-creator/scripts/quick_validate.py .
```
