# Agent Subtitle Translator Skill

<p align="center">
  <img src="assets/icon-large.png" alt="Agent Subtitle Translator Logo" width="180">
</p>

[English](README.md)

安全翻译单个 SRT、VTT 或 ASS 字幕文件：时间轴在本地处理，字幕 ID 严格校验，并尽可能完整保留 ASS 结构。

本仓库首先是一个 Skill。内置 CLI 负责确定性的解码、解析、分批、校验和合成；执行 Agent 使用自身可用的翻译模型，因此 CLI 不需要外部 LLM API Key。

> ⭐ 如果这个 Skill 对你有帮助，请为[本仓库点一个 Star](https://github.com/Lumen01/agent-subtitle-translator)。你的支持能让更多人发现这个项目，也会鼓励项目持续改进。

## 安装 Skill

### 让 Agent 执行安装

将下面这段 Prompt 交给有终端权限的 Agent：

```text
请按照 https://github.com/Lumen01/agent-subtitle-translator 的安装说明安装此 Skill，并确认当前 Agent 能够使用。若与现有安装冲突，请先告知我。
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

## Agent 执行顺序

Agent 使用本 Skill 时，可以直接运行确定性 CLI。需要观察实时进度时，再按以下步骤启用本地 visualizer：

1. 在 Skill 目录检查环境：安装或确认 `requirements.txt` 中的 Python 依赖，确认 Python 能运行 `scripts/subtitle_tool.py --help`，确认 Node.js 为 20 或更高版本；需要时运行 `npm install`，并确认 `npm run build` 成功。
2. 检查 `http://127.0.0.1:4317/api/health`。只有健康状态正确、服务标识为 `subtitle-visualizer` 且 Skill 版本兼容时才复用；否则先处理端口占用，再启动服务。
3. 需要观察实时进度时，在指定浏览器中打开服务打印的本机 URL，并报告页面是否加载成功。
4. 运行 `visualizer:bridge -- identify`，然后创建任务、翻译批次、校验响应，并通过 bridge compose。

下面的 CLI 代码块是确定性核心能力参考。同一任务和输出路径不要混用 CLI compose 与 bridge compose。

## 确定性 CLI 参考

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

运行 `python3 scripts/subtitle_tool.py --help` 及各子命令的 `--help` 可查看碰撞与重试参数。生成的批次 Prompt 只包含正文和稳定 ID，不包含时间轴或原始 ASS override 标签。最终报告与字幕位于同一目录，路径为 `<output-path>.report.json`；例如 `SPS.ja.srt` 对应 `SPS.ja.srt.report.json`。如果输出已存在，请选择新路径；只有明确要替换原结果时才使用显式覆盖参数。

## 本地翻译过程可视化

本 Skill 提供一个可选的、只负责展示的本地 Web 工作台，适合普通用户同时观察多个由 Agent 创建的字幕翻译任务。左侧显示任务队列，点击任务后，右侧会展示批次进度、校验、重试、降级、翻译耗时、字幕明细和实时事件流。字幕文件、目标语言和翻译控制全部在 Agent 中完成，Web 页面不接受任务输入。原有 Python CLI 继续负责确定性的字幕处理核心。

Agent 使用 visualizer 时，bridge 是唯一的任务执行入口。上面的 CLI 命令仍可用于纯 CLI 调用；同一任务和输出路径不要先后通过两套入口重复 compose。

在 Skill 目录启动或复用本地服务：

```bash
npm install
curl -fsS http://127.0.0.1:4317/api/health
```

当健康接口返回 HTTP 200，且 JSON 中 `status` 为 `"ok"`、`service` 为 `"subtitle-visualizer"`，版本与当前 Skill 兼容（本版为 `1.1.1`）时，复用现有实例并仅在需要观察实时进度时打开其 URL，跳过第二次启动。请求失败或版本不兼容时，先处理占用端口，再启动当前版本。如果端口被其他服务占用，应报告冲突并选择其他端口或有意处理，不要自动终止未知进程。服务只监听 `127.0.0.1`，任务历史保存在仓库外的 `~/.agent-subtitle-translator/visualizer`。Agent 需要观察进度时显式打开打印出的本机 URL。Agent 端同时继续输出任务创建、字幕准备、批次处理、校验、重试、降级和最终生成状态。服务不会调用翻译服务，也不要求配置 API Key；Agent 通过桥接命令上报真实执行过程：

```bash
npm run visualizer:bridge -- identify \
  --agent "Agent 名称" \
  --model "模型名称" \
  --model-version "5.6" \
  --model-series "Sol" \
  --reasoning-strength "high"

npm run visualizer:bridge -- create \
  --input ~/Movies/movie.en.srt \
  --target-language zh-Hans

npm run visualizer:bridge -- batch-start --task TASK_ID --batch 1
# 将 batches/batch-0001.txt 完整发送给当前可用的翻译模型。
npm run visualizer:bridge -- submit-response \
  --task TASK_ID \
  --batch 1 \
  --response /tmp/batch-0001.txt

npm run visualizer:bridge -- compose --task TASK_ID
```

bridge 默认拒绝覆盖已有字幕或报告。`--output` 只能指定当前任务私有 output 目录中的文件名。需要生成另一份结果时，请传入新的文件名；明确替换同一结果时，才追加 `--overwrite`：

```bash
npm run visualizer:bridge -- compose --task TASK_ID --overwrite
```

报告位于输出字幕旁边，路径为 `<output-path>.report.json`。

如果校验失败，先在 Web 任务中记录失败，再使用原始 Prompt 和校验错误重试；发送重试前运行 `retry-batch --task TASK_ID --batch 1`。只有完成规定重试且剩余问题为 ASS `S` 样式标记不匹配时，才可以使用 `--allow-style-fallback`。

运行 identify 后，Web 页面会在会话行显示 Agent，并在每个任务卡片内显示该任务记录的翻译模型；下方程序元数据显示共用的程序与 Skill 版本，该版本统一从 package.json 读取。Agent 知道完整模型标识时，应将它作为 `--model` 传入，例如 `GPT-5.6 Luna Hight`；也可以通过 `--model-version`、`--model-series` 和 `--reasoning-strength` 传入 `GPT`、`5.6`、`Sol`、`high` 这类结构化信息。旧模型或其他模型缺少可选字段时，Web 页面会自动省略对应字段；Agent 无法确认的值不应自行补全。建议在每次可视化会话开始时先执行一次 identify。Web 页面只展示 Agent 创建和控制的任务。纯 CLI 流程可以不启动 Web 服务；visualizer 启用后，任务创建、校验和 compose 都应保持在 bridge 入口。

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
npm install
npm test
```
