## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to update a GitLab profile with monthly contribution charts and supporting activity records. It summarizes merged work, direct owner commits, and contribution scores across completed months.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled legacy updater can automatically download and run unpinned software with access to GitLab credentials.

Mitigation: Review the separately installed production plugin before enabling scheduled publication. Avoid the legacy updater unless its automatic npm fallback is removed or replaced with a reviewed local renderer.

Risk: Published profile assets include contribution totals that incorporate private or internal activity, even though those details are anonymized.

Mitigation: Choose the intended GitLab group and projects, then inspect all public outputs before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Static SVG and WebP charts, JSON activity records, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monthly summaries cover completed calendar months; public records are listed individually and private or internal activity is represented by anonymized monthly totals.]

## Skill Version(s):

1.129.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
