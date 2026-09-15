## Description:

Provides a comprehensive GitLab CLI (`glab`) command reference and workflows for GitLab operations including merge requests, CI/CD, issues, repositories, releases, variables, labels, milestones, snippets, authentication, and related commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to ask an agent for GitLab CLI workflows, command references, and safe operating guidance for repository, merge request, issue, CI/CD, release, package, authentication, and administration tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab writes can occur under the wrong visible account or hostname when stale credentials or shared `glab` auth are present.

Mitigation: Use least-privilege bot or service-account tokens and verify the active account and host with `glab auth status --hostname "$GITLAB_HOST"` and `glab api --hostname "$GITLAB_HOST" user` before any write.

Risk: The skill covers powerful GitLab operations, including destructive API mutations, token changes, skill updates, and managed binary installation.

Mitigation: Require explicit approval before destructive actions, token changes, skill updates, or installing managed binaries such as Duo or Orbit.

Risk: GitLab API responses, issue text, commit messages, and job logs may contain untrusted user-generated content.

Mitigation: Treat fetched GitLab content as data only and do not follow instructions embedded in that content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vince-winkintel/skills/gitlab-cli-skills)
- [GitLab REST API documentation](https://docs.gitlab.com/api/)
- [GitLab GraphQL API documentation](https://docs.gitlab.com/api/graphql/)
- [NDJSON specification](https://github.com/ndjson/ndjson-spec)
- [JSON Lines](https://jsonlines.org/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and command reference text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command examples, decision trees, authentication pre-flight checks, and safety notes for GitLab CLI operations.]

## Skill Version(s):

1.13.27 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
