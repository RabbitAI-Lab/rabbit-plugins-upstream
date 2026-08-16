## Description:

This skill helps agents query public Xiaohongshu data for content research, high-engagement notes, comments, competitor style, and creator activity without writing marketing copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, analysts, and agents use this skill to retrieve public Xiaohongshu search results, note details, comments, and creator posts for topic research, KOL screening, competitor monitoring, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note/profile URLs, and token-authenticated requests are sent to the Guaikei API.

Mitigation: Use only with authorized public Xiaohongshu targets and avoid private, sensitive, or non-public business targets unless approved.

Risk: Fetched results may be saved locally in logs/.

Mitigation: Review local logs for sensitive targets or analysis outputs and delete them when no longer needed.

Risk: The GUAIKEI_API_TOKEN enables authenticated API access if exposed.

Mitigation: Keep the token in environment or secret-management storage and avoid placing it in prompts, shared files, or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-kol-check)
- [Guaikei API website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; command results may be saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
