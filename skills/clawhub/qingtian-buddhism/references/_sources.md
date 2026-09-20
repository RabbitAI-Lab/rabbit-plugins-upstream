# 内容来源与版权记录（_sources.md）

本 skill 的全部内容**唯一来源**为 ModelScope 公开数据集 `Wangzhenren/pali2026-06-21txt` 中的《巴利三藏巴利-中文对照译本（2026-06-21）》。

## 一、数据源
- 数据集：`Wangzhenren/pali2026-06-21txt`（ModelScope）
  - 数据集页：`https://modelscope.cn/datasets/Wangzhenren/pali2026-06-21txt`
  - 语料 zip 下载直链（公开、无需登录）：`https://modelscope.cn/datasets/Wangzhenren/pali2026-06-21txt/resolve/master/%E5%B7%B4%E5%88%A9%E4%B8%89%E8%97%8F%E5%B7%B4%E5%88%A9-%E4%B8%AD%E6%96%87%E5%AF%B9%E7%85%A7%E8%AF%91%E6%9C%AC%EF%BC%882026-06-21%EF%BC%89%20txt.zip`
- 版本：5.1（2026-06-21）
- 版权：© 2025–2026 Sunanda | OpenTipitaka，文件头声明「本书可自由分享」。
- 性质：巴利语—中文对照；译文由 AI 生成并经人工校对，仅供学习参考。
- 体量：217 个 txt（三藏经文 / 义注 / 复注 / 藏外典籍），约 200MB。
- 完整文件清单：`references/canon-index.md`（相对路径，指向 `data/corpus/`）。
- **获取方式**：本技能不捆绑语料。首次使用时运行 `python scripts/setup_corpus.py`，脚本自动下载上述 zip 并解压到 `data/corpus/`（无需登录/密钥）。`data/corpus/` 与 `data/corpus.ready` 为运行时生成，发布包不应包含。
- **语义检索索引（同源数据集）**：同数据集另提供语义检索所需的 `pali_index.faiss`（FAISS 标量量化索引，101,170×768，内积+已 L2 归一化=余弦）与 `chunks.jsonl.gz`（映射表，字段 `{id, rel, start, end, text}`，id 即 FAISS 向量序号，rel 为原文 txt 相对路径）。二者由 `setup_corpus.py` 一并下载到 `data/index/`；嵌入模型 `BAAI/bge-base-zh`（768 维，公开模型）由 `semantic_search.py` 首次调用时自动拉取。语义检索为 Grep 关键词检索的**补充增强**，非必需依赖。

## 二、使用原则（务必遵守）
1. 所有经文、故事、教义、偈语**必须从 CANON_DIR（data/corpus/）摘取**，不得凭记忆或引用其他译本。
2. 巴利与中文须逐句对应摘引，不擅自改写译文。
3. 每篇内容文件头部 YAML 的 `source` 字段写明：文件名（可省略长前缀）+ 经号/品名。
4. 本 skill 不对外分发该译本原文，仅做学习用途的内部摘引与讲解。

## 三、各模块内容登记（均逐句摘引并标注出处）
| 模块 | 目录 | 篇数 | 主要摘引来源 |
|------|------|------|--------------|
| 每日一故事 | references/stories.md | 91 | 法句义注（45）、本生义注-1~7（45 个本生故事，序分+叙事+结分；本生-1/本生-2 仅偈颂）、示范（1），按 `(date_index: N)` 定位 |
| 核心教义库 | references/teachings/ | 16 | 相应部（蕴品/大品）、中部、长部、增支部 |
| 巴利小课堂 | references/pali/ | 62 | 相应部/中部/长部/增支部/小部（法句/自说） |
| 禅修引导 | references/meditation/ | 5 | 中部 MN 118、小部（小诵·慈经/Khp 9）、身至念等 |
| 佛陀与圣弟子 | references/figures/ | 12 | 相应部（有偈品）、长部 DN 16、法句义注、义注 |
| 经典阅读 | references/suttas/ | 20 | 中部/长部/相应部/增支部/小部（小诵·经集） |
| 每日偈语 | references/dhammapada.md | 423 | 小部/法句（Dhp 1.1–26.41），按 `<!-- dhp:N -->` 定位 |

> 出处示例（真实可核验）：
> - `stories.md`（`date_index: 37`，Tambadāṭhikacoraghātakavatthu，愚人品第1事，约 4684–4723 行；法句 100）→ 法句义注_2026-06-21.txt
> - `teachings/anatta.md` → 相应部/蕴品_2026-06-21.txt（# 3. Anattasuttaṃ，SN 22.59）
> - `pali/kamma.md` → 增支部/六集_2026-06-21.txt（AN 6.63，Cetanāhaṃ...kammaṃ vadāmi）
> - `suttas/metta.md` → 小部/小诵_2026-06-21.txt（Khp 9 慈经，约 519–584 行）
> - `dhammapada.md`（`<!-- dhp:1 -->`，Dhp 1.1）→ 小部/法句_2026-06-21.txt
