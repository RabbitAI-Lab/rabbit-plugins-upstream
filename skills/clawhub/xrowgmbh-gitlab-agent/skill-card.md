## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to let an agent manage assigned GitLab issues and merge requests, including gated project access checks, branch and merge request work, pipeline follow-up, labels, comments, and deterministic reviewer selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform unattended GitLab write actions, including issue, branch, merge request, label, reviewer, pipeline, and possible merge operations.

Mitigation: Use a narrowly scoped service account and enable it only for intended projects after a manual test run.

Risk: Recurring execution can repeatedly act with the configured GitLab token if enabled too early.

Mitigation: Keep the recurring job disabled until behavior has been tested on low-risk projects and project-level change-control expectations are reviewed.

Risk: The skill instructs pushes with ci.skip and later manual pipeline starts, which may not match every team's CI policy.

Mitigation: Review the ci.skip and pipeline-start behavior against team rules before production use.

## Reference(s):

- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/)
- [CI Tools label component](https://ci-tools.xrow.de/Components/label)
- [OpenClaw creating skills](https://docs.openclaw.ai/tools/creating-skills)
- [xrow public skills project](https://gitlab.com/xrow-public/skills)
- [Documentation style guidance](references/documentation-style.md)
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, GitLab updates, JSON helper output, and code changes when work requires them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GitLab CLI/API actions through glab and jq with GITLAB_TOKEN authentication.]

## Skill Version(s):

1.93.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
