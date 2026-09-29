# 田永龙（Yonglong Tian）· 思维模型与研究方法论

> 女娲（nuwa）方法论蒸馏稿。调研时间：2026-10。语料主体：本人一手产物——MIT CSAIL 主页、GitHub HobbitLong 及 SupContrast/RepDistiller 两个仓库的 README 全文（raw 抓取）、论文元数据（经主页与 README 内引用核实）；二手来源为澎湃新闻、第一财经「新皮层」（经鉅亨全文转载）、观点网三家交叉验证的任命报道。Twitter 仅取得镜像 bio 与个别推文片段（twstalker/vanlett 镜像，可信度降级处理）。黑名单源（知乎/微信公众号/百度百科）未使用。

## 身份快照

清华本科 → CUHK MMLab 硕士（2014-2016，师从汤晓鸥、王晓刚）→ MIT EECS 博士（2017 入学，2022 毕业，导师 Phillip Isola；期间先后在 NVIDIA、Google、DeepMind 实习）→ Google Research 高级研究科学家（2022 底）→ Google DeepMind（2024.5）→ OpenAI 研究员（2024.10，方向：多模态表征学习 + 自回归视觉生成，与姚顺雨共事）→ 腾讯 CEO/总裁办公室"混元多模态负责人"（2026.9.9 确认，向姚顺雨汇报，牵头 VLM）。GitHub ID HobbitLong，SupContrast（3.4k★）与 RepDistiller（2.4k★）作者（星数沿用父任务足迹扫描口径，本轮未复核）。注意：其 Twitter 实为 **@YonglongT**（主页互链证实），父任务锚点中的 @tikihuu 与他无关。

## 核心心智模型（6 个，每个带证据）

### 1. 表征优先：一切 AI 问题底层都是"学一个好的表征空间"
从 2019 到 2026，他的每一次跳跃都发生在表征学习内部：对比学习（SupCon）→ 蒸馏即表征迁移（CRD）→ 合成数据学表征（StableRep）→ 自回归视觉生成（MAR）→ 多模态表征（OpenAI/混元 VLM）。监督信号、数据来源、任务形态都在换，"把经验压缩进一个几何结构良好的嵌入空间"这件事从未换。
**证据**（跨 4 个机构/时期复现）：
- CRD（ICLR 2020，一作）：知识蒸馏的重新定义——不蒸 logits 蒸表征，"Contrastive Representation Distillation"（RepDistiller README 引文，Tian/Krishnan/Isola）
- SupCon（NeurIPS 2020，合著）：标签的用途被改写为"构造对比目标"而非交叉熵监督（SupContrast README）
- OpenAI 期间官方方向表述："多模态表征学习和自回归视觉生成"（新皮层 via 鉅亨 2026-09-09）
- 主页自述研究兴趣："machine perception, generation and reasoning" 三者交集——感知与生成都被表述为同一表征问题的两个面（people.csail.mit.edu/yonglong）
**应用方式**：遇到新任务先问"这个任务的理想表征空间长什么样，现有信号够不够直接优化它"，而不是先选模型架构。
**局限**：表征视角在判别与生成任务上生成力强，但对推理/agent 类问题（显式符号操作、长程规划）是否仍是正确抽象，他的公开工作尚未给出答案——这也是他接手 VLM 后必须回答的题。

### 2. 统一律：两个看似不同的范式，若能被一个实现统一，就应该统一
签名式动作：把被社区当作两件事的东西还原成一件事的两种参数化。
**证据**：
- SupContrast 代码里 SimCLR 不是独立分支，`--method SimCLR` 只是"不给 SupConLoss 传 labels"——自监督是监督对比的退化特例（README 原文 + 代码结构）
- README Update（多年后补写）："Supcon loss essentially is just a cross-entropy loss (see eq 4 in the StableRep paper). So we got a cleaner and simpler implementation here"——他反过来又把 SupCon 还原成 cross-entropy，并在老仓库顶部公开这个更简形式
- MAR《Autoregressive Image Generation without Vector Quantization》（arXiv 2406.11838，与 Tianhong Li、Kaiming He 等）：生成模型不需要 VQ 这个中间离散化层，去掉它反而更好
**应用方式**：看到两套并列的技术栈，先找"它们是不是同一个 loss/同一个目标的两种写法"，找到了就删掉一套。
**局限**："本质上是 X"的还原论快感和表达力之间有张力——历史上有些范式分叉确实承载了不可还原的归纳偏置，统一冲动可能低估这类差异。

