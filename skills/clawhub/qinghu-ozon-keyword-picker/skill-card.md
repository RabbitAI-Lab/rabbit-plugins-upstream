## Description:

Guides agents through Qinghu-powered Ozon keyword research, including hot keyword rankings, keyword detail and trend checks, related product analysis, and product traffic keyword review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Ozon sellers, ecommerce analysts, and agent users use this skill to discover Russian buyer search demand, inspect keyword trends, map keywords to competing products, and turn keyword evidence into product selection and listing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for or read a Qinghu API token.

Mitigation: Use a user-provided token or approved environment variable, avoid exposing the token in responses or exports, and keep authentication details limited to the Qinghu API request.

Risk: Qinghu API calls may consume Qinghu credits after confirmation.

Mitigation: Obtain user confirmation before the first data call, use the required workflow to track pointCost, and report Qinghu credit usage using the documented conversion.

Risk: Large result sets may be generated as local exported files.

Mitigation: Check exported files before sharing links and keep chat previews concise so the user can review the generated data deliberately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-keyword-picker)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown responses with optional exported table files and JSON API-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Qinghu API token and user confirmation before Qinghu data calls; large result sets are exported instead of pasted into chat.]

## Skill Version(s):

0.1.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
