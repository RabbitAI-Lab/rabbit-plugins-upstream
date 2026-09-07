## Description:

Helps construction and engineering bid teams evaluate a specific tender using ZhiLiaoBiaoXun historical tender data, including bid/no-bid posture, likely competitors, pricing references, qualification risks, and report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External construction bidders, bid managers, and business development teams use this skill to analyze whether to pursue a concrete engineering tender, estimate competitive pricing, identify likely bidders, and produce a decision report backed by cited tender records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic trial registration sends a MAC-hash-based device identifier to the provider.

Mitigation: Prefer a preconfigured ZLBX_API_KEY when available and require user consent before automatic registration.

Risk: The skill can store an API key in the user's home directory.

Mitigation: Avoid exposing the local config file or key values in chat, logs, reports, or shared workspaces.

Risk: Generated reports preserve signed access links that may expose tender or company records.

Mitigation: Treat generated HTML reports and signed links as sensitive and review recipients before sharing.

Risk: The security summary flags unsafe HTML link rendering.

Mitigation: Open generated HTML only from trusted report data and review links before distribution.

Risk: Bid recommendations may be misleading when historical tender data is incomplete or outdated.

Mitigation: Require reports to label data gaps, cite time ranges, and support commercial decisions with human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/construction-tender-bid-decision)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Bid decision workflow](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto registration details](artifact/references/auto-register.md)
- [ZhiLiaoBiaoXun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZhiLiaoBiaoXun skill docs](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [text, markdown, HTML file, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report with an optional self-contained HTML report file and cited tender-record links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include data-source notes, data gaps, estimated API-credit use, and at most 20 rendered citation details.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