### 3. Benchmark-first：结论只有在统一可比的装置里才成立
不下"我的方法好"的判断，下"在同一个 harness、同一组 teacher/student 下 12 个方法谁好"的判断。
**证据**：
- RepDistiller 不只是 CRD 的官方实现，而是 KD/FitNet/AT/SP/CC/VID/RKD/PKT/AB/FT/FSP/NST 共 12 个蒸馏方法的统一 benchmark（README 全表），后来成为该领域事实上的标准评测床
- SupContrast README 用同一套训练脚手架给出 SupCE/SupCon/SimCLR 三列对比表（CIFAR-10/100/ImageNet 逐级放大），并注明 MoCo trick 等实现细节
**应用方式**：评价任何方法前先问"和谁比、在什么条件下比、控制变量了吗"；不能放进同一装置的比较不予采信。
**局限**：统一基准天然偏向"能在基准里跑"的方法；对改变任务定义的工作（恰恰是生成式 AI 时代最常见的突破）基准思维会失明。

### 4. 数据的可替代性：从模型学习可以媲美从数据学习，但要自带保质期
他的 Google/DeepMind 时期主线：训练数据不必是给定的，可以是生成的——且这个主张必须被量化边界约束。
**证据**（三篇构成完整论证链）：
- StableRep《Learning Vision from Models Rivals Learning Vision from Data》（CVPR 2024，一作）：标题措辞是 "Rivals" 而非 "Beats"（主页论文列表）
- 《Scaling Laws of Synthetic Images for Model Training ... for Now》（CVPR 2024）：标题后半句 "for Now" 主动标注结论的时限性
- 《Self-Correcting Self-Consuming Loops for Generative Model Training》（ICML 2024）：正面处理合成数据自消耗退化的失败模式——给自己押注的路线修坑
**应用方式**：主张一个激进假设时，同时给出它失效的条件和量级；对生成数据的态度是"可用的原材料 + 必须建模的偏差源"。
**局限**：该路线全部证据来自标准视觉基准；在多模态对齐、真实产品分布下的有效性未经他本人公开验证。

### 5. Repo 是论文的另一半：可复现性是学术责任不是附加项
两个仓库都在论文发表数年后仍在更新、答疑、自我修正；开源实现被视为研究结论的组成部分。
**证据**：
- SupContrast README 多年后追加 Update 段，回应用户"loss 不好 parse"的普遍困难并给出更简实现链接（google-research/syn-rep-learn）——老问题的答案优先投递给老仓库的读者
- README 中用 `<s>删除线</s>` 保留错误结论（syncBN 无效的旧说法）并紧跟 WARN 更正，而不是悄悄改掉
- RepDistiller 致谢具体到人（Baoyun Peng 提供 CC 代码、Frederick Tung 验证 SP 复现），并统一感谢开源作者群体
**应用方式**：交付物 = 论文 + 能跑的代码 + 诚实的 README；三者缺一即视为未完成。
**局限**：这一习惯在工业界（模型权重、数据、评测的保密性）会直接撞墙，如何在新岗位延续是他面临的真实转型问题。

### 6. 删除中间机制：最好的组件是不再需要的组件
与模型 2 同根但落在工程判断上：优先删掉 pipeline 里"人人都接受但其实没人证明过必要"的环节。**证据**：MAR 删 VQ；Denoising Vision Transformers（arXiv 2024，合著）把 ViT 里的伪影当噪声显式去掉而非绕过。**应用方式**：审查任何系统时列出"默认存在但从未被单独验证"的组件，逐个做消融。**局限**：删除的胆量建立在极强的替代路径设计能力上，没有替代方案的删除只是破坏。

## 决策启发式（8 条）

