## Description:

Provides GitLab CLI (glab) command reference and workflows for merge requests, CI/CD, issues, releases, repositories, authentication, and project administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and run glab commands for GitLab projects, including merge requests, pipelines, issues, releases, and administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab writes or privileged workflows could affect the wrong host, repository, or actor.

Mitigation: Require explicit host, repository, and actor confirmation before writes, token, runner, governance, skill-update, or transcript-sync workflows.

Risk: Examples may reference scripts or support files that are not bundled with this release.

Mitigation: Verify referenced files exist and inspect them before using those examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vince-winkintel/skills/gitlab-cli-skills)
- [GitLab REST API documentation](https://docs.gitlab.com/api/)
- [GitLab GraphQL documentation](https://docs.gitlab.com/api/graphql/)
- [GitLab CLI configuration documentation](https://docs.gitlab.com/cli/configuration/#environment-variables)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance only; sensitive GitLab commands are documented but not automatically executed.]

## Skill Version(s):

1.13.31 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
