# example/design-blocks — 外部样本 · 设计切片案例集

> **定位**：成熟 skill 的**端到端设计切片**放这里——与 `example/fin-information-pipeline.md` 平级，但样本来自**外部已上线的 skill**。
> **这些切片干什么用**：`references/design-blocks-library.md` 里 126 条条目 D-NNN、`references/design-principles-library.md` 里的设计观 DP-NNN，每一条都不是拍脑袋写的——**这里是它们的证据原件**。想看"这条为什么成立"，顺着条目编号回来翻原文切片。
> **怎么产出新切片**：读被采样 skill 的 SKILL.md 与脚本 → 按 B01–B10 归位亮点 → 逐条写「落位 / 主题 / 触发 → 要点 / 理由 / 做法 / 证据 / 标签」→ 编号进库。判据见 [`references/design-blocks-library.md`](../../references/design-blocks-library.md) 顶部「条目格式」。

## 目录约定

```
example/design-blocks/<skill-name>/
├── README.md            # 这个 skill 好在哪里、采到哪些设计亮点、怎么读
├── 1-highlights.md      # 亮点清单（按 B01–B10 归位，条目格式见 design-blocks-library 顶部）
├── 2-source-skill.md    # 原 skill 关键切片（SKILL.md 全文或精华节选，附出处）
└── 3-into-library.md    # 已沉淀进 design-blocks-library / design-principles-library / lessons 的对应条目
```

## 怎么读（按目的选路径）

| 你想看 | 读哪个 | 学到什么 |
|--------|--------|---------|
| 这个 skill 整体好在哪 | `README.md` | 架构类型、设计模式、最值得抄的 3–5 个亮点 |
| 亮点怎么归纳成条目 | `1-highlights.md` | 亮点条目标准格式的实填版 |
| 原文证据 | `2-source-skill.md` | 亮点对应的真实原文/代码片段 |
| 沉淀到哪了 | `3-into-library.md` | 收录落库的对应关系 |

## 当前内容

> **编号说明**：下文出现的 `A-xxx` 是 3.11.0 之前的旧编号。两套旧编号已合并为统一的 `D-NNN`，反查见 [`design-blocks-library.md` 文末「旧编号映射表」](../../references/design-blocks-library.md#旧编号映射表迁移期反查)。

- [`cloudbase/`](cloudbase/README.md) — cloudbase-2.32.4 完整切片（产出 15 条亮点，对应 design-blocks-library A-011~A-103 多条）。
- [`memory-manager-v2-3.9.0/`](memory-manager-v2-3.9.0/README.md) — memory-manager-v2-3.9.0 切片（产出 10 条亮点 A-301~A-310 + 元设计层：成本感知/安全默认/证据自证 → design-principles-library DP-101~103）。
- [`skill-creator/`](skill-creator/README.md) — skill-creator（Anthropic 官方）切片（产出 4 条亮点）。
- [`tencent-docs/`](tencent-docs/README.md) — tencent-docs-1.0.41 完整切片（产出 15 条亮点 A-201~A-215）。
- [`ima-skills/`](ima-skills/README.md) — ima-skills-1.1.9 切片（产出 14 条亮点 A-401~A-414 + 元设计 DP-001~003；含 2-principles.md 元设计切片，v3.5.0 起本切片模式为范例）。
- [`westock-data/`](westock-data/README.md) — westock-data-1.0.7 切片（产出 12 条亮点 **A-501~A-512** + 元设计 **DP-201~203**：失败模式驱动设计 / 成本显性化 / 约束前置+完整性自检）。本片特殊性：**回照自己照出真 bug**（主路由 0 条可触线规则 → v3.6.0 补 4 条上限 + validate 第 12 项）。
- [`smart-charts-8.1.1/`](smart-charts-8.1.1/README.md) — smart-charts-8.1.1 切片（产出 12 条亮点 **A-513~A-524** + 元设计 **DP-204~206**：单一事实来源优先于同步纪律 / 可打断性由可逆性判定 / 安全与质量机制必须有对立面用例）。本片特殊性：**首个完整三产出样本**（亮点 + 蓝图 + 自省）；回照照出 **T10 版本双落点纪律只存在于 AI 记忆文件**（三层全缺）。
- [`tencent-news/`](tencent-news/README.md) — tencent-news（腾讯新闻）1.2.3 切片（产出 15 条亮点 **D-133~D-147** + 元设计 **DP-209~211**：权威源唯一化 / 失败即熔断不得向右兜底 / 验收先问执行者能力）。本片特殊性：**首个"刚安装的外部商城包"样本**——立标阶段即标"运行期不可验"；自省照出 **DP-208（源头拦截）是我们自己立的原则却没在自己流程里落地**（防线全在终点）。

## ⚠️ 已覆盖 · 不必重复收录清单（防重复入库）

> **用法**：收录新 skill 前先查此表。**命中就不必重复收录**（我们已有对等物且通常更强），把精力留给真空缺。

| 候选机制 | 不收理由 | 我们的对等物 |
|---|---|---|
| 能力边界矩阵（标的×维度） | 已有且更强 | `capability-boundary.md`：边界矩阵 + 4 问决策树 + 20 场景正反例 |
| 易混淆消歧（"像 A 其实不是 A"） | 已收 | A-401 三层路由表第②层（designer-guide / blueprint-template） |
| 失败给替代（fail-with-direction） | 已收 | A-409「不支持 + 应该用什么替代，把死路变指路牌」 |
| 双层错误分类（进程级 / 业务级） | 已收 | A-408 / A-410（错误码表必带"建议处理"列，写动作不写解释） |
| 二进制信任链 / SHA256 双层校验 | 技术栈不相关 | skill-designer 无二进制分发（只收其思想 → A-502 可验证性决定严格度） |
| 场景库 / 用例模板集 | 内容资产非机制 | `design-blocks-library.md` / `design-principles-library.md` 对等 |
| 错误码表 + suggestion 必带（smart-charts） | 已收 | A-410 错误码表带建议处理列 |
| 依赖声明带 reason 注释（smart-charts） | 已收 | A-414 运行时依赖声明带 reason |
| 默认策略不打扰用户（smart-charts） | 已收 | A-404 可逆性决定确认等级（**A-518 是其可判据化升级版**） |
| 沙箱三层校验 + 逃逸 PoC（smart-charts） | **场景不相关** | 元 skill 不执行不可信代码；**建议不补**（补了是过度设计） |
| 双平台脚本对 sh + ps1（tencent-news） | **场景不相关** | `sd_cli.py` 是跨平台 Python，无需双份包装器；**建议不补** |
| 状态脚本模式（tencent-news） | 已收 | D-075 状态脚本模式（探测+决策一次调用） |
| 输入指纹做缓存失效判据（tencent-news `requestedStarts`） | 已收 | D-080 用输入指纹做缓存失效判据 |

## 维护纪律

1. 每个样本 skill 一个子目录，`README.md` 必须写清"好在哪里"与"采到什么"，不写流水账。
2. 亮点条目**必须可溯源**（来源 + 证据片段），与 design-blocks-library 的条目一一对应。
3. 涉及隐私/路径/密钥必须匿名化（用户名 → 匿名，绝对路径 → `~/.workbuddy/...`）。
