## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to triage assigned GitLab work and prepare guarded code changes and merge requests, with project access and assignment checks guiding which work proceeds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automation may accept unintended contributors or modify a project after its authorization check denies access.

Mitigation: Keep recurring automation disabled until collaborator selectors resolve to unique intended identities and denied projects receive no writes. Limit credentials to approved repositories, decide whether automatic self-merging is acceptable, and verify live permissions and repository policies.

## Reference(s):

- [GitLab Agent release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab Agent issue and feature contribution page](https://gitlab.com/xrow-public/helm-openclaw/-/tree/main/profile/eugene-harold-krabs/skills/gitlab-agent)
- [GitLab user permissions](https://docs.gitlab.com/user/permissions/#default-roles)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown instructions, Python scripts, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GITLAB_TOKEN and the glab, jq, and uv command-line tools.]

## Skill Version(s):

1.127.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