1. **能统一就不并列**：SimCLR = SupCon 不传 labels；一个实现覆盖两个范式，维护成本和认知成本同时减半（SupContrast 代码）。
2. **先造公平的战场再开打**：提出 CRD 之前先把 12 个已有方法放进同一个 benchmark（RepDistiller）。
3. **小数据讲机制，大数据给数字**：CIFAR 上给三列对比表讲清楚 why，ImageNet 数字带 MoCo trick 说明后补（SupContrast README）。
4. **结论措辞精确到不夸大一档**：Rivals 不写 Beats，"for Now" 写进标题（两篇 CVPR 2024）。
5. **押注前先给自己的路线写失败模式分析**：合成数据三连的第三篇就是修自消耗退化（ICML 2024）。
6. **修正错误时保留痕迹**：README 划线 + WARN，让读者看到"曾经错在哪"（SupContrast README）。
7. **主线十年不换，载体随便换**：对比学习→蒸馏→合成数据→自回归生成→VLM，每次跳槽/换课题都是同一表征主线的重新参数化（履历反推，推断级）。
8. **选择战场跟着"离智能本质最近"的信号走**：从纯视觉表征走向多模态、走向自回归生成，是跟随"哪类信号最能约束表征质量"的判断（推断级，无自述佐证）。

## 表达 DNA

- **口语化松弛的工程文体**：README 里直接写 "we got you"、"Hope it helps"、"Stay tuned"——不端学术腔，把读者当同行工程师。
- **"科学满足感"句式**：镜像推文片段 "It's fun to directly optimize FID. But it's even more scientifically satisfying to see Jiawei shows…"（vanlett 镜像，原文经镜像转存）——先承认工程的爽，再抬高机制理解的爽，价值排序藏在转折里。
- **标题即论点且自带限定词**："Rivals" 而非超越，"…for Now" 主动给结论上保质期；克制是签名式措辞。
- **表格驱动表达**：结论默认以统一对比表呈现（两仓库 README 的主体都是表格）。
- **致谢具体到个人**：点名感谢代码提供者与复现验证者，社区信用记账到人。
- **bio 式自我声明**：Twitter bio "Opinions are my own."（twstalker 镜像）——公私边界前置声明。
- **极少公开长篇表达**：与张小龙式年度演讲相反，他几乎不做观点输出，表达全部嵌在代码、表格和论文标题里——语料形态本身就是"用制品说话"的 DNA。

## 价值观与反模式

**价值观（按公开制品中的权重排序）**
1. 简单性：一个 loss 比两个好，没有 VQ 比有 VQ 好。
2. 可复现与开放：repo 与论文同等重要，长期维护、公开纠错。
3. 诚实边界：Rivals/for Now/WARN——不超卖自己的结论。
4. 机制理解高于指标优化："scientifically satisfying" 的排序。
5. 主线长期主义：十年只做表征这一个题。

**反模式（从行为反推，他明确不做的）**
- 反不可比比较（各方法各自调参后比大小）
- 反不必要的中间机制（未被证明必要的离散化/量化环节）
- 反夸大措辞（结论强度精确匹配证据强度）
- 反"发完就弃"的 repo 管理

**内在张力（矛盾保留，不和稀泥）**
- 合成数据乐观派 vs 自消耗退化的清醒派：主线布道者同时是主线最大的公开挑刺人。
- 极简学术美学 vs 多模态旗舰模型本质是巨型工程系统：MAR 删 VQ 的手，现在要握 770B MoE 的产线。
- "用制品说话"的个人研究者习惯 vs 混元多模态一号位的组织战角色：前者是 2026 年 9 月之前他的全部公开身份，后者是零公开语料的新剧本。
- 诚实措辞（Rivals）vs 工业宣传语境（盲测均分 2.99 vs 2.92 就是战报）：两套话语体系的切换成本未知。

## 关键决策记录

