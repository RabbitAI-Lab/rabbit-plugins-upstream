## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to let an agent discover assigned GitLab issues and merge requests, verify project access, make scoped changes, manage workflow labels, and deliver merge requests through CI and review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authorizes repeated GitLab writes and some external or public actions without per-action confirmation.

Mitigation: Use a dedicated, least-privileged GitLab account and token limited to projects where autonomous write access is acceptable.

Risk: Fork maintenance, external upstream contribution, CI variable, release, cron, and ci.skip behavior can affect repositories beyond routine issue triage.

Mitigation: Review or remove those behaviors before production use or use in sensitive repositories.

Risk: The security scanner classified the release as suspicious because of broad autonomous GitLab change capabilities.

Mitigation: Review the skill and helper scripts before deployment, then monitor GitLab activity from the dedicated agent account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)
- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/)
- [CI Tools label component](https://ci-tools.xrow.de/Components/label)
- [OpenClaw creating skills guidance](https://docs.openclaw.ai/tools/creating-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, GitLab CLI/API actions, code diffs, merge request text, comments, labels, and JSON from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and jq with GITLAB_TOKEN; helper scripts emit access-gate status text and active work item JSON.]

## Skill Version(s):

1.84.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
