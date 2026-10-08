## Description:

Provides GitLab CLI command references and workflows for merge requests, CI/CD, issues, releases, repositories, and administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan and perform GitLab tasks through glab, including reviews, pipeline management, issue tracking, and repository administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes may target the wrong GitLab host, project, or visible account.

Mitigation: Check the target host and project, then verify the authenticated account immediately before each write.

Risk: Administrative, token, package deletion, global install, and forced commands can have broad or irreversible effects.

Mitigation: Review the specific command and scope before execution; use least-privilege credentials and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vince-winkintel/skills/gitlab-cli-skills)
- [GitLab REST API documentation](https://docs.gitlab.com/api/)
- [GitLab GraphQL documentation](https://docs.gitlab.com/api/graphql/)
- [GitLab CLI environment variables](https://docs.gitlab.com/cli/configuration/#environment-variables)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may change GitLab resources when executed.]

## Skill Version(s):

1.13.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
