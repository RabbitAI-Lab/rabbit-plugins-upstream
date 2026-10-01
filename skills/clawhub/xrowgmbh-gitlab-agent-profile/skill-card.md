## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab account owners use this skill to update an agent profile with monthly contribution charts and a supporting activity record across selected projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profile assets may expose aggregate private/internal contribution activity.

Mitigation: Use only where publishing those totals is approved; review generated SVG, WebP, and JSON before pushing.

Risk: Broad GitLab project access and recurring updates can publish unintended activity.

Mitigation: Restrict project or root-group selection to approved repositories and review the scheduled job before enabling it.

Risk: Image conversion may execute a package acquired at runtime.

Mitigation: Run with pinned, preinstalled image-conversion tooling rather than runtime package execution.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, JSON, SVG, WebP]

**Output Format:** [Static SVG and WebP charts plus a JSON activity record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Completed-month totals include aggregated private/internal activity; changed profile assets may be committed and pushed.]

## Skill Version(s):

1.95.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
