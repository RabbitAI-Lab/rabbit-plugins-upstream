## Description:

财务分析入门工具 helps individual investors, junior analysts, and finance students analyze a single company through valuation modeling, financial ratio analysis, and basic risk assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, individual investors, junior analysts, and finance students use this skill to turn natural-language finance-analysis requests into structured single-company workflows covering DCF valuation, comparable valuation, ratios, cash flow, and risk checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad file, command, and API authority for finance-analysis workflows.

Mitigation: Review the skill before installation, keep use limited to explicit finance-analysis tasks, and avoid broad filesystem access.

Risk: Private financial files or API keys could be exposed if credentials or sensitive inputs are provided without a clear external-provider requirement.

Mitigation: Do not provide credentials unless the external provider is known and required; pass credentials through controlled environment mechanisms when needed.

Risk: Batch or automated report claims exceed the free-edition single-target scope described by the evidence.

Mitigation: Treat batch and automated report behavior as unsupported unless separately reviewed and tested.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/accounting-finance-tool-free)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with text inputs, YAML configuration examples, and structured analysis-report outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free-edition scope is single-target analysis; quality depends on user-provided financial data and assumptions.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
