## Description:

Collects public Xiaohongshu content for note search, note details, comments, and creator-post monitoring when an agent is working with Xiaohongshu, XHS, or RedNote content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, content operators, and market analysts use this skill to retrieve structured public Xiaohongshu data for content research, competitor monitoring, KOL screening, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note or profile URLs, and token-authenticated requests are sent to guaikei.com.

Mitigation: Install only when that data sharing is acceptable, and avoid submitting sensitive URLs or secrets.

Risk: Collected research targets or results may remain on disk in generated logs.

Mitigation: Periodically review or delete generated logs when the collected data should not be retained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-content-collector)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON results from the invoked command-line tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; successful results may be saved locally under logs.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