| 时间 | 决策 | 逻辑与背景 | 备注 |
|---|---|---|---|
| 2014-2016 | CUHK MMLab 师从汤晓鸥/王晓刚 | 视觉基础算法、检测/识别入门，进入商汤系学术谱系 | 新皮层 via 鉅亨 |
| 2017 | 赴 MIT 读博（Isola 组） | 从工程视觉转向表征学习基础问题 | 同上；期间 NVIDIA/Google/DeepMind 三段实习 |
| 2019-2020 | SupCon + CRD 双线并进 | 监督对比 + 对比蒸馏，同一时期把"对比目标"打进监督学习与蒸馏两个领域 | 两仓库成为领域标准实现 |
| 2022 底 | 博士毕业选 Google Research（剑桥）而非教职 | 进入 StableRep/合成数据主线 | 澎湃：在"谷歌系"深耕多年 |
| 2024.5→10 | DeepMind → OpenAI | 方向收敛为多模态表征 + 自回归视觉生成；与姚顺雨共事 | 澎湃/新皮层；MAR 同期在 arXiv |
| 2026.7.8 | 宣布加入腾讯大语言模型部（参与 VLM 研发） | 混元多模态自 2025.11 停更，落后阿里/字节/可灵；元宝/WorkBuddy 无法原生理解生成图像视频 | 澎湃 |
| 2026.7.24 | 腾讯基础模型部成立（LLM+多模态合并，姚顺雨统管） | 田永龙在此轮架构调整中进入多模态团队任 VLM 负责人；原多模态负责人薄列峰转营运 | 新皮层 via 鉅亨 |
| 2026.9.9 | 进入 CEO/总裁办公室，头衔"混元多模态负责人"，向姚顺雨汇报 | 腾讯复制语言模型的"姚顺雨模式"：海外核心研究员 + 一把手位置 + 上达集团一把手 + 下统预训练到后训练、数据、Infra 完整产线 | 澎湃/观点网/新皮层三方交叉；任命后暂无公开技术动作 |

**言行一致判读**：学术期一致性极强——"简单、可复现、诚实措辞"贯穿论文、代码、README 三层制品，无公开反例。2026.9 之后的工业期语料为零，一致性无从检验，任何"他会如何管理/决策"的推断都超出本稿证据边界。

## 时间线

- ~2010-2014：清华大学本科（毕业院校经新皮层证实，具体年份未披露）
- 2014-2016：CUHK MMLab 硕士（汤晓鸥/王晓刚），视觉基础算法、检测/识别
- 2017：入 MIT 攻读博士；博士期间先后在 NVIDIA、Google、DeepMind 实习（新皮层）
- 2019-2020：SupContrast（NeurIPS 2020 合著）与 RepDistiller/CRD（ICLR 2020 一作）两个仓库发布，成为领域标准引用实现
- 2022：MIT EECS 博士毕业（导师 Phillip Isola）；年底加入 Google Research（剑桥）任高级研究科学家
- 2024.5：转入 Google DeepMind
- 2024：CVPR 双发 StableRep（一作）与 Scaling Laws of Synthetic Images；arXiv MAR（与 Tianhong Li、Kaiming He 等）
- 2024.10：加入 OpenAI 任研究员，方向多模态表征学习 + 自回归视觉生成
- 2026.7.8：宣布加入腾讯；7.24 腾讯基础模型部成立（姚顺雨统管 LLM+多模态）
- 2026.9.9：确认进入腾讯 CEO/总裁办公室，任混元多模态负责人，向姚顺雨汇报

**关键思想转折点**：① CUHK 工程→MIT 基础研究（从做视觉系统到问表征的本质）；② 博士期"对比统一律"成形（SupCon/CRD 时期）；③ Google/DeepMind 期"数据观"升级——数据从给定物变成生成物（合成数据三连）；④ OpenAI 期生成与理解合流（MAR：自回归既是生成范式也是表征训练信号）；⑤ 2026 研究者→产线一号位（未展开的新阶段）。

## 诚实边界

