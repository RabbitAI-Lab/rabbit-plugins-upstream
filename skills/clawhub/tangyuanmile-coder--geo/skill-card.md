## Description:

基于爱搜 MCP/API 或已提供的原始对话数据，制作 GEO 商品诊断静态 HTML 报告，展示商品卡指标、品牌转卡表现及每个搜索意图下的平台商品榜。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tangyuanmile-coder](https://clawhub.ai/user/tangyuanmile-coder)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations analysts use this skill to turn AIDSO or WorkBuddy GEO product-card samples, or supplied raw dialog exports, into single-day static HTML diagnostic reports for product-card monitoring and competitive environment reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: New sampling can spend AIDSO points if the user authorizes a paid task plan.

Mitigation: Review the full confirmation card, current point pricing, prompts, platform combinations, and repeat count before using the exact paid-authorization phrase.

Risk: AIDSO credentials or raw customer data could be exposed if copied into chat, reports, logs, or package files.

Mitigation: Keep tokens in the WorkBuddy connector or environment configuration, and exclude credentials, raw customer data, local paths, and internal IDs from generated reports and distributable packages.

Risk: Reports may mislead if generated from incomplete samples, unsupported platform combinations, or unverified product taxonomy.

Mitigation: Validate the configured date, question set, supported combinations, source files, taxonomy, sample denominators, and final HTML hash before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tangyuanmile-coder/skills/geo)
- [Input and evidence contract](references/input-contract.md)
- [Metrics and calculations](references/metrics.md)
- [Static report specification](references/report-spec.md)
- [AIDSO MCP and HTTP API reference](references/aidso-api.md)
- [WorkBuddy package contract](references/workbuddy-contract.md)
- [AIDSO API service](https://geo.aidso.com/apiService)
- [AIDSO point pricing](https://geo.aidso.com/question)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese-language Markdown guidance with bash commands, JSON configuration, and static HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline report generation works on provided files; new sampling requires explicit paid authorization and externally configured AIDSO credentials.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
