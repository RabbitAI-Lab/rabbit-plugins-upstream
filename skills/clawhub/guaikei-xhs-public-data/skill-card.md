## Description:

Provides structured public Xiaohongshu data for viral-post discovery, competitor monitoring, KOL screening, and comment insight workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content creators, marketers, and analysts use this skill to fetch public Xiaohongshu search results, note details, note comments, and creator post lists for downstream analysis or reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, and GUAIKEI_API_TOKEN are sent to the third-party guaikei.com API service.

Mitigation: Use the skill only where that data sharing is approved, and avoid submitting sensitive or unauthorized inputs.

Risk: Local logs can retain research data such as comments, profile or note URLs, and access-like query tokens.

Mitigation: Protect or delete the logs directory on shared, synced, or long-lived machines.

Risk: The skill is limited to public Xiaohongshu data and does not provide private, hidden, or login-only content.

Mitigation: Confirm user requests are limited to public data before running commands, and ask for clarification when the link or task is ambiguous.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-public-data)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with Node.js shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; command output includes status, error_code, request, skill_metadata, and results fields.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
