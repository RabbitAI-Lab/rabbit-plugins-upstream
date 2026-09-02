## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to keep GitLab profile assets current with monthly contribution statistics, generated charts, and proof records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use GitLab credentials and may access private GitLab projects.

Mitigation: Run it with a restricted GitLab token and an explicit project list before installing it in accounts with sensitive repositories.

Risk: The skill can update generated files and supports a workflow that commits and pushes changed assets.

Mitigation: Keep output paths under the intended assets directory and require review before pushing generated changes.

Risk: The WebP conversion path can invoke an unpinned npm fallback package.

Mitigation: Prefer a trusted local converter, or pin and review the npm package source before allowing that fallback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated SVG, WebP, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GitLab CLI credentials and configurable output paths for profile assets.]

## Skill Version(s):

1.84.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
