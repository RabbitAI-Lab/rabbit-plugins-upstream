## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to update a GitLab agent profile with contribution statistics, static charts, and a proof file for public and redacted private activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses GitLab token access to scan configured groups and projects.

Mitigation: Use a least-privilege GitLab token and prefer an explicit project list over broad group discovery.

Risk: Generated public outputs can include aggregate private or internal contribution totals.

Mitigation: Review the generated proof file and chart before publishing or pushing profile assets.

Risk: The workflow can commit and push generated assets.

Mitigation: Require human review before push and run the update in a workspace where only intended profile assets can change.

Risk: Image conversion may fall back to npm-installed tooling.

Mitigation: Preinstall and pin trusted image conversion tooling in the execution environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)
- [Skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, JSON]

**Output Format:** [Markdown guidance with command references; generated SVG, WebP, and JSON asset files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GitLab CLI access and environment configuration; may update assets and commit or push generated profile outputs when instructed by the workflow.]

## Skill Version(s):

1.93.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
