## Description:

Retrieves structured public Xiaohongshu note, profile-post, interaction, and comment data to help agents support content research, competitor monitoring, KOL screening, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, and analysts use this skill to retrieve public Xiaohongshu search results, note details, creator posts, and comments for research and reporting. It is not intended for private data, logged-in data, follower estimation, or direct marketing decisions without human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note URLs, profile URLs, and retrieved public data to guaikei.com using GUAIKEI_API_TOKEN.

Mitigation: Use the skill only when third-party processing by guaikei.com is acceptable, keep the token secret, and avoid submitting sensitive or non-public targets.

Risk: Command results may be saved locally as retained research data, including comments or competitor-monitoring exports.

Mitigation: Protect or delete the logs directory according to the user's data-handling rules.

Risk: Returned engagement data can be incomplete, stale, unavailable, or misleading if the source content changes or the API returns errors.

Mitigation: Check status and error_code fields before analysis, retry transient failures, and require human review before making business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-radar)
- [Guaikei service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; command execution returns structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful runs may save JSON results under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
