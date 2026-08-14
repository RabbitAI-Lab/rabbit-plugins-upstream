## Description:

Guaikei XHS Search helps agents query public Xiaohongshu notes, note details, comments, and creator posts for trend, competitor, KOL, and content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External content creators, marketing teams, data analysts, and agents use this skill to retrieve public Xiaohongshu search results, note details, comments, and creator posts for market research and content planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, and the GUAIKEI API token are sent to guaikei.com.

Mitigation: Use the skill only when that third-party data sharing is acceptable, and configure the token only in trusted agent environments.

Risk: Returned public-data results may be saved locally under logs.

Mitigation: Review or delete generated log files when research is sensitive or the system is shared.

## Reference(s):

- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei API Website](https://www.guaikei.com)
- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with CLI commands; command execution returns structured JSON and may save local log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and sends public Xiaohongshu keywords or URLs to guaikei.com.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact package.json, SKILL.md metadata, and changelog report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
