## Description:

青虎AI B 站社媒运营 helps agents use Qinghu Bilibili data APIs to analyze Bilibili trends, video scripts, comments, creator profiles, and creator videos for content strategy, sentiment review, and UP creator placement planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, marketers, and agent builders use this skill to plan Bilibili content and placement strategy from Qinghu data, including topic selection, long-form video structure analysis, comment sentiment, and UP creator matching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read a Qinghu token from the user or environment to access Qinghu Bilibili data APIs.

Mitigation: Install and invoke it only when Qinghu API access is expected, and provide credentials only in contexts where the agent is authorized to use that account.

Risk: Some Qinghu tool calls may spend Qinghu points after consent.

Mitigation: Confirm paid-tool authorization before use and review reported Qinghu point consumption for the session.

Risk: Larger result sets may be exported as local table files in the workspace.

Mitigation: Avoid using the skill for sensitive research that should not be saved locally, and review or remove exported files according to workspace data-handling policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-bilibili-social)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow permission check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON-RPC examples, shell command examples, and exported local table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request a Qinghu token, may call Qinghu Bilibili data tools, and may export result sets of 10 or more records to local table files.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
