## Description:

Qinghu Rednote Social helps agents analyze Xiaohongshu trends, notes, comments, and creator data to build content topics, viral-note breakdowns, pain-point libraries, KOC/KOL shortlists, posting plans, and Rednote promotion codes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, social media operators, and agents use this skill to research Xiaohongshu topics, evaluate comparable notes and comments, screen KOC/KOL creators, and prepare planting and content-matrix recommendations. It also guides agents through Qinghu API authorization, result interpretation, credit reporting, and large-result export behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token for Xiaohongshu data workflows.

Mitigation: Use a user-provided token or QINGHU_TOKEN/QHKIT_TOKEN, avoid exposing credentials in conversation or logs, and confirm authorization before API calls.

Risk: Qinghu API calls may consume credits.

Mitigation: Ask for user approval before the first call in a session and report credit use from the response envelope's pointCost value divided by 10000.

Risk: Exported local files may contain campaign, creator, note, or comment data.

Mitigation: Share only intended export links or compact previews, and manage local files according to the user's data handling expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-rednote-social)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow permission check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional JSON request examples, shell command snippets, and exported table files for larger datasets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export table files when returned record arrays contain 10 or more items; API calls require user confirmation and Qinghu credit reporting.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
