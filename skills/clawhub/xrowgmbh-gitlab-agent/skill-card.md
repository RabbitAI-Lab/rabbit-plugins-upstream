## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to operate assigned GitLab issues and merge requests through guarded project access checks, assignment checks, label management, pipeline handling, reviewer selection, and merge request delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unattended write-capable GitLab authority can mutate issues, merge requests, labels, reviewers, branches, pipelines, CI/CD variables, releases, and external upstream contributions outside the intended workflow.

Mitigation: Install with a dedicated least-privilege GitLab bot account limited to intended projects, and gate or remove write actions that should require human approval.

Risk: Recurring automation and external upstream contribution behavior can continue activity or operate beyond expected project boundaries.

Mitigation: Enable recurring operation only when continuous automation is intended, and require explicit upstream URLs plus review of external contribution behavior before use.

Risk: ci.skip pushes, CI/CD variable commands, release commands, and pipeline triggers can affect quality and release controls.

Mitigation: Require human review or policy controls for ci.skip, CI/CD variable, release, and pipeline-trigger behavior in protected workflows.

## Reference(s):

- [ClawHub GitLab Agent release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/)
- [CI Tools label component](https://ci-tools.xrow.de/Components/label)
- [OpenClaw creating skills](https://docs.openclaw.ai/tools/creating-skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, glab, Git, YAML, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, jq, and GITLAB_TOKEN; helper scripts emit status text or JSON for access checks, active work listing, and reviewer selection.]

## Skill Version(s):

1.84.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
