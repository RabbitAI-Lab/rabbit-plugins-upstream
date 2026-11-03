## Description:

Reference workflows for GitLab CLI (glab) across merge requests, CI/CD, issues, releases, repositories, authentication, and other GitLab operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this reference to choose and run glab commands for GitLab project work, including collaboration, CI/CD, authentication, configuration, and administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab commands can change project state, permissions, pipelines, or credentials.

Mitigation: Use least-privilege credentials and verify the host, account, and target before changes.

Risk: The governance workflow can persistently upload prompts and tool arguments across repositories.

Mitigation: Review the governance scope and approve it separately before enabling it.

Risk: Downloaded binaries and remote skills may need separate review, and referenced helper scripts are missing from this package.

Mitigation: Review downloaded binaries and remote skill sources separately, and verify helper scripts before relying on them.

## Reference(s):

- [GitLab CLI configuration and environment variables](https://docs.gitlab.com/cli/configuration/#environment-variables)
- [GitLab quick actions](https://docs.gitlab.com/user/project/quick_actions/)
- [GitLab Model Context Protocol server](https://docs.gitlab.com/user/model_context_protocol/mcp_server/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples may act on the selected GitLab host, account, and repository.]

## Skill Version(s):

1.13.37 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
