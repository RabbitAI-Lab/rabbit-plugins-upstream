## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab project maintainers use this skill to let an assigned agent discover, triage, implement, and deliver GitLab issues and merge requests through guarded glab workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad unattended GitLab write actions, including comments, branches, pushes, labels, pipeline actions, and merge request updates.

Mitigation: Install it only for a dedicated low-privilege GitLab bot account scoped to approved projects, and keep the recurring job disabled until a manual run succeeds.

Risk: The skill includes instructions for sensitive GitLab operations such as CI variable management, release creation, self-assignment, and pushes with ci.skip.

Mitigation: Review or remove those instructions before production use, especially in repositories with privileged CI/CD or release workflows.

Risk: Incorrect project access or assignment state could cause the agent to act on work it should not handle.

Mitigation: Use the owner membership security gate, configure GITLAB_AGENT_OWNER, preserve the workflow::forbidden guard, and monitor denied items.

## Reference(s):

- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools label component](https://ci-tools.xrow.de/Components/label)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [OpenClaw creating skills](https://docs.openclaw.ai/tools/creating-skills)
- [xrow public skills project](https://gitlab.com/xrow-public/skills)
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, YAML, JSON, and GraphQL snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authenticated GitLab CLI access via GITLAB_TOKEN with glab and jq installed.]

## Skill Version(s):

1.82.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
