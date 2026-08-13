## Description:

Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations, including merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, and other glab commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate GitLab through glab for repository, merge request, issue, CI/CD, release, package, authentication, and administrative workflows. It is most useful for terminal-centric automation and day-to-day GitLab project maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers GitLab write workflows that can modify merge requests, issues, pipelines, releases, packages, and other project state.

Mitigation: Before writes, verify the target GitLab host, account, project, and token scope, and prefer least-privilege bot or service-account tokens.

Risk: Credential and shell identity workflows can cause actions to run under the wrong visible GitLab identity if stale environment variables or shared glab auth are reused.

Mitigation: Clear stale GitLab auth variables, load the intended actor environment explicitly, and run glab auth status plus glab api user checks immediately before write operations.

Risk: The skill includes direct glab api usage that can bypass safer command-specific confirmation paths.

Mitigation: Review API method, endpoint, host, and request fields before running POST, PATCH, PUT, or DELETE calls, especially when confirmation flags are skipped.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vince-winkintel/skills/gitlab-cli-skills)
- [GitLab REST API documentation](https://docs.gitlab.com/api/)
- [GitLab GraphQL documentation](https://docs.gitlab.com/api/graphql/)
- [GitLab Duo CLI documentation](https://docs.gitlab.com/user/gitlab_duo_cli/)
- [NDJSON specification](https://github.com/ndjson/ndjson-spec)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.13.22 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
