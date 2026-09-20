# 青田·原始佛教修学助手 维护说明

> 当前版本：**v1.5.7**（生产可用；语料与语义索引从 ModelScope 数据集按需拉取，不捆绑大文件；内置 Grep + 混合/语义双检索；R3 固化故事「原文＋白话文」双段输出规范，白话文读取时现场生成、不预写入库；R4 本生故事改为优先取材本生义注（序分+叙事+结分），45 条本生条目逐条核验、修正 12 条；R5 依据发布预检完善可发现性与发布内容）。本 skill 已具备完整内容库，非草稿阶段。

## 它是什么
严格依据《巴利三藏巴利-中文对照译本（2026-06-21）》（ModelScope 数据集 `Wangzhenren/pali2026-06-21txt`）作答的原始佛教 / 上座部修学助手。所有经文、故事、教义、偈语均**逐句摘引自译本并标注出处**，不凭记忆编造，不把后世宗派发挥当作「佛说」。详见 `SKILL.md`（角色、教义护栏、触发路由、输出规范）。

## 安装与首次使用（重要）
1. 将本目录放入用户级技能目录：`~/.workbuddy/skills/qingtian-buddhism/`（Windows 对应：`%USERPROFILE%\.workbuddy\skills\qingtian-buddhism\`）。
2. **首次使用需联网拉取语料与语义索引**：在本技能目录下运行
   ```bash
   python scripts/setup_corpus.py
   ```
   脚本会从 ModelScope 公开数据集下载约 200MB 的 zip 解压到 `data/corpus/`，并下载语义索引 `pali_index.faiss` + `chunks.jsonl.gz` 到 `data/index/`（无需登录/密钥，仅需联网）。完成后生成 `data/corpus.ready` 与 `data/index.ready` 标记；之后启动会自动跳过下载。
3. **语义检索模型**（可选）：首次运行语义检索时会自动拉取 `BAAI/bge-base-zh`（约 400MB，sentence-transformers 缓存到本地，仅需联网一次）。若暂未安装依赖或离线，检索层自动降级（`hybrid_search.py --bm25-only` 无需模型），Grep 检索仍可用。
   ```bash
   pip install sentence-transformers faiss-cpu   # 语义/混合检索所需（Grep 检索不需要）
   ```
   > 注：faiss-cpu 对 Python 3.14 的轮子支持可能滞后；如安装失败，建议在 Python 3.10–3.12 的虚拟环境中运行检索脚本。
4. `data/corpus/`、`data/index/`、`data/*.ready` 为**运行时自动生成**，发布包不应包含（见下方「发布注意事项」）。

## 目录速览
- `SKILL.md`：角色、教义护栏（最高优先级）、触发路由、输出规范。改这里 = 改行为。
- `references/`：所有内容。模型只从这里取料（护栏第 1 条）。
  - `stories.md` 每日故事 **91 篇**（单文件，法句义注 45 + 本生 45 + 示范 1），按 `(date_index: N)`（N=1–91）循环定位；每篇含「故事正文（译本摘引）＋出处＋教法关联＋今日一得」四段；「白话文」为默认输出项，读取时现场生成（不预写入库）；**本生故事优先取材 `本生义注-1~7`（序分+叙事+结分，菩萨身份据此），本生-1/2 仅为偈颂**（v1.5.6）
  - `suttas/` 经典 **20 篇**（按尼柯耶分目，含目录索引 README.md）
  - `teachings/` 核心教义词条 **16 篇**（四圣谛/八正道/三法印/五蕴/缘起…）
  - `pali/` 巴利术语小课堂 **62 篇**
  - `meditation/` 禅修引导 **5 篇**（入出息念/慈心禅/身至念/行禅/四护卫禅）
  - `figures/` 佛陀与圣弟子 **12 篇**（含目录索引 README.md）
  - `dhammapada.md` 法句经偈颂 **423 篇**（单文件，按 `<!-- dhp:N -->` 注释标记定位，N=1–423）
  - `practice-log.md` 修行打卡格式说明与示例（实际打卡追加写入 `data/practice-log.md`，运行时数据，跨会话持久且更新不丢失）
  - `_sources.md` 内容出处与版权登记（已完整填充）
  - `canon-index.md` 217 个经文 txt 索引（相对路径，指向 `data/corpus/`）
- `scripts/setup_corpus.py`：首次使用从 ModelScope 拉取语料到 `data/corpus/` 与语义索引到 `data/index/`
- `scripts/semantic_search.py`：语义检索层（bge-base-zh + FAISS）。用法：
  ```bash
  python scripts/semantic_search.py "四圣谛"            # 自然语言问答，默认加 bge 中文指令
  python scripts/semantic_search.py "nibbāna" --no-instruct
  python scripts/semantic_search.py "哪些经讲缘起" --topk 8 --json
  python scripts/semantic_search.py "四圣谛" --context 800   # 附带原文上下文（自动 CRLF→LF）
  ```
  返回 top-k 原文片段（含 `rel` 文件路径、`start/end` 偏移、`text`、`score`、可选 `context`）。⚠️ `start/end` 是 LF 归一化文本的字符偏移，需要上下文请用 `--context` 或模块 `resolve_context()`，勿自行切片。
- `scripts/hybrid_search.py`：**混合检索**（BM25 关键词 + FAISS 向量，RRF 融合；模糊问推荐）：
  ```bash
  python scripts/hybrid_search.py "哪些经讲缘起"          # 融合检索
  python scripts/hybrid_search.py "appamāda" --bm25-only # 仅关键词，无需 faiss/模型
  ```
- `scripts/verify_citation.py`：引用核验（防幻觉护栏）：
  ```bash
  python scripts/verify_citation.py --file "义注/经藏义注/小部义注/法句义注_2026-06-21.txt" --quote "此身实不久，将卧于地上；被弃无意识，无用如碎木。"
  ```
- `scripts/health_check.py`：一键体检（语料/索引/对齐/依赖/内容库），发布前运行。
- `scripts/build_index.py`：本地重建语义索引（段落感知分块，可选 bge 嵌入 + FAISS）。
- `tests/test_skill.py`：自动化回归（纯标准库）：`python tests/test_skill.py`
- `data/corpus/`（运行时生成）：从数据集下载的原文 txt
- `data/index/`（运行时生成）：语义索引 `pali_index.faiss` + 映射 `chunks.jsonl.gz`（+ 派生缓存 `chunks.offsets` / `bm25.idx`）

> 内容规模（v1.5.7）：故事 91 / 教义 16 / 巴利 62 / 经典 20 / 禅修 5 / 人物 12 / 偈语 423，合计 **629 个内容条目**，全部逐句摘引自 CANON_DIR（即 data/corpus/）并标注出处。

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
3. 按 `SKILL.md` 第四节的模块模板写正文。**故事入库只需摘引原文，不必预写白话文——「白话文」在读取/输出时由助手现场生成**（见 `stories.md` 首部说明与 SKILL.md §五 故事模板）。
4. 在 `_sources.md` 登记出处。

## 入库前必做
- **出处抽查**：随机抽 10 篇，确认经号、部派归属、巴利拼写无误。
- 自查是否踩 `SKILL.md` 负面清单；教义陈述是否挂了出处。
- **白话翻译**：叙事可白话重述，但偈语与经文摘引块须整段保留译本原文；默认纯中文，用户显式要求外语时才暂停中文限制（见 §三·8 / §五·一）。

## 发布注意事项
- 发布到 SkillHub 时，**不要**把已下载的 `data/corpus/`、`data/index/`、`data/*.ready`、`data/_corpus_download.zip` 纳入包；这些由使用者首次使用时 `setup_corpus.py` 自动生成（技能根 `.gitignore` 已忽略 `data/`）。
- 技能包应保持轻量（仅 SKILL.md / README.md / references/ / scripts/ / tests/）。语义检索依赖 `sentence-transformers` + `faiss-cpu`，请在 README/发布说明中告知使用者按需 `pip install`。
- **发布前自检**：运行 `python scripts/health_check.py` 与 `python tests/test_skill.py`，两者通过再发布。

## 如何激活
放入 `~/.workbuddy/skills/qingtian-buddhism/` 后重启/刷新，对话中提到佛陀、佛法、禅修等触发词即可唤起；首次对话涉及经文检索前，确保已运行过 `setup_corpus.py` 拉取语料。

## 测试记录
- **R1（2026-08-11，skill-prod-test v1.5.1）**：首轮深度测试。基线 v1.5.0。
  - 发现并修复 6 项：D1 缺失 `.gitignore`（P1）→ 新增；D2 打卡日志写入技能包内致更新丢数据（P1）→ 改写 `data/practice-log.md`；D3 README 目录速览/规模描述仍为重构前目录结构（P2）→ 校正；D4 `_sources.md` 表格与出处示例使用旧单文件路径（P2）→ 校正；D5 "年内天数"未定义（P3）→ 显式定义；D6 `semantic_search.py` 的 `import faiss` 缺兜底（P3，仅作文档建议，未改脚本）。
  - 无新缺陷项：stories 91 篇无重复、dhammapada 423 偈、source 标记 100% 覆盖、CANON_DIR 与解压结构一致、数据源 URL 可达（302→CDN）、路由表全命中。
  - 未执行项：语料/语义索引 200MB 全量下载与端到端语义检索（仅做直链可达性 HEAD 验证）。
- **R2（2026-09-09，深度审查 + 完善，v1.5.3 → v1.5.4）**：
  - 修复缺陷 6 项：① 语义检索偏移错位（chunks 偏移为 LF 归一化字符偏移，语料为 CRLF；新增 `resolve_context`/`--context`，禁止自行切片）（P1）；② `import faiss` 无兜底（补上 R1 D6，友好降级提示）（P2）；③ `setup_corpus.py` 临时 zip 删除失败静默吞错 + 已就绪分支自动清理遗留 zip（P2）；④ README 版本/计数滞后 v1.5.1→v1.5.4、巴利 61→62、总条目 628→629（P2）；⑤ `index_ready()` 增加最小字节校验、下载中断清理半成品（P3/P4）；⑥ 下载失败残留临时文件清理（P4）。
  - 新增能力：`hybrid_search.py`（BM25+FAISS RRF 混合检索，参考 tripitaka-mcp）；`verify_citation.py`（引用核验防幻觉，参考 FoJin）；`health_check.py`（一键体检）；`build_index.py`（段落感知分块重建索引，参考 SuttaCentral segment 理念）；`tests/test_skill.py`（13 项自动化回归，纯标准库）。
  - 实测验证：`python tests/test_skill.py` 全通过；`health_check.py` 逐项通过；`verify_citation.py` 对故事引文实测通过；`hybrid_search.py --bm25-only` 实测可用。
  - 未执行项：端到端语义/混合检索（需装 faiss-cpu + sentence-transformers，Python 3.14 兼容性待验证，建议 3.10–3.12 虚拟环境实测）；`build_index.py` 全量嵌入重建（需模型，未在本次执行，仅 dry-run 分块验证）。
- **R3（2026-09-10，v1.5.4 → v1.5.5）**：
  - 完善：故事输出规范固化为「故事正文（译本摘引·原文）＋白话文」双段必配、并列呈现（用户需求：今日故事原文之外须配白话文）。白话文采用**运行时生成**策略——读取故事时由助手依据原文现场生成，不预写入库（用户明确：每次读取故事时现生成即可）。
  - 落地：SKILL.md §四 故事路由 / §五 故事模板 / §七 / §八 明确白话文为默认输出项、现场生成（遵循 §五·一 白话翻译规范）；`stories.md` 首部更新条目结构说明（原文四段入库）并附白话文示例；README 目录速览 / 新增步骤 / 版本同步。
  - 存量：无需批量补齐白话文（运行时生成）；故事条目保持原文入库。
  - 验证：`python tests/test_skill.py` 13/13 通过；`health_check.py` 错误 0。
- **R4（2026-09-19，内容核验 + 取材修正，v1.5.5 → v1.5.6）**：
  - 问题：45 个「本生」条目（date_index 47–91）入库时全部只从偈颂文件取材（`三藏经文/经藏/小部/本生-1、本生-2` 仅含 547 则偈颂、无散文叙事），序分/结分（说法背景、菩萨身份、弟子对应）系统性缺失；`#524 桑喀巴拉` 将施救者阿罗逻误判为「菩萨」。根因：对巴利文献「经文（偈颂）＋义注（散文叙事）」双层结构的取材偏差——完整叙事在 `义注/经藏义注/小部义注/本生义注-1~7`（语料内始终存在）。
  - 修复：45 条全部对照本生义注（序分+叙事+结分）逐条核验，**修正 12 条**（含 #524 整条重写：菩萨＝龙王桑喀巴拉/前世难敌王子，施救者阿罗逻＝前世舍利弗，补序分「祇陀林·优婆塞守布萨」，category 慈悲→持戒；另修正 #81/#151/#178/#179/#190/#220/#521/#523/#533/#534/#537 的菩萨身份，其中 #521 依结分（义注-5:484）确证菩萨为鹦鹉阎浮迦）；33 条核对无误。
  - 同步：`canon-index.md` 补登记「本生故事优先查本生义注-1~7」；`_sources.md` 来源登记更新；`SKILL.md` §四 故事路由与 §四·一 速查表更新；改动前已备份至 `data/backups/`（*.20260919.bak）。
  - 验证：`python tests/test_skill.py` 13/13 通过；`health_check.py` 18 项 0 错误（2 个可选依赖告警，与本次无关）。
  - 交付：`本生条目核验报告_20260919.md`（逐条证据行号 + 修正清单 + #524 重写说明）。
- **R5（2026-09-19，发布内容完善，v1.5.6 → v1.5.7）**：
  - 依据 skill-distributor 发布预检（33 维）建议完善：① SKILL.md description 重写——补功能动词（推荐/解读/讲解/引导/教学/检索等）、「青田·原始佛教修学」核心词与英文关键词（Early Buddhism / Theravada），提升各平台可发现性；② README 安装路径占位符规范化，消除 Windows 绝对路径；③ 发布包排除 `tests/reports/` 历史测试记录（本地保留）；④ dhammapada.md 单文件偏大建议接受（423 偈单文件为按日期定位的最优结构，SKILL.md 已注明 Grep 兜底）。
  - 验证：预检 8 项建议 → 消除 7 项（隐私 PII 0、可发现性建议 0），仅余 dhammapada 1 项接受。
  - 发布：GitHub（tag v1.5.7）+ ClawHub + 腾讯 SkillHub 同步完成（ClawHub/SkillHub 同版本号不可重发，故升 v1.5.7）。
