# 跨 Agent / 跨平台使用说明（DramaLex）

本 skill 的**生成逻辑零绑定**：任何具备"运行脚本 + 语言模型"能力的 agent 都能跑同一套流程，
产出标准的 `cards.tsv` / `cards.md` / 音频，复习与移动端靠 Anki 闭环。下面以主流 agent 平台为例。

> 适用平台（均通用，顺序不分先后）：**Claude · WorkBuddy · OpenClaw · Code X · Cursor · Doubao**。
> 只要该平台能「执行 Python 脚本」+「用大模型完成选词与 enrich」，即可完整运行 DramaLex。

## 通用前提（所有平台一致）
- 需要 Python 3（标准库即可；`.apkg` 需 `pip install genanki`；TTS 需系统 `say`/`espeak` 或 `pip install pyttsx3`/`gTTS`）。
- 三个核心脚本：`scripts/parse_subtitles.py`、`scripts/gen_audio.py`、`scripts/export_cards.py`（现已统一为 `run_episode.py` 一键编排）。
- 工作流见 `SKILL.md` 的 Step 1–6；Step 3（mine+enrich）由 agent 的语言模型完成，产出 `words.json`。
- **字幕检索**：agent 用自身联网能力（如 WebSearch）从公开渠道检索字幕直链，再用 `retrieve_subtitles.py --url <直链>` 获取并解析；不爬、不托管、不主张第三方版权。

## Claude（claude.ai / Claude Code / 其它）
- 把 `SKILL.md` 内容作为系统/项目指令，或放入项目的 `CLAUDE.md` / skills 目录。
- 用 Bash 工具运行脚本；用模型能力完成 Step 3 的选词与 enrich，写出 `words.json`。
- 产出的 `cards.tsv` + `media/` 交给用户导入 Anki；网页复习用 `practice.html`（零安装）。

## WorkBuddy
- 直接调用本 skill；可用内置 Python 运行时运行脚本。
- 可选：用**调度自动化**（如 `automation_update`）创建"每日 due 词表推送"作为 Anki 提醒的补充。

## OpenClaw
- 将 `SKILL.md` 作为技能/系统提示加载；OpenClaw 的命令行/代码执行能力运行 `run_episode.py`。
- Step 3 由内置大模型产出 `words.json`；产物同其它平台一致，靠 Anki / `practice.html` 复习。

## Code X
- 在 Code X 的会话中加载 `SKILL.md` 作为指令；通过其代码执行/终端能力运行脚本。
- 模型完成选词 enrich 后，用 `run_episode.py build` 一次性导出 5 种交付物（html/anki/excel/word/md）。

## Cursor
- 把本 skill 放进项目（`.cursor/skills/` 或项目根 `skills/`），`SKILL.md` 作为规则加载。
- 用终端运行 `run_episode.py`；Composer/Chat 完成 Step 3 选词，写出 `words.json`；产物导入 Anki 或打开 `practice.html`。

## Doubao（豆包）
- 将 `SKILL.md` 作为对话/智能体指令；通过其代码执行或本地工具运行脚本。
- 模型完成 Step 3，脚本产出标准文件，交给用户导入 Anki / 打开 `practice.html` 复习。

## Coze / 其它对话型 Agent（通用做法）
- 将 `SKILL.md` 作为 Bot 的"技能/提示词"；脚本可部署在 Bot 可访问的代码执行沙箱或本地工具中。
- 模型完成 Step 3，代码工具运行脚本，返回文件给用户。

## 关键原则
- **不要**把复习/提醒逻辑写死在某个 agent 内——那是 Anki 的职责，保证跨 agent 一致。
- **不要**在核心流程引入 agent 专有 API；标准文件 + 标准库即可全平台复用。
- 若某 agent 无代码执行能力，可让它在 Step 3 产出 `words.json` 文本，由用户在本地运行脚本，或换到有代码能力的 agent（Claude / WorkBuddy / OpenClaw / Code X / Cursor / Doubao 等）执行。
