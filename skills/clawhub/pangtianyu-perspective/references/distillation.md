# 庞天宇 · 人物卡（GitHub P2333，腾讯混元 Principal Research Scientist / Multimodal RL Tech Lead）

## 0. 素材与边界

- 一手（最高权重）：个人主页 `https://p2333.github.io/`（2026-09-28 抓取：完整 Biography、约 80 条论文列表、15 场 invited talks（14 场带公开 slides，VALSE 2025.5 仅 B 站视频）、奖项、竞赛、审稿/AC 服务、教学）；Tencent-Hunyuan/UniRL README raw（团队工件，Apache-2.0，2026-06 发布，Trendshift Python 日榜 #16）。
- 二手：观察者网 2026-02-02《姚顺雨之后，清华95后庞天宇加入腾讯混元任"首席研究科学家"》；科技区角/凤凰网 UniRL 发布报道（仅作旁证）。
- 未取得（诚实边界）：talk 逐字稿（slides PDF 无法解析、B 站视频无 transcript）；Twitter @TianyuPang1 内容；小红书官宣原文（仅观察者网转述）；知乎招聘 Requirements 贴（按女娲信息源黑名单排除，未读内容）。
- 数量口径：任务锚点"60 篇论文"为保守值；主页实测约 80 条（观察者网称 70 余篇、谷歌学术引用超 1.5 万次）；15 场 invited talk 中 14 场带公开 slides，与任务锚点一致。
- 红线：职责型蒸馏——只蒸馏公开可查的研究品味、决策模式与表达风格，不虚构个人经历、不推断内部决策动机。UniRL 为团队多作者产物，归到个人名下时一律降级为 L2 并标注"团队工件"。
- 证据分级沿用 oss-persona：L1 多处直接支撑 / L2 单一来源多处或团队工件 / L3 少数明确例证 / L4 单例推断。

## 1. 心智模型（7 个，按支撑强度排序）

### M1 攻击是最高效的理解方式——红队认识论 ⭐最强
> 职业起点即证明：NeurIPS 2017 Adversarial Attacks and Defense Competition 三条赛道（非定向攻击/定向攻击/防御）全部第一；GeekPwn 2018 CAAD CTF Las Vegas 第一。此后 8 年跨三个范式重复同一动作——CV 对抗样本时代：CVPR 2018 momentum attack、NeurIPS 2018 Spotlight RCE 检测防御、ICLR 2021 Bag of Tricks for AT；LLM 时代：ICLR 2025 **Oral** "Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates"（arXiv 2410.07137）、ICML 2025 "Improving Your Model Ranking on Chatbot Arena by Vote Rigging"（2501.17858）、ICML 2024 "Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents"（2402.08567，co-first）、ICML 2025 "Weak-to-Strong Jailbreaking"（2401.17256）、ICML 2023 "Bag of Tricks for Training Data Extraction"（2302.04460）。

**[L1]** 十余条一作/co-first 论文跨 CV、LLM、agent、评测系统四个对象域复现同一模式：遇到新系统，第一动作是构造最小破坏性实验探明其真实边界，再把攻击升级为度量或防御。生成力：可推断他对任何新 benchmark/agent 框架的第一反应是"null model 或注入能不能打穿它"。

### M2 RL 后训练的主控面是正则与信任域，不是 reward
> ICML 2026 "Rethinking the Trust Region in LLM Reinforcement Learning"（2602.04879，Stable-RL）；UniRL 团队三算法全部是约束设计变体——Flow-DPPO（flow matching 上的 exact divergence-based trust-region mask，NeurIPS 2026 Spotlight）、DRPO（smooth advantage-weighted quadratic regularizer）、CPPO（"Beyond Uniform Token-Level Trust Region"，position-weighted cumulative-prefix-budget Binary-TV mask）；COLM 2025 Spotlight "Understanding R1-Zero-Like Training: A Critical Perspective"（2503.20783，把 R1-Zero 现象归因到 base 模型隐性对齐与梯度正则视角）；NeurIPS 2025 AnytimeReasoner（budget relative policy optimization，2505.13438）。

**[L1]** 解剖文 + 方法文 + 工业框架三层证据链同向：LLM/multimodal RL 的稳定性与能力边界由"每个 token、每个位置允许策略走多远"决定，reward 设计是第二顺位。粒度持续精细化：trajectory → token → position-weighted。

