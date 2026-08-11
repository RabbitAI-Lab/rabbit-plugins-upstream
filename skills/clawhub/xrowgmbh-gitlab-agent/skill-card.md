## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab automation operators use this skill to process assigned issues and merge requests, check owner-verified project access, manage workflow labels, prepare branches and merge requests, and follow guarded delivery steps through review and CI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can grant broad unattended write authority in GitLab through a token-bearing automation account.

Mitigation: Install it only on a dedicated GitLab bot account with least-privilege project access, a narrowly scoped token, protected branch rules, and audit logging.

Risk: Recurring execution can repeatedly act on issues, merge requests, labels, CI pipelines, releases, variables, and forks without interactive confirmation.

Mitigation: Require human approval around recurring execution, releases, CI/CD variables, fork maintenance, and writes outside the directly assigned issue or merge request.

Risk: The skill depends on correct owner and assignment gating before reading or changing GitLab project objects.

Mitigation: Keep the owner membership check and assignment gate enabled, fail closed when membership evidence is incomplete, and stop work when the security-check script marks an object forbidden.

## Reference(s):

- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [CI Tools label component](https://ci-tools.xrow.de/Components/label)
- [OpenClaw creating skills guidance](https://docs.openclaw.ai/tools/creating-skills)
- [xrow public skills project](https://gitlab.com/xrow-public/skills)
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, GitLab CLI examples, JSON configuration, and code or configuration changes as needed for assigned work.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to use glab and jq to inspect and update GitLab issues, merge requests, branches, labels, comments, CI pipelines, variables, releases, and forks.]

## Skill Version(s):

1.81.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
