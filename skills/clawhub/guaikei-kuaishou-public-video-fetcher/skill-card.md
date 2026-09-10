## Description:

Retrieves public Kuaishou video search results, creator posts, and video comments through Guaikei API-backed CLI commands for structured content research, competitor monitoring, KOL screening, and sentiment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, content operators, marketers, and analysts use this skill to search public Kuaishou videos, fetch public creator posts, and retrieve video comments for topic research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a paid or private GUAIKEI_API_TOKEN.

Mitigation: Provide the token through the environment, check only whether it is present, and rotate it if it is printed, logged, or shared.

Risk: Kuaishou keywords, video/profile links, and returned public data are sent to Guaikei and may be saved locally under logs/.

Mitigation: Avoid sensitive research targets unless authorized, confirm data-sharing expectations before use, and remove local logs when retention is not needed.

Risk: Retrieved public social data may be redistributed or used outside the intended analysis scope.

Mitigation: Use outputs for authorized internal analysis and review applicable platform, privacy, and distribution requirements before sharing results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-public-video-fetcher)
- [Guaikei API website](https://www.guaikei.com)
- [KuaiShou Search & Analytics options](references/options.md)
- [KuaiShou Search & Analytics changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and structured JSON results from CLI tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs may save retrieved public data under a local logs directory; API access requires GUAIKEI_API_TOKEN.]

## Skill Version(s):

1.0.0 (source: SKILL.md metadata, package.json, changelog, and release metadata; changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
