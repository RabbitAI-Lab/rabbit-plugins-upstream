## Description:

Searches public Xiaohongshu posts by keyword and helps agents retrieve post details, comments, creator posts, engagement metrics, and direct links for content and market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, brand marketing teams, analysts, and agents use this skill to research public Xiaohongshu content, identify viral topics, review comments, monitor competitors or creators, and summarize findings from returned data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and returned public Xiaohongshu content pass through GuaiKei's third-party API.

Mitigation: Use the skill only for public data and topics that are appropriate to send to GuaiKei; avoid sensitive research topics and private or internal target lists.

Risk: Full result JSON may be saved locally under logs/ without an evidence-backed retention or disable control.

Mitigation: Run the skill in a workspace with appropriate local access controls and review or remove logs after use when data should not be retained.

Risk: The security verdict is suspicious because the skill collects Xiaohongshu comments and creator-post data through a third-party API.

Mitigation: Review the skill before installing and confirm that token handling, API use, collection scope, and local logging fit the deployment policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-viral-mining)
- [GuaiKei service site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN. Command results include status, error_code, message, request metadata, skill metadata, and results; successful runs may save full result JSON under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
