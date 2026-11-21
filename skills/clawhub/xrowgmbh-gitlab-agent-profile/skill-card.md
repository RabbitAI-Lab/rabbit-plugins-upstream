## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab profile maintainers use this skill to collect monthly contribution statistics and refresh the profile chart and public proof records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The chart-rendering fallback can automatically download and run an npm package, and the security scan was partial.

Mitigation: Review the renderer installation path and any missing referenced paths before use; avoid running with GitLab credentials available until the fallback is trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions]

**Output Format:** [SVG and WebP charts, JSON proof records, and Markdown instructions with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Charts cover completed calendar months; public proof records omit private project details.]

## Skill Version(s):

1.150.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
