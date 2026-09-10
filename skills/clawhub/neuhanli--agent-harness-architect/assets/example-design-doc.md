# 示例设计文档（教学范例 · 虚构项目）

> **这是什么**：一份**填满的**端到端架构设计示例，用来校准"写到多深算够"。项目（财务对账 agent）是**虚构**的，仅作教学——它**不是知识库案例**（知识库存放于 `references/`，须官方可核验；本文件在 `assets/`，是产出范例，不掺入防污染知识库）。
> **它刻意示范五件事**：① 范式选型"判据在先、案例在后"，并**主动拒绝**插件化/多智能体/分布式等"看着高级"的过度设计；② 关键取舍给**可比较的量化**；③ 六层落到**可直接编码**（真实 API、类型、配置）；④ **魔鬼代言人**反例；⑤ **范式偏见自检**。
> 配套模板见 `assets/design-doc.md`，判据见 `references/h-framework.md` §六/§七，红线见 `references/production-checklist.md`。

---

# 财务对账 Agent Harness 架构设计（示例）

## 1. 需求规格

| 维度 | 内容 | 状态 |
|---|---|---|
| 目标与用途 | 每日把银行流水（Excel/CSV）与 ERP 应收明细自动匹配，标出未匹配/金额不符/重复/低置信，产出对账报告；人只处理被标出的异常 | 已确认 |
| 成功标准 | 对"自动判定已匹配"的对：准确率 ≥ 99%、**误配率 ≤ 0.1%**；纯规则路径单批 5000 行 ≤ 3 分钟；每笔自动匹配**可追溯判定依据**；同配置复跑**幂等** | 已确认 |
| 任务结构 | 主干是**固定管线**（读取→规范化→匹配→标异常→报告）；少数"疑难行"（规则未命中）需**开放式推理**（模糊/多笔合并） | 已确认 |
| 数据/资源边界 | 读：银行流水文件 + ERP **只读**（查询或导出 CSV）。写：**只写**自己的结果库 + 报告目录；**绝不写** ERP/银行 | 已确认 |
| 硬约束 | 错配代价高（财务）→ 自动匹配必须可解释、可回滚；**数据不出内网**，原始流水**不得上传外部 LLM API**（合规） | 已确认 |
| 用户与场景 | 财务部 2–3 人；单机/内网服务器；每日批处理 + 按需复跑 | 已确认 |
| 边界（不做什么） | 不做自动过账/付款；不做多租户；不做实时流式；一期不做"一笔银行配多笔 ERP"的合并匹配 | 默认假设（可推翻） |
| 技术栈约束 | Python 3.11+；Excel 用 openpyxl/pandas；结果库用 SQLAlchemy + SQLite（可换 Postgres）；校验用 pydantic | 默认假设（可推翻） |

## 2. 架构范式 P（判据在先，案例在后；每项写"选定 + 被否端 + 否决理由"）

> 依据 `h-framework.md` §六逐项推导。本场景**刻意逆着案例库主流（插件化 + 中心化里的"插件化"那一端）**——下面的"否决理由"就是架构师克制力的体现。

| 子维度 | 选定 | 被否的对端 | 否决理由（含代价） |
|---|---|---|---|
| 扩展方式 | **嵌入式** + 轻量依赖注入（`BankReader`/`Matcher` 抽象接口） | 插件化（薄内核 + 运行时热插拔 + 可逆注册） | 银行格式有限且稳定、ERP 一种、**无第三方生态需求**；插件化的代价（内核生命周期、可逆注册、依赖装配）远超收益——对照 `pattern-dependency-injection` 的"何时不用"，以及 `mini-swe-agent`"能力≠复杂度"的克制立场 |
| 配置方式 | **声明式为主**（YAML 描述列映射/阈值/白名单）+ 命令式承载匹配算法 | 纯声明式（把匹配逻辑也塞进配置） | 财务要能自己改列映射且需可 diff/审计 → 映射与阈值用声明式；但**匹配算法不进配置**，否则会逼出"配置里的 DSL"，更难维护（`pattern-declarative-configuration` 的"何时不用"） |
| 部署拓扑 | **单机** | 分布式 | 5000 行/日、单批预算 ≤3min，单机绰绰有余；分布式 = 一致性/运维/可观测骤增，**规模不存在**（§10 给了单机预算测算） |
| 编排模式 | **中心化**（单管线协调者） | 去中心化/对等 | 任务能被一个协调者完全掌握，无需自治对等 agent；对等只会增加最终一致性与调试成本（`pattern-actor-model` 的"何时不用"）。注：去中心化在本库无 verified runtime 案例，但此处是"判否"，不受影响 |

