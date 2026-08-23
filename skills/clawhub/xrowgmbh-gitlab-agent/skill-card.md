## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to let an agent discover assigned GitLab issues and merge requests, apply project and assignment gates, and deliver guarded merge request work through GitLab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad recurring authority to change GitLab projects without per-action approval.

Mitigation: Install it only for a dedicated GitLab bot account with the minimum project or group scope and role required, and keep the recurring job disabled until a human explicitly approves it.

Risk: GitLab write operations such as variable or release changes, skipped CI, and manual pipeline control can weaken repository controls if over-permitted.

Mitigation: Remove or forbid variable and release operations unless required, and ensure repository protections and required merge request checks cannot be bypassed by ci.skip or manual pipeline control.

## Reference(s):

- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/)
- [CI Tools label component](https://ci-tools.xrow.de/Components/label)
- [OpenClaw creating skills](https://docs.openclaw.ai/tools/creating-skills)
- [xrow public skills project](https://gitlab.com/xrow-public/skills)
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Markdown]

**Output Format:** [Markdown instructions with bash, GraphQL, JSON, and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GITLAB_TOKEN plus glab and jq; may perform GitLab API calls and project write actions when enabled.]

## Skill Version(s):

1.84.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
