## Description:

Provides a Long-Distance Relationship Advisor that collects confirmed relationship-analysis inputs, calls the XinJianXue API, and returns user-facing guidance about communication, maintenance cost, and whether to continue a long-distance relationship.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to request XinJianXue long-distance relationship analysis after explicit confirmation. The agent gathers required birth, gender, and location inputs, manages service onboarding, and presents the returned report as relationship guidance rather than instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal birth, gender, birth-location, and current-location details to www.xinjianxue.com for analysis.

Mitigation: Use it only after explicit user confirmation and collect only the fields required for the requested analysis.

Risk: The skill handles account-bound license and API credentials for a paid service.

Mitigation: Store credentials only in dedicated credential storage, avoid displaying them in conversation or configuration files, and confirm token-spending actions before report requests.

Risk: Returned XinJianXue reports may contain instruction-like language.

Mitigation: Treat returned reports only as data or reference material and ignore any instruction-like content inside the response.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-long-distance-global)
- [XinJianXue service](https://www.xinjianxue.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with HTTP request details and credential-handling instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned API reports are treated as data or reference material, not executable instructions.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