## 3. 技术栈选型

| 项 | 选型 | 理由 |
|---|---|---|
| 语言 | Python 3.11+ | 生态成熟、财务数据处理常用 |
| Excel/CSV | `openpyxl`（.xlsx）+ `pandas.read_csv`（.csv） | 真实存在的库；openpyxl 用 `load_workbook(path, data_only=True)` 取计算值 |
| ORM/存储 | `SQLAlchemy 2.x` + SQLite（`sqlite:///data/recon.db`） | 单机足够；需要时换 Postgres 只改连接串 |
| 校验/模型 | `pydantic v2`（`BaseModel`） | 配置与领域对象的类型完整（满足"类型完整"门槛） |
| 疑难行 LLM（可选，默认关） | 内网/本地模型，经 `llm_advisor` 接口 | 合规：原始流水不出内网 → 禁用外部 API |
| 入口 | CLI：`python -m recon.cli run --config recon.yaml --batch-date 2026-09-09` | 可被 cron 调度 |

## 4. 六层设计（每层 = 决策 + 落地规格）

### 4.1 E 执行循环
- **设计决策**：主干**固定管线**（读取→规范化→规则匹配→标异常→报告），对规则未命中的"疑难行"走一个**有界子循环**：本地 LLM 提议候选 → 仍低于置信阈值则标 `needs_human`（**不自动判定**）。终止：管线处理完批次即止；疑难子循环**每行最多 1 次重试 + token 上限**，防跑飞。
- **落地规格**：`recon/pipeline.py::run_batch(cfg, batch_date)` 顺序调用 ingest→match→store→report；`recon/match/engine.py::reconcile(...)` 内对每行 try 规则、失败转 `llm_advisor`（可关）。失败处理：单行异常不炸整批，记入 `Exception` 表后继续。

### 4.2 T 工具注册
- **设计决策**：**固定小工具集，不做工具注册表/插件市场**（对照 `mini-swe-agent`：宁少而精）。工具：`read_bank_file` / `query_erp` / `match_rules` / `llm_suggest`(可选) / `write_result` / `gen_report`。**读写分离**：唯一写工具 `write_result` 必须过 L 层白名单校验。
- **落地规格**：工具就是普通 Python 函数（见 §6），由 `engine`/`pipeline` 直接调用，不经"LLM 动态选工具"。权限区分靠 L 层 hook，不靠 prompt 提示。

### 4.3 C 上下文管理
- **设计决策**：**批处理主体完全不占用模型上下文**（纯代码）。仅疑难行子循环用到上下文，且**每次只带"该行 + top-N(=5) 候选 + 规则命中情况"的结构化片段**，控制在 ~1.5–2k token/行；不带整批数据。
- **落地规格**：`llm_advisor.suggest(txn, candidates, rule_hits) -> Suggestion`，prompt 由该三要素拼装；无跨行上下文累积，天然无需压缩。

