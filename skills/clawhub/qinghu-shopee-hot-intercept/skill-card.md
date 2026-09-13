## Description:

Helps agents use Qinghu Shopee and 1688 marketplace data to find hot Shopee products, validate demand trends, compare price bands, locate same-item sourcing, and recommend follow-selling or differentiated sourcing strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and agents use this skill to investigate Shopee hot products by site and category, validate product trends, estimate price-band competition and margin potential, and produce concise recommendations with optional local table exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Qinghu API key and sends Shopee and 1688 analysis requests to Qinghu.

Mitigation: Install only when that data sharing is acceptable, provide a scoped Qinghu key where possible, and avoid entering unrelated secrets.

Risk: Marketplace data calls may consume Qinghu credits after user confirmation.

Mitigation: Confirm planned tool calls before execution and report actual Qinghu credit consumption from the returned pointCost values.

Risk: Large result sets may be exported automatically to local table files.

Mitigation: Review exported files before sharing them and remove any unnecessary local data after use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-hot-intercept)
- [Qinghu marketplace data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Concise Markdown recommendations with JSON or shell snippets and optional exported table files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Qinghu API key; tool calls require user confirmation, may consume Qinghu credits, and larger result sets may be exported to local table files.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
