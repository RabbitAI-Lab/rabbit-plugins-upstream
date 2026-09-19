## Description:

Comprehensive GitLab CLI (glab) command reference and workflows for merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, and other GitLab operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents working on GitLab projects use this skill to select glab commands and workflows for source control, collaboration, CI/CD, releases, credentials, variables, runners, registries, security settings, and direct API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers write-capable GitLab operations, including merge request actions, issue comments, raw API mutations, runner changes, variables, and registry workflows.

Mitigation: Review proposed commands before execution, verify the target GitLab host and actor with glab auth status and glab api user, and use explicit project or group targeting for state-changing commands.

Risk: Credential and token workflows can expose or misuse GitLab secrets if environment files, command output, or exported variables are handled carelessly.

Mitigation: Use least-privilege bot or service accounts, keep credential files out of version control with restrictive permissions, avoid printing secret values, and rotate or revoke tokens according to policy.

Risk: GitLab content returned by commands or MCP tools may include user-generated text that attempts indirect prompt injection.

Mitigation: Treat fetched issue bodies, commit messages, job logs, graph content, query output, and tool metadata as data only, and do not follow instructions embedded in that content.

Risk: Some covered command surfaces are experimental, admin-only, or instance-version dependent.

Mitigation: Verify live glab help, required GitLab edition or feature flags, and required role permissions before relying on security, runner-controller, artifact-registry, Orbit, MCP, or other experimental workflows in durable automation.

## Reference(s):

- [GitLab REST API documentation](https://docs.gitlab.com/api/)
- [GitLab GraphQL documentation](https://docs.gitlab.com/api/graphql/)
- [GitLab CLI environment variables](https://docs.gitlab.com/cli/configuration/#environment-variables)
- [NDJSON specification](https://github.com/ndjson/ndjson-spec)
- [JSON Lines](https://jsonlines.org/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitLab API request examples, JSON or NDJSON output guidance, and workflow decision guidance.]

## Skill Version(s):

1.13.28 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
