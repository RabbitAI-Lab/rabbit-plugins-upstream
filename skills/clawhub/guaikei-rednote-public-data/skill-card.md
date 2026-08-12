## Description:

Retrieves structured public Xiaohongshu and RedNote search results, note details, comments, and creator post lists for downstream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Content, marketing, research, and data teams use this skill to collect public Xiaohongshu and RedNote content for trend discovery, competitor monitoring, KOL screening, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or links and the GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use the skill only when that data sharing is acceptable, and provide the token through the documented environment variable.

Risk: Generated local logs can contain research targets, URLs, profile metadata, or comment data.

Mitigation: Review, retain, or delete generated logs according to the user's data handling requirements.

Risk: Collected social-media data may be subject to platform, privacy, or legal restrictions.

Mitigation: Use the skill only for lawfully accessible public content under applicable platform and privacy rules.

## Reference(s):

- [Guaikei service website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Node.js CLI commands that return structured JSON results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save task outputs under the local logs directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
