## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to update GitLab profile assets with monthly contribution statistics, charts, and supporting proof records for selected projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support scheduled profile publishing and may commit and push generated asset changes.

Mitigation: Keep the cron disabled unless repeated automated publishing is intended, and review generated changes before pushing.

Risk: Generated proof records may include GitLab project, merge request, commit, label, reviewer, and URL details.

Mitigation: Review the JSON proof file for private project details before publishing it to a public profile repository.

Risk: Configurable output paths can write files outside the intended profile asset location if set carelessly.

Mitigation: Keep chart, WebP, and records outputs under the repository assets directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown instructions plus generated SVG, WebP, and JSON profile assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, python3, and GITLAB_TOKEN; default outputs are written under assets/.]

## Skill Version(s):

1.82.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
