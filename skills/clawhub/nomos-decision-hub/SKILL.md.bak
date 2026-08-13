---
name: nomos-decision-hub
slug: nomos-decision-hub
version: 2.0.0
displayName: NOMOS 决策引擎
description: 确定性决策引擎，支持因果分析、合规审计、压力测试、根因追溯，通过新加坡IMDA AI Verify 95/100合规审计
required_commands:
  - python3
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
当用户询问以下内容时自动触发：
- 确定性/可审计决策引擎设计
- 因果反事实分析、根因追溯
- AI决策合规审计（IMDA/EU标准）
- 决策场景压力测试、鲁棒性分析
- 高风险决策的人在环治理方案
- 企业级决策系统部署方案
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
