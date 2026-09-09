## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to operate assigned GitLab issues and merge requests, verify owner-created project access, manage labels and CI state, and prepare merge requests through guarded review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants itself broad unattended GitLab write authority over repositories and recurring work.

Mitigation: Install only with a narrowly scoped GitLab token and only in projects where unattended issue, merge request, label, branch, reviewer, fork, and CI changes are acceptable.

Risk: No-confirmation workflow language can reduce user control over external or irreversible GitLab actions.

Mitigation: Remove or narrow the no-confirmation language, fork self-assignment fallback, and recurring maintenance behavior unless each action class is separately approved and scoped.

Risk: CI controls such as ci.skip pushes, pipeline retries, and pipeline triggering can affect repository delivery safeguards.

Mitigation: Require repository policy review before enabling CI mutations, and keep protected branch and merge controls enforced outside the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab Default Roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Label Component](https://ci-tools.xrow.de/Components/label)
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/)
- [OpenClaw Creating Skills](https://docs.openclaw.ai/tools/creating-skills)
- [xrow Skills Project](https://gitlab.com/xrow-public/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, YAML examples, and Python helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, jq, and GITLAB_TOKEN; helper scripts perform GitLab API calls through glab.]

## Skill Version(s):

1.90.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
