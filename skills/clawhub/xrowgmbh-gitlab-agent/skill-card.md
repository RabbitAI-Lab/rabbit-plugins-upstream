## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this agent to process GitLab work, inspect assigned issues and merge requests, prepare code changes, and move authorized work through review and closure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious because scanners report autonomous GitLab assignments and workflow changes beyond its stated assigned-work purpose, alongside a possible access-control flaw; the review was partial.

Mitigation: Before enabling automated runs, verify that project membership and authorization checks restrict claims and writes to the intended scope, and use a GitLab token with only the required permissions.

## Reference(s):

- [GitLab Agent skill source](https://gitlab.com/xrow-public/helm-openclaw/-/tree/main/profile/eugene-harold-krabs/skills/gitlab-agent)
- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [GitLab contribution guide](https://docs.gitlab.com/development/contributing/#make-changes-and-open-a-merge-request)
- [OpenClaw skill creation guide](https://docs.openclaw.ai/tools/creating-skills)
- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [Discovery performance notes](references/discovery-performance.md)
- [Documentation style guide](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Markdown reports, GitLab issues and merge requests, GitLab labels and comments]

**Output Format:** [Code and shell operations, Markdown summaries, and GitLab work item updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GITLAB_TOKEN and the glab, jq, uv, and dnf commands. GitLab changes are made under the configured account.]

## Skill Version(s):

1.152.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
