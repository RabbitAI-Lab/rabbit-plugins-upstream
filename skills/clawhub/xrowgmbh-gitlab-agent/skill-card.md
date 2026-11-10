## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use the agent to review assigned GitLab issues and merge requests, then carry out authorized work under project access and assignment checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports possible GitLab actions and access beyond the stated safeguards, including project changes when owner verification fails; scanner coverage is incomplete.

Mitigation: Review the authorization gates before enabling the skill, start with limited project access, and monitor GitLab changes.

## Reference(s):

- [GitLab Agent release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab Agent maintained source](https://gitlab.com/xrow-public/helm-openclaw/-/tree/main/profile/eugene-harold-krabs/skills/gitlab-agent)
- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [GitLab contribution guide](https://docs.gitlab.com/development/contributing/#make-changes-and-open-a-merge-request)
- [OpenClaw skill creation guide](https://docs.openclaw.ai/tools/creating-skills)
- [uv script guide](https://docs.astral.sh/uv/guides/scripts/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [GitLab work item updates and Markdown reports, with code or configuration changes when assigned.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authenticated GitLab access and the glab, jq, and uv tools; may make GitLab changes such as issue or merge request updates.]

## Skill Version(s):

1.135.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