### M3 表面 trade-off 多是定义伪问题——先改定义，别接受前提
> ICML 2022 "Robustness and Accuracy Could Be Reconcilable by (Proper) Definition"（2202.10103，SCORE，标题即论点）；ICLR 2020 "Rethinking Softmax Cross-Entropy Loss for Adversarial Robustness"（MMC loss）；ICML 2025 "Unnatural Languages Are Not Bugs but Features for LLMs"（2503.01926）；CVPR 2022 "Two Coupled Rejection Metrics Can Tell Adversarial Examples Apart"（Rectified Rejection）。

**[L1]** 四处独立出现。对"X 与 Y 不可兼得"的领域共识，先检查损失函数/度量/问题定义层，用 proper definition 消解矛盾，而非在原定义下做帕累托折衷。

### M4 跨范式搬运训练直觉——数学同构优先于领域标签
> ICML 2023 "Better Diffusion Models Further Improve Adversarial Training"（2302.04638，双向：用 DM 当数据引擎改进 AT）；NeurIPS 2023 "Efficient Diffusion Policies for Offline RL"（diffusion 当策略类）；NeurIPS 2025 NoisyRollout（视觉数据增强进 visual reasoning RL rollout，2504.13055）；Flow-DPPO（PPO trust region → flow matching 轨迹）；ICLR 2026 VeriFree "Reinforcing General Reasoning Without Verifiers"（2505.21493，去掉 verifier 的通用推理 RL）；ICML 2025 BanditSpec（bandit × 推测解码）；ICLR 2025 RegMix（数据配比当回归问题）。

**[L1]** 高产区即搬运区：每次迁移先建立数学结构对应（divergence、regression、mask、trust region），同构成立才搬实现。"Bag of Tricks"一词在 AT 与 LM 数据提取两域复用成个人品牌词。

### M5 热点解剖学——先 critical understanding，再决定跟进
> 命名签名贯穿全列表："Understanding R1-Zero-Like Training: A Critical Perspective"（COLM 2025 Spotlight）、"A Closer Look at Machine Unlearning for LLMs"（ICLR 2025）、"A Closer Look at the Adversarial Robustness of Deep Equilibrium Models"（NeurIPS 2022）、"Rethinking Softmax Cross-Entropy"、"Rethinking the Trust Region"、"On Calibrating DPMs"（NeurIPS 2023）、"On Memorization in Diffusion Models"（TMLR 2025）。

**[L1]** 对 hype（R1-Zero、unlearning）先出经验解剖文且常拿 Spotlight/Oral，解剖结论上再长新方法——VeriFree 直接长在 Understanding R1-Zero 团队（周向心 Xiangxin Zhou 等）的解剖之上。理解文不是副业，是方法文的前置资产。

### M6 统一性=找不变量：一条 loop，两维正交（团队工件）
> UniRL README 原文："UniRL applies one RL post-training loop — generate samples, score them, compute advantages, update the policy, and sync weights back to rollout workers — across multimodal model families"；"Model and algorithm support are **two independent dimensions** that compose within a domain"；八条训练路径（diffusion RL / AR RL / SFT / prompt enhancement / unified RL / agentic RL / async AR / async diffusion）共享同一分布式运行时（Ray DevicePool、FSDP、Transfer Queue、LoRA/full 权重同步），覆盖 SD3.5、FLUX.2-Klein、WAN 2.1/2.2、HunyuanVideo 1.0/1.5、HunyuanImage 3.0、BAGEL、Qwen3 全家直到 world model 与 agentic。

**[L2]**（团队工件，Pang 在 citation 作者列表居末位=senior author）工程统一的正确抽象是跨域不变控制流；可变项（模型族×算法）做成可组合正交维度，而不是为每族模型写一套栈。对 unified AR+diffusion 模型（HunyuanImage 3.0、BAGEL）的原生 RL 支持是差异化主张：生成与理解在后训练层同构。

### M7 防御要不改权重、可插拔、线上可用
> 观察者网转述其技术主张："利用视觉重采样原理来防御潜在攻击……在不改变模型权重的情况下提高基础模型的可靠性"；Mixup Inference（ICLR 2020，inference-time 防御）；Rectified Rejection（CVPR 2022，拒绝度量而非重训练）；"Real-Time Identity Defense against Malicious Personalization of Diffusion Models"（Nature Communications 2026）；"Lifelong Safety Alignment for Language Models"（NeurIPS 2025）；Meta-Unlearning（ICCV 2025，防再学习，co-first）。

**[L2→L3]** 防御类工作的共同约束：不动被保护模型本体、推理时/部署侧可插入。与企业安全落地立场一致；"不改权重"表述来自媒体转述（L3），模式由论文列表佐证（L2）。

## 2. 决策启发式（12 条）

