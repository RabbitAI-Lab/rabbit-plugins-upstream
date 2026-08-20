## Description:

青虎AI 电商选品上货 helps agents use Qinghu ecommerce data workflows for cross-platform product sourcing, competitor analysis, market assessment, supply collection, and listing support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and agents use this skill to route product research, competitor analysis, market evaluation, sourcing, and listing tasks across Amazon, TikTok Shop, Shopee, Ozon, Douyin, Xiaohongshu, Bilibili, and 1688. The skill is intended to produce concise recommendations, supporting metrics, and exported detail files when result sets are large.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform shop-listing workflows that may affect real ecommerce accounts.

Mitigation: Use a dedicated Qinghu token with limited scope and require explicit confirmation before listing or publishing actions affect a shop account.

Risk: The skill may create automatic local exports for larger ecommerce result sets without enough storage disclosure.

Mitigation: Tell the user when files are created, avoid putting secrets in exports, and review file contents before sharing them.

Risk: Qinghu-collected ecommerce data may differ from seller-backend or platform-native metrics.

Mitigation: Label platform, site, period, and sample size, and advise users to validate important business decisions against platform backend data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ecom-sourcing)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, API Calls, Code, Shell commands, Configuration instructions, Files, Markdown]

**Output Format:** [Markdown guidance with JSON API payloads, inline code or shell examples, and exported table files for larger result sets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a Qinghu token; paid tool calls and shop-listing actions should require explicit user authorization.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
