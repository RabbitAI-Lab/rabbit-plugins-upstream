## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to keep a GitLab profile repository updated with monthly contribution charts and proof records. It helps publish static SVG, WebP, and JSON assets that summarize owner and agent contribution activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can repeatedly use GitLab credentials to publish repository changes.

Mitigation: Use a least-privilege GitLab token and review the first generated diff before allowing automated pushes.

Risk: Configured output paths can write generated files outside the intended assets location.

Mitigation: Keep chart, WebP, and records output paths under the intended assets directory.

Risk: A scheduled run could update profile assets before the operator is ready.

Mitigation: Verify the bundled cron remains disabled until scheduled updates are intentionally enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with shell execution steps and generated SVG, WebP, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab CLI authentication and writes profile assets to environment-configured output paths.]

## Skill Version(s):

1.80.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