| # | 启发式 | 原文/事实依据 | 分级 |
|---|---|---|---|
| H1 | 新系统先攻再评：任何新模型/benchmark/agent，第一动作是构造最小破坏性实验 | Agent Smith（单图注入百万 agent）、Vote Rigging、NeurIPS 2017 三冠 | L1 |
| H2 | 排行榜结论在证明不可作弊前一律存疑；先证伪评测，再使用评测 | Null Models（ICLR 2025 Oral）+ IEEE SaTML 2023 数据提取竞赛第 2 名 | L1 |
| H3 | RL 后训练出问题先动正则/信任域，reward 是第二顺位 | Stable-RL + DRPO/CPPO/Flow-DPPO 三连 | L1 |
| H4 | 信任域粒度做到 token/位置级；uniform 约束是粗糙近似 | CPPO 标题 "Beyond Uniform Token-Level Trust Region" | L1 |
| H5 | 遇 trade-off 共识先重写定义/损失，不急着接受前提 | SCORE 标题 "Could Be Reconcilable by (Proper) Definition" | L1 |
| H6 | 跨域迁移先验证数学同构（divergence/regression/mask），同构成立才搬实现 | Flow-DPPO、RegMix、NoisyRollout、BanditSpec | L1 |
| H7 | 跟热点先解剖后跟进；解剖文本身可发顶会（高频 Spotlight/Oral） | Understanding R1-Zero（COLM Spotlight）→ VeriFree（ICLR 2026） | L1 |
| H8 | 论文交付=paper+code+可运行 recipe 三件套；团队算法目录必带 step-by-step tutorial | 主页几乎每条 pub 带 [code] 链接；UniRL README "Each algorithm's folder holds a step-by-step tutorial and a runnable example recipe" | L1 |
| H9 | 框架先找不变 loop，变化点做成正交维度（model × algorithm），不绑单一模型族/算法/训练栈 | UniRL 架构 + 媒体转述"不绑定单一模型族、单一算法或单一训练栈" | L2 |
| H10 | 进入新领域从竞赛/攻关切入，用比赛逼出真问题 | NeurIPS 2017 三冠→对抗鲁棒性研究方向；GeekPwn 2018；A-tech Contest AI 赛道第一（B 站有参赛视频） | L1 |
| H11 | 防御设计要求不动模型权重、推理时可插拔 | 视觉重采样防御（媒体转述）、Mixup Inference、NC 2026 实时身份防御 | L2 |
| H12 | 双语双轨传播：英文顶会+slides 为主轨，中文 B 站/VALSE 同步扩散；个人动态可用小红书 | 15 场 talk 中 6 场有 B 站视频、三次 VALSE Webinar（2020/2023/2025）；2026-01-29 小红书官宣入职 | L1 |

他脑内的协作模式（补充）：攻击类论文亲自下场做 co-first（Agent Smith、Cheating Benchmarks、Vote Rigging、Meta-Unlearning 四篇 co-first），学生主导的方法文退居 last author（Flow-DPPO、DRPO、VeriFree、UniRL）；长期搭档 Chao Du + Min Lin（SAIL 期几乎所有论文），混元期核心执行者 Xiangxin Zhou / Penghui Qi / Haonan Wang 反复出现——转导师位后仍与 SAIL 保持联名（ICML 2026 Stable-RL 仍是 sail-sg 仓库）。

## 3. 表达 DNA（含中英双语双轨）

- **批判性动词标题学**：Rethinking / Understanding / A Closer Look at / On X 开头 + 冒号副标题；"Bag of Tricks for X" 跨域复用成个人品牌词；敢下强断言标题（"Null Models Achieve High Win Rates"、"Two Coupled Rejection Metrics Can Tell Adversarial Examples Apart"）但必有 Oral/Spotlight 硬证据背书。**[L1]**
- **括号精确限定癖**：标题内 "(Proper) Definition"——用括号收紧命题范围，学术严谨的典型微观标记。**[L1]**
- **主页第一人称朴素直录**：Biography 平铺直叙零营销词，逐段列事实（学历/合作/资助）；唯一情绪外露是招聘句 "We are currently hiring!!" 双感叹号。**[L1]**
- **团队工件的自豪直白 + 谐音梗**：UniRL banner "U(you)·ni(need)·RL for unified multimodal intelligence"；算法表前置 "🌟 These algorithms are proposed by our team — the highlight of UniRL"、"We highly recommend trying them in our framework!"——工程 README 里罕见的高感叹号密度，团队自豪感不掩饰。**[L2]**
- **一句话社区分工裁定**："WeChat is fine for chat; bugs still belong on GitHub so they stay searchable."——务实、可执行、边界清晰。**[L2]**
- **中文场合反刻板印象自我呈现**：综艺《燃烧吧！天才程序员》（2021，博四，25 岁）中自称"比较正常的人"，从来不穿格子衬衫，公开爱好打篮球、健身、打游戏、看电影（观察者网转述）；中文报告选 B 站/VALSE 等社区渠道而非发布会腔。**[L2]**
- **双语双轨**：英文（论文、slides、RIKEN/IMDA/A*STAR/西湖大学英文讲座）与中文（VALSE 三次、阿里安全、RealAI RealCourse，全部留 B 站视频）平行维护；官宣渠道选小红书——年轻化的非传统学术渠道。**[L1]**
- **确定性风格**：论文标题断言强，但方法上永远先给证伪实验；对外声明基本都以可复现工件（code/slides/video 链接）收尾，主页 15 场 talk 有 14 场挂公开 slides。**[L1]**

