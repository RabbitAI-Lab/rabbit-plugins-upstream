## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to keep a GitLab agent profile updated with monthly contribution statistics, generated profile charts, and a public proof record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can collect GitLab activity across the configured group and publish generated profile assets.

Mitigation: Use a least-privilege GitLab token, limit the root group or project list, and review the generated JSON proof file before publishing.

Risk: The bundled recurring schedule can run the update routine repeatedly if enabled.

Mitigation: Keep the schedule disabled unless recurring publication is required, and review the schedule settings before enabling automation.

Risk: The WebP conversion fallback can invoke npm sharp-cli during automated use.

Mitigation: Remove or pin the npm sharp-cli fallback before unattended runs, or provide a trusted local conversion backend.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown instructions plus generated SVG, WebP, and JSON proof files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, python3, and GITLAB_TOKEN; WebP conversion depends on an available image conversion backend.]

## Skill Version(s):

1.91.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
