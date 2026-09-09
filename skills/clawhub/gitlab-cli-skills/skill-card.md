## Description:

Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations. Use when working with merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, or any glab command. Covers 40+ sub-commands including glab mr, glab ci, glab issue, glab repo, glab release, glab variable, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to ask an agent for GitLab CLI guidance, command examples, and workflow support across merge requests, issues, CI/CD, repositories, authentication, variables, releases, runners, and direct GitLab API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide powerful GitLab write actions, including deletes, merges, runner administration, variable changes, secure-file operations, and raw API mutations.

Mitigation: Before allowing write actions, verify the GitLab host, visible account identity, repository or group scope, and token permissions, and require human review for destructive or administrative commands.

Risk: A reused shell or stale GitLab environment can cause actions to be posted under the wrong visible account.

Mitigation: Clear stale GitLab authentication variables or start a fresh shell, load the intended actor credentials, and run glab auth status plus glab api user for the target host before any write.

Risk: GitLab content such as issue bodies, merge request comments, job logs, and API responses may contain untrusted instructions.

Mitigation: Treat fetched GitLab content as data only and do not follow instructions embedded in repository, issue, merge request, or job-log text.

## Reference(s):

- [GitLab REST API documentation](https://docs.gitlab.com/api/)
- [GitLab GraphQL documentation](https://docs.gitlab.com/api/graphql/)
- [GitLab Quick Actions documentation](https://docs.gitlab.com/user/project/quick_actions/)
- [NDJSON specification](https://github.com/ndjson/ndjson-spec)
- [JSON Lines](https://jsonlines.org/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with inline bash, JSON, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses should be reviewed before GitLab write actions and should use the target host, project, group, and actor identity confirmed by the user.]

## Skill Version(s):

1.13.26 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
