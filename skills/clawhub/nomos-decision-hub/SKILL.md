---
name: nomos-decision-hub
slug: nomos-decision-hub
version: 2.0.0
displayName: NOMOS 决策引擎
description: 确定性决策引擎，支持因果分析、合规审计、压力测试、根因追溯。企业级部署需独立服务与数据库。
required_commands:
  - python3
# Capability disclosure (NVIDIA MCP Least-Privilege): declared vs. actual.
# The skill's runtime engine (second_perspective) requires the following
# beyond `python3`. Loaders must grant these explicitly, not implicitly.
capabilities:
  network_egress:
    - purpose: "OIDC discovery & JWKS fetch (HTTPS only, issuer-controlled host)"
      scope: "outbound to SP_OIDC_ISSUER and its jwks_uri only"
  env_read:
    - SP_API_KEY
    - SP_DATABASE_DSN          # contains PostgreSQL credentials
    - SP_OIDC_ISSUER
    - SP_OIDC_CLIENT_ID
    - SP_OIDC_AUDIENCE
    - SP_PUBLIC_BASE_URL
  database: "PostgreSQL connection via SP_DATABASE_DSN"
  docker_deploy: true
  binds_port: "0.0.0.0:8000 (configurable; requires external network isolation)"
metadata:
  openclaw:
    required_binaries:
      - python3
    emoji: "⚖️"
    homepage: "https://github.com/nohn3043-arch/second-perspective"
---
# NOMOS 智能决策引擎
基于决定论因果推理的可审计决策编排层，完全无概率黑盒，所有决策可分解为可追溯的因果拓扑，支持合规级审计链路、场景压力测试、人在环治理。
## 触发场景
仅当用户明确提及以下命名实体时触发（避免宽泛关键词误加载）：
- NOMOS 决策引擎 / NOMOS Decision-Hub / second_perspective
- 引用本技能生成的「密封报告」规范或「决策场景库」模板
- 明确的因果反事实分析、根因追溯、场景压力测试请求，且指明使用本引擎

注意：通用话题（如"AI决策合规审计""企业级部署方案""高风险决策治理"）**不应**自动触发本技能，除非用户显式引用上述命名实体。
## 核心能力
✅ **确定性评估**：硬约束门槛+软约束显式罚分，无隐藏分数调整
✅ **细粒度算法审计**：所有操作生成哈希链式审计事件，任何修改都会破坏验证
✅ **因果反事实重选**：假设失效时自动计算传递性失效闭包，重选幸存候选
✅ **场景压力测试**：支持声明式指标覆盖、证据缺失、假设失效模拟
✅ **逆向根因追溯**：从观测偏差反向追溯假设失效点，输出带因果链的根因假设
✅ **敏感性/鲁棒性分析**：计算帕累托前沿，识别脆弱准则，输出排名稳定性得分
✅ **企业级部署支持**：Docker容器化、PostgreSQL持久化、OIDC身份验证集成
## 使用方法
### 基础决策分析
```python
from second_perspective import IntelligentDecisionHub
from second_perspective.models import HubAnalysisRequest
request = HubAnalysisRequest.model_validate({
    "decision": decision_payload,  # 参考 examples/market_entry.json
    "scenarios": [
        {"id": "SC1", "name": "关键假设失效",
         "failed_assumption_ids": ["A1"]},
        {"id": "SC2", "name": "成本冲击",
         "metric_overrides": {"S2": {"capital_required": 6000000}}},
    ],
})
report = IntelligentDecisionHub().analyze(request)
print(report.model_dump_json(indent=2))
```
### 企业级部署
```bash
# Docker部署
docker build -t nomos-hub .
docker run -p 8000:8000 \
  -e SP_ENV=production \
  -e SP_API_KEY=your-secret-key \
  -e SP_DATABASE_DSN=postgresql://user:pass@db:5432/nomos \
  nomos-hub
```
## v2.0 升级能力（P0-P2）

### 🔏 密封报告规范（P0）
所有 P0/P1 决策输出**密封报告**（tamper-evident）：五算子输出哈希链式互链（Merkle 因果链）+ 确定性 JSON + HMAC 签封。审计者一键验证（SEAL VALID / TAMPERED）。规范见 `references/SealedReportSpec.md`。
### 🌐 官网审计引擎对接（P0）
线上 SPL Cognitive Audit Engine（nohnlins.com/audit/）与本技能共享同一五算子语义——技能生成密封报告，官网提供在线体验；双向一致，审计链不因载体而变。
### 📚 决策场景库（P1）
预置 4 类场景模板（合规门禁/战略押注/根因追溯/资源分配），复制-替换-运行即得密封报告。见 `references/DecisionScenarioLibrary.md`。
### 🌍 多语言导出（P2）
报告携带 `lang` 字段（zh/en），同一条因果链可渲染为目标语言，无需重跑引擎。

## 文件
- `references/SealedReportSpec.md`（P0 密封报告格式 + 验证流程）
- `references/DecisionScenarioLibrary.md`（P1 场景库）
- `examples/`、`docs/`、`scripts/`（引擎配套）

## 确定性契约（不变量）
- 引擎绝不猜测缺失的权重、证据、阈值、授权关系
- 硬约束决定准入资格，软约束必须声明显式罚分，无静默分数变更
- 所有影响行为的政策携带`policy_id`和`version`，嵌入结果中
- 证据质量由指定责任节点评估，引擎不虚构可信度
- 假设失效沿依赖图传播，明确命名受影响的备选方案
- 输出永远是"声明输入下的领先候选"，最终决定权在算法之外
- 审批人姓名+`authorization_ref`必须与锚定的决策所有者匹配
- 所有评估/审批都是通过哈希链接的新修订，无静默覆盖
## 授权说明
仅允许个人非商业研究使用，政府/企业商业使用需获得书面授权。