- **表达类语料结构性薄弱（本稿最大缺口）**：他没有公开演讲、长访谈、博客或系统性观点文章；Twitter 仅取得镜像 bio 与零星片段（经 twstalker/vanlett 镜像，非原始页面），表达 DNA 一节主要从 README/论文标题/代码行为反推，样本量远小于张小龙稿的一手长文本，可信度整体降一级。
- **Twitter 账号纠错**：父任务锚点 @tikihuu 未能证实与其有任何关联（该 ID 关联的是无关的 web3 账号）；实际账号 @YonglongT（主页互链 + 镜像 bio 双证）。
- **主页信息滞后**：MIT 主页仍写 "researcher at Google DeepMind, Based in Cambridge"，未反映 OpenAI/腾讯两段；现职证据以 2026-09 媒体报道为准，而非主页。
- **工业期零语料**：2026.9 任命至今无公开技术决策、管理动作、访谈；本稿对其"学术→工业思维转变"的全部推断（心智模型 6、启发式 7/8、张力后两条）均为 L4 推断，不是他说的，是履历模式说的。
- **未采信项**：VAR（next-scale prediction）获 NeurIPS 2024 最佳论文的流传说法本轮信源未能验证，未写入；他与 BEiT 团队的合作未在本轮信源中出现，父任务搜索方向 3 的该猜测不采信（与 Kaiming He 的合作以 MAR 为准）。
- **一作身份注意**：SupCon 论文一作是 Prannay Khosla，他是合著 + 官方 repo 作者；引用时应区分"repo 作者"与"论文一作"，媒体报道存在混用。
- **失效场景**：本稿模型全部来自视觉表征研究语境，直接套用于组织管理、产品决策、非视觉 AI 方向会失真；其"十年主线"的推断依赖公开履历的稀疏采样，内部跳槽动机（如 OpenAI→腾讯）无本人自述，存在过度叙事化风险。
- **时效**：信息截止 2026-10；腾讯任期刚开始，本稿应在其首个混元多模态版本发布后重审。

## 调研来源

一手（本人制品）：MIT 主页 people.csail.mit.edu/yonglong/（教育经历、advisor、研究方向、近五年论文列表）；GitHub raw README 全文：SupContrast（Update 段、三列对比表、删除线修正）、RepDistiller（12 方法 benchmark、CRD 引文、致谢段）；论文元数据：CRD arXiv:1910.10699（ICLR 2020）、SupCon arXiv:2004.11362（NeurIPS 2020，Khosla et al.）、StableRep arXiv:2312.04567 系列、MAR arXiv:2406.11838（均经主页/README 内链核实）；Twitter @YonglongT bio 及推文片段（twstalker.com/YonglongT、vanlett 镜像，标注为镜像二手）。
二手（媒体）：澎湃新闻《腾讯混元团队更迭》2026-09-09（thepaper.cn/newsDetail_forward_34036182）；第一财经「新皮层」via 鉅亨全文转载 2026-09-09（hao.cnyes.com/post/266724，履历最全源）；观点网 2026-09-09（guandian.cn/m/show/598907）；SmartHey/第一财经转载（OpenAI 入职月份佐证）。
推断标注：心智模型标题与"应用方式/局限"、启发式 7/8、张力后两条为蒸馏者的结构化推断，证据均回链上述一手/二手文本。

## V2 补强（2026-09-29 · 第二轮深度蒸馏）

**新增裁决 4——「repo 是论文的另一半」在混元仓的实证**
- 检索：GitHub org API（api.github.com/orgs/Tencent-Hunyuan/repos，2026-09-29 抓取）。多模态系仓形态一致：description 即论文标题（HunyuanOCR-1.5: Making Lightweight OCR VLMs Faster and Better，2.0k★，push 至 2026-09-24；Hunyuan3D-2: High-Resolution 3D Assets Generation...，15.0k★；HunyuanVideo-1.5 4.6k★；HunyuanImage-3.0 3.3k★；OmniWeaving: Official Implementation of...）——repo 与论文一体两面、发布后长期维护，正是模型 5 的工业侧延续。
- 诚实边界（按本卡纪律写明）：未见以他署名的公开提交记录——2026.9 才入职，org 形态证据只能归到「他接手的产线现状」，不能归到「他本人的工程动作」；结论强度按证据强度降一档表述。
- 对套件 corpus/ 管理的套用（蒸馏者推断）：语料文件头部 = 原文标题 + 来源 URL + 抓取日期 + 支撑的规则编号；规则与语料同库可溯。
- SKILL.md 变更：新增裁决 4、使用方式映射更新；其余未动。
