## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to discover assigned GitLab issues and merge requests, enforce owner and assignment gates, make scoped changes, manage pipelines, and progress merge requests through review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad autonomous GitLab write access can affect issues, merge requests, branches, labels, pipelines, CI variables, and releases.

Mitigation: Install only for a dedicated, least-privileged GitLab automation account scoped to intended projects, and require human approval for pushes, merges, releases, CI variable changes, and pipeline manipulation.

Risk: Recurring job bootstrap can repeatedly launch autonomous GitLab work.

Mitigation: Keep scheduled execution disabled until a manual run and GitLab authentication are validated, or remove the recurring bootstrap before installation.

Risk: Unpinned CI components can change behavior after installation.

Mitigation: Pin CI components before allowing the skill to run on project CI/CD configuration.

## Reference(s):

- [Documentation Style Guide](references/documentation-style.md)
- [GitLab Default Roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [OpenClaw Creating Skills](https://docs.openclaw.ai/tools/creating-skills)
- [xrow Public Skills Project](https://gitlab.com/xrow-public/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, GitLab CLI/API actions, code changes, and JSON helper output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, jq, and GITLAB_TOKEN; helper scripts emit JSON or fail-closed diagnostics.]

## Skill Version(s):

1.91.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
