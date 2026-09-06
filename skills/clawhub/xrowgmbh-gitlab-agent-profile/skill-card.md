## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to keep a GitLab agent profile repository updated with monthly contribution charts and proof records from GitLab merge request and commit activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run recurring automation that reads GitLab project activity and may commit and push generated profile assets.

Mitigation: Review the cron before enabling it, confirm the target repository and assets paths, and install it only where that GitLab activity and write behavior is intended.

Risk: WebP generation can fall back to npm sharp-cli when local image conversion tools are unavailable.

Mitigation: Prefer ImageMagick or another reviewed local converter so the npm fallback is not used unexpectedly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands; generated SVG, WebP, and JSON asset files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab authentication through GITLAB_TOKEN and the glab CLI; default output paths are under assets/.]

## Skill Version(s):

1.84.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
