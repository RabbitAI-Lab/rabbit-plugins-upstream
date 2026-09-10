## Description:

Guides agents through Bilibili social media operations using Qinghu data APIs to analyze trends, mid- and long-form video scripts, comments, audience sentiment, and UP creator fit for content seeding campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing operators and developers use this skill to plan Bilibili content strategy, deconstruct mid- and long-form videos, assess comment sentiment, and identify suitable UP creators for content seeding campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token for Bilibili analysis.

Mitigation: Use environment variables or direct secret entry where available, avoid exposing the token in shared outputs, and approve API access only for trusted sessions.

Risk: Qinghu API calls may consume account credits.

Mitigation: Confirm the planned tools before first use and report actual Qinghu point consumption from the response envelope after paid calls.

Risk: Large result sets may be saved as local spreadsheet or export files.

Mitigation: Review exported files before sharing and include only the data needed for the campaign analysis.

Risk: Bilibili commercial content planning can create platform disclosure and compliance obligations.

Mitigation: Review Bilibili commercial-content rules and disclosure requirements before publishing or placing sponsored content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-bilibili-social)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with JSON-RPC/API examples and optional local spreadsheet or export files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large result sets are expected to be exported as local files with concise previews; paid Qinghu calls should report actual Qinghu point consumption.]

## Skill Version(s):

0.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
