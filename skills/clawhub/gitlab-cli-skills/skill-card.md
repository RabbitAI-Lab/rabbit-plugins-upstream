## Description:

Comprehensive GitLab CLI (glab) reference and workflows for merge requests, CI/CD, issues, releases, repositories, authentication, and related operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this reference to find GitLab CLI commands and workflows for common project, collaboration, CI/CD, and administration tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A troubleshooting step prints the full Docker configuration, which can expose saved registry credentials in agent logs.

Mitigation: Replace the full-file printout with a check limited to the intended registry's credential-helper setting; keep credentials out of logs and use least-privilege tokens.

## Reference(s):

- [GitLab CLI configuration and environment variables](https://docs.gitlab.com/cli/configuration/#environment-variables)
- [GitLab REST API](https://docs.gitlab.com/api/)
- [GitLab GraphQL API](https://docs.gitlab.com/api/graphql/)
- [GitLab MCP server](https://docs.gitlab.com/user/model_context_protocol/mcp_server/)
- [GitLab quick actions](https://docs.gitlab.com/user/project/quick_actions/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown reference with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.13.33 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
