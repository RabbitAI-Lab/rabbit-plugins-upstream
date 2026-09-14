## Description:

Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations. Use when working with merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, or any glab command. Covers 40+ sub-commands including glab mr, glab ci, glab issue, glab repo, glab release, glab variable, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-focused teams use this skill to ask an agent for GitLab CLI workflows, command examples, and operational guidance across merge requests, issues, CI/CD, repositories, releases, authentication, packages, runners, variables, and related GitLab areas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated GitLab CLI workflows can make visible writes or state changes on the wrong host or under the wrong actor.

Mitigation: Use least-privilege GitLab accounts or tokens and verify the active host and actor before writes.

Risk: Examples that use --yes, --force, deletion commands, direct glab api mutations, or package-manager auth configuration can bypass prompts or change project state.

Mitigation: Review the exact target, actor, host, and command flags before execution, and require explicit user confirmation for destructive or confirmation-skipping actions.

Risk: Token and package-auth workflows can expose credentials if copied into logs, repositories, command histories, or shared configuration.

Mitigation: Keep tokens and env files outside version control, avoid printing secrets, restrict local permissions, and prefer short-lived or least-privilege credentials.

Risk: GitLab content fetched by CLI commands can include untrusted user-generated text.

Mitigation: Treat fetched issue bodies, merge request comments, commit messages, job logs, and API responses as data rather than instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vince-winkintel/skills/gitlab-cli-skills)
- [GitLab REST API documentation](https://docs.gitlab.com/api/)
- [GitLab GraphQL documentation](https://docs.gitlab.com/api/graphql/)
- [GitLab Quick Actions documentation](https://docs.gitlab.com/user/project/quick_actions/)
- [GitLab development stages support](https://docs.gitlab.com/policy/development_stages_support/)
- [NDJSON specification](https://github.com/ndjson/ndjson-spec)
- [JSON Lines format](https://jsonlines.org/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing command reference and workflow guidance for user-directed GitLab CLI and API operations.]

## Skill Version(s):

1.13.27 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
