## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to discover GitLab work, manage assigned issues and merge requests, and prepare or deliver project changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags that the automation may accept unintended users’ work and modify projects that fail its owner authorization check.

Mitigation: Keep recurring execution and collaborator acceptance disabled until selector ambiguity and writes after failed owner checks are fixed.

Risk: The bundled files do not include deployment-specific configuration, repository instructions, or CI components needed to assess a live installation.

Mitigation: Use a dedicated account scoped to intended projects, define incident and fork-maintenance scope, retain human review for merges, and review the live configuration, repository instructions, and CI components separately.

## Reference(s):

- [GitLab Agent ClawHub release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [Maintained GitLab Agent source](https://gitlab.com/xrow-public/helm-openclaw/-/tree/main/profile/eugene-harold-krabs/skills/gitlab-agent)
- [GitLab user permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [Discovery performance notes](artifact/references/discovery-performance.md)
- [Discovery benchmark data](artifact/references/discovery-benchmark.json)
- [Documentation style guide](artifact/references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown reports, code changes, shell commands, configuration guidance, and GitLab issue or merge request updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May make changes in GitLab projects while processing work.]

## Skill Version(s):

1.130.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
