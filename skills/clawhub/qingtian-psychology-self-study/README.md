# 青田·心理自习室（咨询师实战训练台）· Skill 说明

> 面向**心理咨询师（含准咨询师）**的实战训练台：提高、完善、丰富自己的理论与对话实践本领。核心是**练对话**——17 流派 TPR 练习器三模式（体验：AI 当咨询师 / 实操：AI 当来访者、你当咨询师施技 / 督导：贴逐字稿、AI 当督导师五维分析）。**即用即走**：新用户一键默认开跑、一句话可定制，日常只推荐「下一件事」；按**阶段**（启蒙→流派→领域→整合→专项→精进）推进，阶段总结为完成门槛。配套理论补课、评估施测演练（21 量表）、个案概念化、伦理两难决策、认知/反移情记录、情绪打卡、经验等级与进度追踪（能力五维）。

## 它能做什么
- **即用即走**：新用户无需问答直接开始（默认：单人·零基础·咨询方向·~10h/周）；说一句「我有一年咨询经验，主攻 CBT」即可定制；配置随时可改。
- **日常单推荐**：系统按阶段/进度/画像只推荐一件事（练对话/理论补课/评估演练/记录/总结），说一个词就开跑；「有什么可做」才展开选项。
- **阶段制进度**：六阶段路径（`curriculum/roadmap.json`），每个阶段有任务清单（输入/输出/练习/伦理）；**阶段总结是阶段完成的唯一标志**（对抗「自我感动式学习」）。
- **能力五维成长**：对话技术 / 个案概念化 / 理论功底 / 评估能力 / 伦理与自我；练习、分析与补课均沉淀进五维，进度页按五维展示。
- **伦理与安全**：不诊断、不开药、危机立即给资源（热线与情绪急救包单源 `resources/crisis-resources.md`）。
- **进度追踪**：读写 `progress.json`；经验/等级/里程碑与进度导出/导入备份。
- **集成子技能**：TPR 心理咨询练习器（17 流派 · 三模式：体验/实操/督导，含来访者画像库）、心理量表测评系统（21 量表，含 PHQ-2/GAD-2 快速筛查）。

## 目录结构
```
qingtian-psychology-self-study/
├── SKILL.md              # 主入口（运行时中枢：角色/流程/处理器/安全，v2.1.0 咨询师训练台）
├── README.md
├── curriculum/           # onboarding话术（一键默认）、roadmap.json（六阶段+前置检查+阶段任务）、milestones
├── modules/              # 11 个内容库（7 进度模块 + ethics + dialogue-analysis + thought-diary + exposure）
├── resources/            # book-list.json、film-guide、case-library、prompts、crisis-resources.md（危机单源）
├── tools/                # flashcard-gen.py、progress-backup.py（导出/导入）、migrate-v2.py（周制→阶段制迁移）、progress-tracker、templates
├── schemas/              # progress-schema.json（v2：currentStage/stageCompleted/stageSummary）
├── manifest/             # manifest.json（分发元数据，v2.0.0）+ 说明
├── tests/                # integration_test.py、run_all.py（一键全量）、dryrun/、reports/
├── practice/             # 内嵌 TPR 心理咨询练习器（v1.0.3 整份内嵌）
│   ├── RUNBOOK.md        #   练习引擎运行手册（三模式调度：体验/实操/督导；危机/HTML报告）
│   ├── client-profiles.md  #   来访者画像库（实操模式：4 类困扰 × 4 类人格 × 3 档强度）
│   └── references/       #   41 个文件：therapies(17)、counselors(17)、ethics、onboarding、practice、risk-assessment、safety-boundaries、dialogue-examples、report-template
└── assessment/           # 内嵌 心理量表测评系统
    ├── RUNBOOK.md        #   测评引擎运行手册（21量表/快速筛查/出题/计分/报告；v2 默认推 1 个量表）
    ├── scales/           #   21 个标准量表 JSON（PHQ-2/GAD-2/PHQ-9/GAD-7/SCL-90…，ASRS 官方计数计分）
    ├── scripts/          #   scoring_engine.py（sum/average/count）、report_generator.py、score_and_report.py（集成封装）
    └── references/       #   safety_protocol.md、scale_authority.md
```

> **v2.1 变更说明**：定位升级为**咨询师实战训练台**（服务心理咨询师提高/完善/丰富理论与实践本领）。① 对话练习重构为**三模式**：体验（AI 当咨询师）/ 实操（AI 当来访者，新增 `client-profiles.md` 来访者画像库）/ 督导（逐字稿五步分析 + 五维透镜）；② 学习主线改为**练→析→督→学**闭环，理论补课服务练习缺口；③ assess 重定位为评估施测演练，thought-diary 兼做反移情记录，ethics 重定位为伦理两难决策；④ 默认配置 goal=counselor。v2.0 成果保留：阶段制（无「第几周」）、一键开跑、单推荐、处理器 8+5、状态机 5+1、组队已删。旧进度文件用 `python tools/migrate-v2.py <progress.json>` 迁移。

## 使用
1. 对 WorkBuddy 说「练咨询 / 学心理学」即触发；新用户**无需问答**直接开始，或一句话定制。
2. 说「今天练什么」进入日常单推荐；说「练」「实操」「督导」「测」「补课」「总结」「打卡」直接开跑对应动作。
3. 想换配置、备份进度等，按需说（隐藏能力）。
4. 每阶段结束务必「总结」写阶段总结——这是阶段完成的唯一标准。

## 测试
```bash
# 一键全量回归（计分引擎用例 + 集成测试 + 干跑脚本）
python tests/run_all.py
```

## 安全声明
本工具为**对话练习工具**，AI 扮演的来访者与督导师均为教学模拟，不替代真实咨询师、真实督导、精神科诊疗或危机干预。AI 不具备诊断与处方权。涉及严重困扰请寻求专业帮助（热线与情绪急救包见 `resources/crisis-resources.md`：全国统一心理援助热线 12356 / 青少年 12355 / 妇女儿童 12338，紧急情况拨打 120/110）。练习与测评两条链路各自保留最高优先级的危机护栏。

## 已知边界
- 进度仪表盘的可视化由独立 HTML（学习进度汇总.html）承担，Skill 负责数据。
- 实时提醒可用 WorkBuddy 自动化触发本 Skill。
- 内嵌量表计分依赖本地 Python 运行 `score_and_report.py`；若环境无 Python，回退 LLM 依 scale JSON 直接计分。
- 渐进暴露为教学演示工具，不适用于创伤/惊恐/自伤风险人群，详见 `modules/exposure.md` 安全边界。
