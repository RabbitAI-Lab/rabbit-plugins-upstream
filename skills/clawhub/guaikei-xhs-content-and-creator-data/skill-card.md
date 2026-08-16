## Description:

Searches public Xiaohongshu notes, retrieves note details and comments, and lists creator posts for content research, competitor analysis, KOL screening, and trend discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, market analysts, and creator teams use this skill to retrieve structured public Xiaohongshu content, comments, and creator-post data for topic research, competitor monitoring, trend analysis, and KOL screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, and requested public data are sent to Guaikei.

Mitigation: Use the skill only when that data sharing is acceptable for the user's task and avoid submitting sensitive research inputs.

Risk: Successful results can be stored locally in logs/.

Mitigation: Review terminal and workspace output before sharing it, and periodically delete logs that contain sensitive research or creator data.

Risk: GUAIKEI_API_TOKEN is required for API access.

Mitigation: Provide the token through the environment, treat it as a secret, and avoid exposing it in shared output or committed files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-content-and-creator-data)
- [Guaikei website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance, Configuration]

**Output Format:** [Structured JSON from Node.js command-line scripts, with human-facing guidance for routing and follow-up analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and can save successful results to logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