### 4.4 S 状态存储
- **设计决策**：SQLite + SQLAlchemy ORM 存 `Batch/Match/Exception/Audit`；每次运行一个 `batch_id`；**幂等**：`batch_id = f"{batch_date}::{config_hash}"`，复跑同 id 先删后写；每笔匹配的 `basis`（命中规则/LLM 建议 + 置信度）持久化 → 满足"可追溯"。**不上事件溯源**（无回放/时移需求，代价不值，见 `pattern-event-sourcing` 的"何时不用"），但保留 **append-only 的 `Audit` 表**做轻量留痕。
- **落地规格**：`recon/store/models.py` 定义 ORM；`recon/store/repo.py::write_batch(session, batch_id, results)` 做"删旧+插新"幂等写；并发：单写连接（批处理串行），无需连接池。

### 4.5 L 生命周期钩子
- **设计决策**：`write_result` 前置**白名单校验**——只允许写 `allowlist_write_dbs`/`report_dir`，写 ERP/银行或任意其它路径一律 `raise PermissionError`；日志对流水号/金额**脱敏**；金额超阈值却判"已对平"的记录标"复核"。
- **落地规格**：**用真实机制，不虚构 hook API**——在 `recon/guard/hooks.py::assert_writable_target(db_url, allowlist)` 中**解析为绝对路径并规范化后比对**（不只字符串前缀，防路径穿越），由 `repo.write_batch` 在开事务前调用；另可用 SQLAlchemy `event.listens_for(Session, "before_flush")` 兜底。

### 4.6 V 评估接口
- **设计决策**：**确定性校验，绝不让模型给自己判卷**（`production-checklist` 红线）。匹配结果由规则复核（金额相等？日期在窗口内？双方记录都存在？）；离线用**人工标注集**（≥500 笔）算准确率/误配率作 CI 回归门禁；置信度 < `min_confidence` 一律转 `needs_human`，**不计入"已匹配"**（从源头压误配）。
- **落地规格**：`recon/eval/verify.py::audit_matches(results) -> AuditReport`（纯函数复核）；`recon/eval/score.py` 跑标注集出 precision/误配率；引用/依据由**程序从匹配规则绑定**写入 `basis` 字段，不由生成方自由发挥。

## 5. 模块 / 目录结构（代码骨架）

```
recon/
├── cli.py            # 入口：run/verify 子命令，解析 --config/--batch-date
├── config.py         # pydantic 配置模型 + YAML 加载 + config_hash
├── pipeline.py       # E 层：固定管线协调（run_batch）
├── ingest/
│   ├── bank_reader.py# openpyxl/pandas 读多格式 → 规范化 BankTxn
│   └── erp_reader.py # ERP 只读（CSV/查询）→ ErpReceivable
├── match/
│   ├── rules.py      # 确定性匹配规则引擎（金额+日期窗+参考号）
│   ├── llm_advisor.py# 疑难行：本地 LLM 提议候选（可关，默认关）
│   └── engine.py     # 编排：规则优先 → 疑难转 llm → 仍不确定转 needs_human
├── store/
│   ├── models.py     # SQLAlchemy ORM：Batch/Match/Exception/Audit
│   └── repo.py       # 幂等写 batch_id、查询
├── guard/hooks.py    # L 层：写目标白名单校验（绝对路径）+ 脱敏
├── report/generator.py# 出对账报告（xlsx + md 摘要）
└── eval/
    ├── verify.py     # V 层：确定性复核（纯函数）
    └── score.py      # 标注集跑准确率/误配率（CI 门禁）
```

## 6. 关键接口签名（真实 API，类型完整）

