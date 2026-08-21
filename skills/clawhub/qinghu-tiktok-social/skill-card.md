## Description:

青虎AI TikTok 社媒运营 helps agents monitor TikTok industry trends and video rankings, search high-engagement content, inspect video details and comments, and produce topic ideas for short-form video planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External social media operators and content teams use this skill to identify what to post on TikTok, track industry and competitor content trends, and turn ranking, search, video-detail, and comment signals into actionable content calendars and topic lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Qinghu API credentials from the environment or from user input.

Mitigation: Use a narrowly scoped Qinghu token, avoid sharing tokens in chat, and rotate or revoke the token after use when appropriate.

Risk: Qinghu API calls may spend credits after session-level user approval.

Mitigation: Confirm the intended tools before first use, report observed Qinghu credit consumption, and stop when authorization is absent or unclear.

Risk: Large TikTok datasets may be exported or cached as local files without a fresh opt-in for each file.

Mitigation: Store exports only as needed, share concise previews instead of raw tables in chat, and delete exported or cached files when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-social)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow authentication check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [guidance, markdown, files]

**Output Format:** [Markdown summaries with optional exported spreadsheet or cached data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs emphasize topic recommendations, trend rankings, competitor account updates, comment insights, data-period labels, and Qinghu credit usage when paid calls are made.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
