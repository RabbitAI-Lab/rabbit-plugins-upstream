## Description:

青虎AI 电商选品上货 routes e-commerce sourcing, competitor analysis, keyword research, market evaluation, supplier collection, and listing workflows across Amazon, TikTok Shop, Shopee, Ozon, Douyin, Xiaohongshu, Bilibili, and 1688 using Qinghu data APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and agents use this skill to choose the right Qinghu data workflow for product sourcing, competitor analysis, market checks, supplier lookup, and storefront listing tasks. It helps agents request required platform context, obtain user approval before tool calls, parse Qinghu API responses, and present concise business conclusions with exported detail files when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Qinghu API credentials and may read QINGHU_TOKEN or QHKIT_TOKEN from the environment.

Mitigation: Keep tokens scoped to the Qinghu service, avoid sharing them in chat, and rotate them if exposed.

Risk: Some Qinghu tool calls may consume credits or perform upload/listing actions.

Mitigation: Review the listed tools and intended actions before approving a call, especially paid or upload-related workflows.

Risk: Large result sets may be exported to local files.

Mitigation: Review exported files before sharing them and remove sensitive business data when it is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-ecom-sourcing)
- [Qinghu MCP API Endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API Key Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu Workflow Auth Check Endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON and shell command examples; may reference exported table files for larger result sets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Qinghu token supplied by the user or environment and user approval before Qinghu tool calls.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