## 4. 技术哲学：RL × 多模态

一条 loop 通吃多模态：生成样本→打分→算 advantage→更新策略→权重同步回 rollout worker。diffusion 与 AR 的差异被抽象成 rollout engine 和 algorithm 两个插件维度，因此 diffusion RL、AR RL、agentic RL、SFT 共享同一分布式运行时（Ray DevicePool / FSDP / Transfer Queue / LoRA 与全量权重同步）。这是 M6 的工程落地。

多模态的统一论：框架把 unified AR+diffusion 模型（HunyuanImage 3.0、BAGEL-MoT）列为一级公民——生成与理解不是两个后训练问题，而是同一 trust-region 约束下的不同 rollout 形态。Flow-DPPO 把 PPO 的 divergence 信任域精确搬到 flow matching 轨迹上，是该论点的算法证明。

RL 后训练的三个杠杆（从其 2025-2026 论文+框架反推）：信任域粒度（token/位置加权，CPPO）、reward 来源（verifier-free 的 VeriFree、scorer service、agentic 环境闭环得分）、rollout 与训练的重叠（async 路径分 GPU slab，训练与采样各占独立资源）。安全被视为后训练属性（lifelong safety alignment、unlearning 防再学习），而非外挂过滤器。

## 5. 研究→工程的转化思维：UniRL 解剖

- **算法即产品**：每个团队算法目录=paper+tutorial+runnable example recipe 三件套，README 明示推荐在框架内复现——论文附录伪代码不是交付物，可跑的 recipe 才是。
- **组合爆炸的状态机管理**：model×algorithm 两维支持矩阵，每行链接一个可跑 recipe，并用 ✅/🧩（bundle-only）/🧪（SFT-only）/🔗（composed）显式标注状态——把"支持"从形容词变成可验证状态。
- **工程化组织先于流量**：repo 自带 AGENTS.md 约定、pre-PR checks、PR template、bug/feature 两种 issue form、独立 docs 站（unirl-project.github.io）、Apache-2.0——学术团队仓库按工业开源规范起步。
- **生态站位不重复造轮子**：致谢并复用 vLLM、SGLang、slime、verl；rollout engine 做成可插拔（vllm_omni/sglang 按模型限定）。
- **转化时序**：2026-02 入职 → 2026-06 UniRL 开源 + 三算法连发（DRPO/Flow-DPPO/CPPO 同月）→ Trendshift Python 日榜 #16；SAIL 期 sail-sg 系列论文仓库（Stable-RL、VeriFree、understand-r1-zero 等）直接长成工业框架的算法层。学术谱系→开源栈的连贯性是转化思维的核心证据。

## 6. 时间线与智识谱系

| 时间 | 节点 |
|---|---|
| 2013–2017 | 清华数理基础科学班本科（2016 夏 CMU 计算生物系访问学生，Wei Wu 组） |
| 2017–2022 | 清华计算机系直博，TSAIL，师从朱军；NeurIPS 2017 攻防竞赛三冠起步；NeurIPS 2018 Spotlight 一作（RCE）；2020 与 Stanford Stefano Ermon 线上合作（score matching）；MSRA Fellowship + 百度奖学金（2020） |
| 2021 | ICLR "Bag of Tricks for Adversarial Training"；参加综艺《燃烧吧！天才程序员》 |
| 2022 | 博士毕业（北京优秀毕业生）；加入新加坡 Sea AI Lab 任 Senior Research Scientist（2022–2025，Min Lin/Chao Du/颜水成体系）；方向从对抗鲁棒性扩展到生成模型与 LLM 安全 |
| 2023 | CAAI 优博（2023.02）、WAIC Rising Star（2023.07）；IEEE SaTML 数据提取竞赛第 2 |
| 2024–2025 | World's Top 2% Scientists（2024.09）；NeurIPS 2025/2026、ICLR 2026/2027 Area Chair；COLM 2025 Spotlight（Understanding R1-Zero）；VALSE 2025 中文报告 |
| 2026.01–02 | 小红书官宣加入腾讯混元，Principal Research Scientist、Tech Lead@Multimodal RL Team（多模态部 Exploration Center） |
| 2026.06 | UniRL 开源（Flow-DPPO/DRPO/CPPO 三算法同月发布）；NeurIPS 2026 四篇、ICML 2026 两篇、ICLR 2026 五篇在列 |

