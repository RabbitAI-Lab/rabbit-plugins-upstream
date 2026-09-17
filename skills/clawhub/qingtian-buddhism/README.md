# 青田·原始佛教修学助手 维护说明

> 当前版本：**v1.5.0**（生产可用，已改为发布版数据分发：语料与语义索引均从 ModelScope 数据集按需拉取，不捆绑大文件；内置 Grep + 语义双检索）。本 skill 已具备完整内容库，非草稿阶段。

## 它是什么
严格依据《巴利三藏巴利-中文对照译本（2026-06-21）》（ModelScope 数据集 `Wangzhenren/pali2026-06-21txt`）作答的原始佛教 / 上座部修学助手。所有经文、故事、教义、偈语均**逐句摘引自译本并标注出处**，不凭记忆编造，不把后世宗派发挥当作「佛说」。详见 `SKILL.md`（角色、教义护栏、触发路由、输出规范）。

## 安装与首次使用（重要）
1. 将本目录放入用户级技能目录：`~/.workbuddy/skills/qingtian-buddhism/`（Windows：`C:\Users\<用户>\.workbuddy\skills\qingtian-buddhism\`）。
2. **首次使用需联网拉取语料与语义索引**：在本技能目录下运行
   ```bash
   python scripts/setup_corpus.py
   ```
   脚本会从 ModelScope 公开数据集下载约 200MB 的 zip 解压到 `data/corpus/`，并下载语义索引 `pali_index.faiss` + `chunks.jsonl.gz` 到 `data/index/`（无需登录/密钥，仅需联网）。完成后生成 `data/corpus.ready` 与 `data/index.ready` 标记；之后启动会自动跳过下载。
3. **语义检索模型**（可选）：首次运行语义检索时会自动拉取 `BAAI/bge-base-zh`（约 400MB，sentence-transformers 缓存到本地，仅需联网一次）。若暂未安装依赖或离线，语义层自动降级，Grep 检索仍可用。
   ```bash
   pip install sentence-transformers faiss-cpu   # 语义检索所需（Grep 检索不需要）
   ```
4. `data/corpus/`、`data/index/`、`data/*.ready` 为**运行时自动生成**，发布包不应包含（见下方「发布注意事项」）。

## 目录速览
- `SKILL.md`：角色、教义护栏（最高优先级）、触发路由、输出规范。改这里 = 改行为。
- `references/`：所有内容。模型只从这里取料（护栏第 1 条）。
  - `stories/` 每日故事 **91 篇**（法句义注 45 + 本生 45 + 示范 1），按 `date_index`（1–91）循环
  - `suttas/` 经典 **20 篇**（按尼柯耶分目，含目录索引 README.md）
  - `teachings/` 核心教义词条 **16 篇**（四圣谛/八正道/三法印/五蕴/缘起…）
  - `pali/` 巴利术语小课堂 **61 篇**
  - `meditation/` 禅修引导 **5 篇**（入出息念/慈心禅/身至念/行禅/四护卫禅）
  - `figures/` 佛陀与圣弟子 **12 篇**（含目录索引 README.md）
  - `dhammapada/` 法句经偈颂 **423 篇**（`dhp-001…dhp-423`，**无 `date_index` 字段，按文件名编号定位**）
  - `practice-log.md` 修行打卡日志（追加式，跨会话持久）
  - `_sources.md` 内容出处与版权登记（已完整填充）
  - `canon-index.md` 217 个经文 txt 索引（相对路径，指向 `data/corpus/`）
- `scripts/setup_corpus.py`：首次使用从 ModelScope 拉取语料到 `data/corpus/` 与语义索引到 `data/index/`
- `scripts/semantic_search.py`：语义检索层（bge-base-zh + FAISS）。用法：
  ```bash
  python scripts/semantic_search.py "四圣谛"            # 自然语言问答，默认加 bge 中文指令
  python scripts/semantic_search.py "nibbāna" --no-instruct
  python scripts/semantic_search.py "哪些经讲缘起" --topk 8 --json
  ```
  返回 top-k 原文片段（含 `rel` 文件路径、`start/end` 偏移、`text`、`score`），便于定位与摘引。
- `data/corpus/`（运行时生成）：从数据集下载的原文 txt
- `data/index/`（运行时生成）：语义索引 `pali_index.faiss` + 映射 `chunks.jsonl.gz`

> 内容规模：故事 91 / 教义 16 / 巴利 61 / 经典 20 / 禅修 5 / 人物 12 / 偈语 423，合计 **628 个内容文件**，全部逐句摘引自 CANON_DIR（即 data/corpus/）并标注出处。

## 新增一篇内容的步骤
1. 在对应目录新建 `.md` 文件。
2. 文件头写 YAML 元数据，例如故事：
   ```yaml
   ---
   title: 标题
   category: 智慧|慈悲|无常|因果|修行|弟子   # 须取自 SKILL.md §八 受控词表
   source: 依据经号/阿含卷次（或注明「白话譬喻改写」）
   pali: ""
   date_index: 2                            # stories 必填（1–91 唯一）；dhammapada 不填（用文件名）
   ---
   ```
3. 按 `SKILL.md` 第四节的模块模板写正文。
4. 在 `_sources.md` 登记出处。

## 入库前必做
- **出处抽查**：随机抽 10 篇，确认经号、部派归属、巴利拼写无误。
- 自查是否踩 `SKILL.md` 负面清单；教义陈述是否挂了出处。
- **白话翻译**：叙事可白话重述，但偈语与经文摘引块须整段保留译本原文；默认纯中文，用户显式要求外语时才暂停中文限制（见 §三·8 / §五·一）。

## 发布注意事项
- 发布到 SkillHub 时，**不要**把已下载的 `data/corpus/`、`data/index/`、`data/*.ready`、`data/_corpus_download.zip` 纳入包；这些由使用者首次使用时 `setup_corpus.py` 自动生成（技能根 `.gitignore` 已忽略 `data/`）。
- 技能包应保持轻量（仅 SKILL.md / README.md / references/ / scripts/）。语义检索依赖 `sentence-transformers` + `faiss-cpu`，请在 README/发布说明中告知使用者按需 `pip install`。

## 如何激活
放入 `~/.workbuddy/skills/qingtian-buddhism/` 后重启/刷新，对话中提到佛陀、佛法、禅修等触发词即可唤起；首次对话涉及经文检索前，确保已运行过 `setup_corpus.py` 拉取语料。
