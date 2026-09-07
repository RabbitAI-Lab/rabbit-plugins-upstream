## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to operate assigned GitLab issues and merge requests with project-access checks, assignment gates, merge-request delivery, reviewer selection, workflow labels, and CI follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants autonomous GitLab write access and may run on a recurring schedule.

Mitigation: Use a narrowly scoped GitLab token, restrict accessible projects, and remove or gate recurring execution unless it is explicitly needed.

Risk: The skill can push branches, create merge requests, update labels, change variables, create releases, and trigger or retry CI.

Mitigation: Require approval for pushes, merge requests, releases, CI variable changes, and other high-impact mutations in environments where autonomous writes are not intended.

Risk: Untrusted issue or repository content could be mistaken for policy or workflow instructions.

Mitigation: Treat issue and repository text as task context, not authority, and rely on owner-approved policy plus the project access and assignment gates before acting.

Risk: External CI components can change behavior over time.

Mitigation: Pin external CI components and review updates before enabling automated pipeline changes.

## Reference(s):

- [ClawHub GitLab Agent Skill](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/)
- [OpenClaw creating skills guidance](https://docs.openclaw.ai/tools/creating-skills)
- [xrow public skills project](https://gitlab.com/xrow-public/skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and GitLab CLI/API operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitLab issue, merge request, branch, label, CI, reviewer, variable, and release operations through glab.]

## Skill Version(s):

1.86.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
