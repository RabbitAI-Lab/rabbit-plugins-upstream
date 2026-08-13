## Description:

Searches public Xiaohongshu notes, note details, comments, and creator post lists to support content research, competitor analysis, KOL screening, and trend discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, content operators, and market analysts use this skill to retrieve public Xiaohongshu content and interaction data for topic research, competitor monitoring, comment analysis, KOL screening, and reporting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note URLs, profile URLs, and GUAIKEI_API_TOKEN are sent to the disclosed guaikei.com API service.

Mitigation: Use the skill only when this third-party data sharing is acceptable, and keep GUAIKEI_API_TOKEN scoped to trusted environments.

Risk: Local logs may retain commercially sensitive queries, targets, comments, or collected public-content data.

Mitigation: Review, protect, or delete the local logs directory according to the sensitivity of each task.

Risk: The artifact license metadata does not match the server-level release license evidence.

Mitigation: Confirm the intended release license before public publication or downstream redistribution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/xhs-dashboard-build)
- [Publisher Profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Text]

**Output Format:** [Markdown guidance with shell command examples and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes local result logs as documented.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
