## Description:

Searches public Xiaohongshu notes by keyword, retrieves note details and comments, and monitors creator posts through the Guaikei API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Content creators, marketers, market researchers, and analysts use this skill to collect structured public Xiaohongshu data for topic research, competitor monitoring, comment review, creator post tracking, and follow-on reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note URLs, profile URLs, and GUAIKEI_API_TOKEN are sent to the Guaikei API.

Mitigation: Install and run the skill only when that third-party API use is acceptable, and avoid submitting sensitive internal research terms or unauthorized data.

Risk: Saved local logs may contain business research, public content metadata, and links collected during analysis.

Mitigation: Protect or delete generated logs when they are no longer needed.

Risk: The skill is intended for public Xiaohongshu data and does not support private, hidden, or login-required content.

Mitigation: Keep use limited to public content and review outputs before redistribution or operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-search)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON command output with status, request metadata, and result records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful results are also saved to local logs.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