```python
# config.py —— 配置模型（pydantic v2）
from pydantic import BaseModel
from typing import Literal

class ColumnMap(BaseModel):
    date: str; amount: str; ref: str; account: str

class BankProfile(BaseModel):
    name: str; file_glob: str; sheet: str | None = None
    header_row: int = 1; columns: ColumnMap

class ReconConfig(BaseModel):
    date_window_days: int = 3
    amount_tolerance: float = 0.01
    min_confidence: float = 0.9          # < 此值 → needs_human，不计入已匹配
    llm_enabled: bool = False            # 默认关（合规 + 成本）
    bank_profiles: list[BankProfile]
    erp_csv: str
    result_db: str                       # e.g. "sqlite:///data/recon.db"
    report_dir: str = "out/"
    allowlist_write_dbs: list[str]

def load_config(path: str) -> ReconConfig: ...
def config_hash(cfg: ReconConfig) -> str:  # sha256(cfg.model_dump_json())，用于幂等 batch_id
    ...

# ingest/bank_reader.py
from pathlib import Path
def read_bank_file(path: Path, profile: BankProfile) -> list["BankTxn"]:
    """openpyxl.load_workbook(path, data_only=True) 读 .xlsx；.csv 走 pandas.read_csv。
    按 profile.columns 做列映射与类型规范化。"""

# match/rules.py
def rule_match(txn: "BankTxn", candidates: list["ErpReceivable"], cfg: ReconConfig) -> "MatchResult":
    """确定性规则：金额相等(容差内) + 日期在窗口内 + ref/参考号命中。
    多候选同分 → 返回 needs_human（绝不自动二选一）。"""

# match/engine.py
def reconcile(bank: list["BankTxn"], erp: list["ErpReceivable"],
              cfg: ReconConfig, advisor: "LlmAdvisor | None") -> list["MatchResult"]:
    """逐行：先 rule_match；status==needs_human 且 advisor 可用 → advisor.suggest；
    仍 < min_confidence → 保持 needs_human。单行异常不炸整批。"""

# match/llm_advisor.py
class LlmAdvisor:
    def suggest(self, txn: "BankTxn", candidates: list["ErpReceivable"],
                rule_hits: list[str]) -> "Suggestion": ...   # 仅接本地/内网模型

# guard/hooks.py
def assert_writable_target(db_url: str, allowlist: list[str]) -> None:
    """解析为绝对、规范化路径后比对白名单；不在名单内 raise PermissionError。
    由 repo.write_batch 在开事务前调用（不只字符串前缀匹配，防路径穿越）。"""

# store/repo.py
from sqlalchemy.orm import Session
def write_batch(session: Session, batch_id: str, results: list["MatchResult"]) -> None:
    """幂等：先 DELETE 同 batch_id，再 bulk insert；事务内完成。"""

# pipeline.py
def run_batch(cfg: ReconConfig, batch_date: str) -> "BatchReport": ...
```

## 7. 核心数据结构

```python
from datetime import date
from decimal import Decimal
from typing import Literal

class BankTxn(BaseModel):
    txn_id: str; date: date; amount: Decimal
    ref: str | None; account: str; raw_row: int      # raw_row 支持回溯到原始文件行

class ErpReceivable(BaseModel):
    erp_id: str; due_date: date; amount: Decimal
    invoice_no: str | None; customer: str

class MatchResult(BaseModel):
    batch_id: str; txn_id: str
    status: Literal["matched", "amount_mismatch", "duplicate", "needs_human"]
    erp_id: str | None; confidence: float
    basis: str                                        # 可追溯：命中的规则说明 / LLM 建议摘要

class Exception(BaseModel):
    kind: Literal["unmatched", "amount_mismatch", "duplicate", "low_confidence"]
    txn_id: str; reason: str; suggested: list[str]

class BatchReport(BaseModel):
    batch_id: str; total: int; matched: int
    exceptions: int; needs_human: int; elapsed_sec: float
```

## 8. 配置文件格式（声明式 schema，逐字段注释）

```yaml
# recon.yaml —— 只描述"映射/阈值/白名单"，不含匹配算法（算法在代码里）
date_window_days: 3        # 匹配允许的日期差（天）
amount_tolerance: 0.01     # 金额容差（元）
min_confidence: 0.9        # 低于此置信度 → needs_human，不计入"已匹配"
llm_enabled: false         # 疑难行是否用本地 LLM；默认关（合规：原始流水不出内网）
erp_csv: "data/erp_receivable.csv"          # ERP 只读来源；生产可换只读查询
result_db: "sqlite:///data/recon.db"        # 结果库
report_dir: "out/"
allowlist_write_dbs:                        # L 层白名单：只允许写这些，其余 raise
  - "sqlite:///data/recon.db"
bank_profiles:
  - name: "ICBC"
    file_glob: "icbc_*.xlsx"
    header_row: 1
    columns: {date: "交易日期", amount: "金额", ref: "摘要", account: "账号"}
  - name: "CMB"
    file_glob: "cmb_*.csv"
    header_row: 0
    columns: {date: "trade_date", amount: "amt", ref: "memo", account: "acct"}
```

