## Description:

Comprehensive GitLab CLI (glab) command reference and workflows for merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, and related GitLab operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to plan and produce GitLab CLI workflows, shell commands, API calls, and configuration steps for repository, issue, merge request, CI/CD, release, and administration tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags token handling as suspicious because one example pulls a stored GitLab token into Python for raw API calls.

Mitigation: Avoid plaintext token extraction unless the token handling path has been reviewed and contained; prefer least-privilege credentials and avoid printing or committing tokens.

Risk: Agents can perform GitLab writes against the wrong host or visible account when shell authentication state is stale or shared.

Mitigation: Verify the target host and account with glab auth status and glab api user immediately before any write operation.

Risk: Destructive commands using confirmation-bypass flags such as --yes or force-style options can remove repositories, packages, images, or other GitLab state.

Mitigation: Require explicit target review for destructive commands and avoid confirmation-bypass flags until resource IDs, scopes, and intended effects are confirmed.

## Reference(s):

- [GitLab REST API documentation](https://docs.gitlab.com/api/)
- [GitLab GraphQL documentation](https://docs.gitlab.com/api/graphql/)
- [GitLab Quick Actions documentation](https://docs.gitlab.com/user/project/quick_actions/)
- [GitLab development stages support](https://docs.gitlab.com/policy/development_stages_support/)
- [NDJSON specification](https://github.com/ndjson/ndjson-spec)
- [JSON Lines format](https://jsonlines.org/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab; generated command guidance may include authenticated GitLab API calls and write operations.]

## Skill Version(s):

1.13.25 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
