## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Meeting participants and teams use the skill to turn explicitly requested feature and bug discussions into sanitized, confidential GitLab issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unclear request or destination could lead to an unintended issue write.

Mitigation: Require an explicit request and a clearly selected project; resolve ambiguity before creating an issue.

Risk: Sanitization and confidentiality checks depend on instructions, and live integration behavior was not tested.

Mitigation: Use a project-scoped integration, inspect the full outgoing content and attachments, set confidential=true at creation, and verify the result.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, API Calls, Text]

**Output Format:** [Sanitized English GitLab issue content and brief chat replies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issue creation requires an explicit, sufficiently clear request; issues are created as confidential.]

## Skill Version(s):

1.129.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