**加新银行 = 在 `bank_profiles` 增一项配置**，不改代码（这就是"嵌入式 + 轻量 DI"够用的证明：声明式覆盖映射，无需插件机制）。

## 9. 层间交叉检查

| 关系 | 说明 |
|---|---|
| E ↔ V | E 的"疑难子循环"终止由 V 定：置信 < `min_confidence` 不得自动判 `matched`，转 `needs_human` |
| S ↔ L | S 的 `write_batch` 被 L 的 `assert_writable_target` 拦截：非白名单库/路径 `raise`，杜绝误写 ERP |
| C ↔ E | C 只带"单行 + top-5 候选"，把 E 的 LLM 成本钉在 <2k token/疑难行，不随批量膨胀 |
| P ↔ T | 选了嵌入式 → T 用普通函数工具，不建 LLM 动态工具表（避免给固定管线配没人调用的注册表） |

## 10. 六层决策表（关键取舍给可比较的量化）

| 层 | 候选方案 | 优点 | 代价（量化） | 选定 | 依据·状态 |
|---|---|---|---|---|---|
| E/T | A 纯确定性规则 | 0 token、可复现、易审计 | 疑难行(估 5–15%)全转人工，人力↑ | — | — |
| E/T | B 规则 + 本地 LLM 兜底疑难行 | 人工量↓ | 整批仅 <10% 行走 LLM：5000×10%×~1.5k≈**<0.75M token/批**，本地模型故外部 API 成本≈0；但引入延迟不确定性（见 §12） | **B（`llm_enabled` 默认 false，可开）** | §10.1 延迟测算·默认假设 |
| S | A SQLite 表 + append-only 审计表 | 简单、够用、幂等易实现 | 无时移/fork 能力 | **A** | 无回放需求，事件溯源代价(存储↑/回放慢)不值 |
| S | B 事件溯源 | 可回放/审计强 | 存储只增、读需回放、schema 演化难 | — | `pattern-event-sourcing` 的"何时不用" |
| 部署 | A 单机 | 预算内、运维 0 | 无横向扩展 | **A** | 见 §10.1 |
| 部署 | B 分布式 | 可扩展 | 一致性/可观测/运维骤增 | — | 规模不存在 |

### 10.1 单批延迟预算（llm_enabled=false，纯规则路径，5000 行 × 假设 2 万条 ERP 应收）

| 环节 | 预算 | 说明 |
|---|---|---|
| 读取 + 规范化 | ~10–30s | IO + openpyxl 解析 |
| 匹配 | ~20–40s | 按"金额分桶"后近 O(n)（非 O(n·m) 全交叉） |
| 写库 + 报告 | ~10–20s | 事务内批量写 |
| **合计** | **≈ 40–90s** | **满足 ≤3min**（留 2× 余量） |

## 11. 参考架构图（文字版）

```
CLI/cron → pipeline.run_batch
             ├─ ingest: bank_reader(多格式→BankTxn) | erp_reader(只读→ErpReceivable)
             ├─ match.engine.reconcile
             │     ├─ rules.rule_match ──命中──▶ MatchResult(matched/...)
             │     └─ 未命中 & llm_enabled ─▶ llm_advisor.suggest ─仍<阈值─▶ needs_human
             ├─ guard.assert_writable_target（白名单，非名单则 raise）
             ├─ store.write_batch（幂等 batch_id=date::config_hash）
             ├─ eval.verify.audit_matches（确定性复核，程序绑定 basis）
             └─ report.generator（xlsx + md）
```

