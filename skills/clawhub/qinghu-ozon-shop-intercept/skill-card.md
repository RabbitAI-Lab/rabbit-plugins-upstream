## Description:

This skill helps agents analyze Ozon competitor shops using Qinghu data, including shop trends, active products, sales structure, emerging products, and actionable replication recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and agent users use this skill to identify comparable Ozon shops, inspect their product mix and growth signals, and produce concise follow-up recommendations. It is intended for shop-level competitor research rather than listing operations or full store management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API key to access Ozon shop research data.

Mitigation: Confirm the user is comfortable providing or exposing the key through QINGHU_TOKEN or QHKIT_TOKEN before use.

Risk: External Qinghu API calls may consume Qinghu credits.

Mitigation: Request user authorization before data calls and report costs using the returned pointCost conversion when available.

Risk: Large competitor datasets may be exported to local files.

Mitigation: Tell the user where exported files are written and avoid exposing more data in chat than necessary.

Risk: Competitor follow-up recommendations can involve brand, authorization, or patent considerations.

Mitigation: Prompt users to verify brand authorization and intellectual-property constraints before acting on product recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-shop-intercept)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow authentication check](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples, plus exported local files for larger datasets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Qinghu data tools after user authorization and may export larger result sets to local spreadsheet files.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
