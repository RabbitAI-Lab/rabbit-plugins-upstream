---
name: lgd-crypto-guard
description: lgd-crypto-guard — 把 LGD 三律（有籍·有证·有门禁）翻译进隐私计算 / 数据加密与最小化 AI 应用（联邦·密文·脱敏）的合规守门器，对 AI 系统做三律自评与门禁判定（零依赖）。 适用场景：当需要隐私计算守门能力时使用本技能；触发词：lgd-crypto-guard。
slug: lgd-crypto-guard
version: 1.0.1
display_name: 隐私计算守门
display_name_en: Privacy-Compute Guard
agent_created: true
author: XLGD · 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch
category: AI 治理
platforms: [windows, macos, linux]
copyright: XLGD · SynomosAI
description_zh: "lgd-crypto-guard — 把 LGD 三律（有籍·有证·有门禁）翻译进隐私计算 / 数据加密与最小化 AI 应用（联邦·密文·脱敏）的合规守门器，对 AI 系统做三律自评与门禁判定（零依赖）。"
description_en: "Translate the LGD three laws into privacy-computing and minimized AI applications (federated, ciphertext, desensitized): three-law self-assessment and gate decisions (zero-dependency)."
classification:
  skillhub: ["ai-governance"]
  iso_25010: ["Security", "Maintainability"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium（按默认策略设计为中等风险）：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high 并走人工批准。"
tags: [lgd-crypto-guard, AI 治理, 隐私计算, 数据最小化]
read_when:
  - AI 模型部署前要验证数据流转是否符合 LGD 三律
  - 系统处理敏感数据，涉及隐私计算/联邦学习/密文传输且要最小化原则
  - AI 接口有日志泄露风险或权限分级错误，要自动脱敏与门禁拦截
  - 用户说「这个隐私计算方案合规吗」「明文有没有出安全区」
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/crypto_guard.py
  runtime: python3
  call_pattern: args
input_schema:
  args:
    type: string
    description: "命令行参数透传给主脚本，具体取值见各包 --help"
    required: false
output_schema:
  stdout:
    type: string
    description: "标准输出为 JSON 结果，含逐项检查与总体结论"
  exit_code:
    type: integer
    description: "0=PASS/完成；1=FAIL/有警告或待补强；2=用法或参数错误"
capabilities:
  - cli_tool
permissions:
  network: false
  filesystem: false
  subprocess: false
requirements:
  python_packages: []
  min_python: "3.8"
changelog: "1.0.1: Bilingual rewrite (full EN+ZH, English first), added read_when; 1.0.0: initial upload (USK v3)"

---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：见平台质量门禁规范

## English

### When to use
- Call it before an AI model deployment, to verify that data flows meet the LGD "registered · evidenced · gated" standard.
- Enable it when a system handles sensitive data in privacy-computing, federated-learning or ciphertext-transmission scenarios and must satisfy the data-minimization principle.
- Use it when an AI interface shows log-leakage risk or flawed permission tiers, triggering automatic desensitization and gate blocking.

### Usage
In a Python runtime, import the core classes and functions from the `crypto_guard.py` module. Configure the inputs as the data source under check, the model path and the compliance policy level (e.g. HIGH). Recommended invocation:
```python
from crypto_guard import GuardianEngine, LGD_POLICY
guard = GuardianEngine(policy=LGD_POLICY.STRICT)
result = guard.check_model(ai_model_path="local/model.pkl")
```

### Workflow
1. **Environment prep**: load the `crypto_guard` module; confirm no dependency conflicts.
2. **Data assembly**: organize the AI model file, training dataset and access-request context into a standardized input object.
3. **Compliance scan**: run the evaluation engine for an LGD three-law self-check on data lineage and encryption strategy.
4. **Report generation**: emit a structured report with the "registered / evidenced / gated" status verdicts.
5. **Execution control**: if the check fails, automatically issue encryption, desensitization or access-denial instructions; on pass, open the service.

### Evidence & safety statement
- Evidence: TBD (no evaluation / badge link yet; update here once it is produced)
- Version: 1.0.1
- Security: no independent security scan has been performed (TBD); the conclusion is pending and no endorsement is given until it is completed.

## 中文

### 何时用
在 AI 模型部署前需验证数据流转是否符合 LGD“有籍·有证·有门禁”标准时调用。
当系统处理敏感数据，涉及隐私计算、联邦学习或密文传输场景且需满足最小化原则时启用。
若检测到 AI 接口存在日志泄露风险或权限分级错误，需触发自动脱敏与门禁拦截机制时使用。

### 用法
在 Python 执行环境中，直接导入 `crypto_guard.py` 模块中的核心类与函数。需配置输入参数为待检数据源、模型路径及合规策略等级（如 HIGH）。实际调用推荐通过以下结构初始化并发送请求：
```python
from crypto_guard import GuardianEngine, LGD_POLICY
guard = GuardianEngine(policy=LGD_POLICY.STRICT)
result = guard.check_model(ai_model_path="local/model.pkl")
```

### 流程
1. **环境准备**：加载 `crypto_guard` 模块，确认无依赖冲突。
2. **数据构建**：组织 AI 模型文件、训练数据集及访问请求上下文为标准化输入对象。
3. **合规扫描**：调用评估引擎对数据血缘与加密策略进行 LGD 三律自检。
4. **报告生成**：输出包含“有籍/有证/门禁”状态判定结果的结构化报告。
5. **执行控制**：若校验未通过，自动触发数据加密、脱敏或访问拒绝指令；通过后开放服务。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.0.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