## 12. 遗留问题与未知区（诚实标注）

1. **"≤3min" 与 "开 LLM 兜底" 可能冲突**：若 `llm_enabled=true` 且疑难行偏多，<500 行 × 本地模型 ~1s/行 ≈ 数分钟级，可能**突破 3min**。对策（待用户拍板）：疑难行走**异步/离线第二批**，或"≤3min"仅约束纯规则路径。**默认 `llm_enabled=false` 以保时限**。
2. **多笔合并匹配**（一笔银行 = 多笔 ERP）超出一期规则，标为**二期**；当前遇到即 `needs_human`。
3. **ERP 若只有 CSV 导出、无只读 API**：数据新鲜度受导出时刻限制，需在使用说明里写明。
4. **标注集从何而来**：V 层门禁依赖 ≥500 笔人工标注，需财务初期投入；未就绪前，准确率门禁只能"部分覆盖客观项"，其余标未知区。

## 13. 魔鬼代言人（反例 · 主动构造"它会怎么崩"）

1. **同金额同日期的错配**：两笔金额、日期相同但对应不同发票 → 自动匹配可能张冠李戴，导致财务错账。**缓解**：`ref/参考号`强制参与匹配；同金额出现多候选**一律 `needs_human`，绝不自动二选一**（`rule_match` 已如此设计）。
2. **疑难行激增拖垮时限**：某银行流水格式变体导致大量行落入"疑难" → 开 LLM 时单批超时。**缓解**：疑难行**硬上限**（超则整批标"需人工复核"而非无限重试）+ 监控"疑难率"突增告警 + LLM 单次超时熔断。
3. **幂等被破坏**：同一 `batch_date` 用**不同配置**复跑，结果不同却被当同一批覆盖 → 审计断链。**缓解**：`batch_id = batch_date::config_hash`，配置变则视为**新批次**，旧批次审计留痕不覆盖（§4.4 已如此）。
4. **白名单被路径穿越绕过**：只按字符串前缀比对 `allowlist` 时，`sqlite:///data/../erp.db` 类路径可能骗过校验。**缓解**：`assert_writable_target` **解析为绝对、规范化路径后再比对**（§4.5、§6 已明确）。

## 14. 范式偏见自检（对照案例库"插件化 + 中心化"主流）

- **扩展方式**：本设计选**嵌入式**，与种子案例主流（5/7 插件化）**相反**。已认真评估插件化——因**无第三方生态需求**而判否，并写明其代价（内核生命周期/可逆注册）。选嵌入式不是"没看过插件化"，是**主动克制**（对照 `mini-swe-agent`）。✓ 未被案例带偏。
- **编排**：选**中心化**单管线，评估过去中心化/对等——任务可被单一协调者掌握，对等只增加一致性/调试成本，判否。此处与案例主流一致，但**是基于判据而非随大流**。✓
- **复杂度自查（有没有为不会发生的需求预留机制）**：显式**拒绝**了事件溯源、插件市场、多智能体、分布式、LLM 全量参与，每条都写了否决理由。保留的 `llm_advisor` 接口是为**已知的"疑难行"真实需求**（非虚构），且默认关闭、可插拔——判定为**合理预留，非过度设计**。声明：**无**为臆想需求预留的机制。✓

---

> **决策依据披露**：本示例的范式选型来自 `h-framework.md` §六判据与 §七矩阵；克制决策对照 `mini-swe-agent`（嵌入式）与 `pattern-dependency-injection/event-sourcing/actor-model` 的"何时不用"；V/L 层红线来自 `production-checklist.md`（不让模型自评、引用由程序绑定、拦截至纵深、鉴权写协议）。所有引用的库/API（openpyxl `load_workbook(data_only=True)`、pandas `read_csv`、SQLAlchemy `Session`/`event.listens_for`、pydantic `BaseModel`）均真实存在。

