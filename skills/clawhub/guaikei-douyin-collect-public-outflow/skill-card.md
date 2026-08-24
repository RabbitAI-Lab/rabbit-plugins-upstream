## Description:

Collects public Douyin keyword search, creator post, video comment, and trending topic data through CLI workflows for short-video research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to collect public Douyin search results, creator posts, video comments, and hot-list topics for content planning, competitor monitoring, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk collection of public social platform data can capture personal or sensitive social signals at scale.

Mitigation: Use the skill only for public Douyin data that the user is allowed to collect, minimize requested limits, and review outputs before reuse or sharing.

Risk: Search terms, creator or video URLs, requested limits, and GUAIKEI_API_TOKEN are transmitted to www.guaikei.com.

Mitigation: Use a dedicated token, avoid submitting confidential search terms or private URLs, and rotate or revoke the token if exposure is suspected.

Risk: Retrieved public data is saved locally in logs by default.

Mitigation: Store logs in an access-controlled location, delete logs when no longer needed, and avoid committing generated logs to repositories.

Risk: Security evidence reports runtime behavior that may conflict with the skill safety notes.

Mitigation: Review stderr and runtime messages during validation, and do not rely solely on the artifact's safety notes when assessing deployment risk.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-collect-public-outflow)
- [Guaikei token and support site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [CLI input and output schemas](assets/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON results on stdout, operational messages on stderr, and JSON log files saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and a GUAIKEI_API_TOKEN; commands can request up to 10000 public records per operation.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, SKILL.md metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
