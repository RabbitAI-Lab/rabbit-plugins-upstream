## Description:

青虎AI 电商选品上货 helps agents coordinate e-commerce product sourcing, competitor analysis, market evaluation, supplier discovery, and listing workflows across Amazon, TikTok Shop, Shopee, Ozon, Douyin, Xiaohongshu, Bilibili, and 1688 using Qinghu-authorized data tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce operators, and agent developers use this skill to route product selection, competitor analysis, market research, sourcing, and listing tasks through Qinghu data workflows. It is designed for workflows that require platform, site, category, period, authorization, and cost checks before data or listing actions are performed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Qinghu API tokens and may expose sensitive access if credentials are pasted into prompts or stored in generated files.

Mitigation: Use environment variables or direct user entry for tokens, avoid echoing credentials, and review outputs before sharing exported files.

Risk: Data calls can spend Qinghu credits.

Mitigation: Before approving calls, review the listed tools, expected cost, target platform or account, and final reported credit usage.

Risk: Exports may contain sensitive business research such as product opportunities, competitor data, keywords, or supplier findings.

Mitigation: Treat generated spreadsheets and cached result files as business-sensitive and share them only with intended recipients.

Risk: Listing workflows can affect store content when approved.

Mitigation: Confirm the exact store or account, product links, template, intended edits, and failure handling before permitting listing-related actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ecom-sourcing)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu login](https://www.iqinghu.com/workbench/login?type=1&urlCode=1788417429126)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow authorization check](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Concise Markdown responses with optional exported table files and inline shell or API examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to generated spreadsheet files when result sets contain 10 or more records.]

## Skill Version(s):

0.1.3 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
