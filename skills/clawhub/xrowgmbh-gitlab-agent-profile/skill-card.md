## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to keep GitLab profile assets current with monthly contribution statistics across configured projects. It collects GitLab merge request and direct commit data, renders static profile charts, and writes a JSON proof file for the counted records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring authenticated automation can update and push GitLab profile assets without an explicit confirmation step.

Mitigation: Use a limited GitLab token, review the cron schedule, and require a diff or approval step before pushes unless unattended publishing is intentional.

Risk: Generated output paths could write outside the intended profile workspace if configured carelessly.

Mitigation: Keep chart, WebP, records, and workspace paths under the intended repository workspace.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands and generated SVG, WebP, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, python3, and GITLAB_TOKEN; default outputs are written under assets/.]

## Skill Version(s):

1.84.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