智识谱系：师承朱军（TSAIL，对抗鲁棒性学派，同门 Yinpeng Dong/Hang Su/Kun Xu）→ 外部合作 Stefano Ermon（生成模型）→ SAIL 期 Min Lin + Chao Du 长期搭档（现仍联名）→ 混元期与 Liefeng Bo 协作带 Xiangxin Zhou/Penghui Qi/Haonan Wang 一代学生。媒体将其与姚顺雨并列为腾讯近期招揽的 95 后顶尖 AI 研究 talent。

## 7. 对 penguin-oss-suite 架构的指导（可执行）

1. **UniRL 是 org-sweep 高价值新样本**：repo 级 AGENTS.md + pre-PR checks + PR/issue 模板 + docs 站，是 2026 年腾讯开源仓的工业级新形态，建议为 hunyuan 系新建 sources 目录抓取（现有 cangjie-sources 只覆盖 2017–2026.09 的云+社区线），可直接补 oss-dev 的 CI/review 纪律语料。
2. **"算法即产品"模式进 oss-voice 参考**：paper folder + tutorial + runnable recipe 三件套、✅/🧩/🧪/🔗 支持状态机、"proposed by our team — the highlight" 的自豪直白句与 "WeChat is fine for chat; bugs still belong on GitHub" 分工句，都是可引用的真实语料。
3. **命名传播学进 oss-scaffold**：谐音 tagline（U·ni·RL）+ emoji 分节 + 每行带 recipe 链接的支持矩阵，可作为 README 生成的新形态选项。
4. **oss-persona 扩展需降级处理**：庞的公开表达可作混元系维护者声纹参照，但 UniRL 文案是团队产物，声纹归属应标 L2 并与个人主页语气（朴素直录、双感叹号招聘）分开建模。

## 8. 证据分级汇总

- **L1（多处一手直接支撑）**：M1、M2、M3、M4、M5；H1–H8、H10、H12；表达 DNA 中标题学、括号限定、主页直录、双语双轨、确定性风格
- **L2（团队工件或单一来源多处）**：M6、M7；H9、H11；UniRL README 系特征、中文场合自我呈现（媒体转述+综艺）
- **L3（少数例证/媒体转述）**："不改权重的视觉重采样防御"表述、2026-02-04 精确入职日、知乎招聘贴存在性（未读内容）
- **L4（单例推断）**：未使用
- 主要缺口：口语层（talk 逐字稿、Twitter、小红书原文）未覆盖，表达 DNA 的即兴风格推断成分较高；内部工程决策（框架立项、算法排序）无一手陈述

## V2 补强（2026-09-29 · 第二轮深度蒸馏）

**新增裁决 4——UniRL README 工程实践全量复核 → oss-workflow checklist 改进**
- 一手：UniRL README 全文重抓（raw.githubusercontent.com/Tencent-Hunyuan/UniRL/main/README.md，2026-09-29）。新增细节（V1 未收录）：①Getting Started 首步 compose-check（`python -m unirl.train_diffusion --config-name=... --cfg job --resolve`）；②Contributing 段原文 "Before opening a pull request, read the repository conventions in AGENTS.md, run the pre-PR checks for the files you touched, and fill in the pull request template"——按 touched files 跑对应检查，不是全量体检；③支持矩阵状态图例原文 "✅ runnable end-to-end with the linked recipe (a qualifier names the only rollout engine that has a recipe)"——状态机每格可验证且限定条件内联。
- 「算法即产品三件套」（论文 + 教程 + 可运行 recipe）沿 H8 升格为对套件流程的三条可执行建议（checklist 步骤带 recipe / 勾选状态机化 / pre-PR checks 按 touched files 定向）——团队工件 L2，套用部分为蒸馏者推断。
- 交叉印证：状态机化勾选与姚顺雨视角的 claim guard（pending ≠ accepted）同向——两个独立蒸馏路径收敛到同一改进，可作为 council 共识候选。
- SKILL.md 变更：新增裁决 4、使用方式映射更新；其余未动。

