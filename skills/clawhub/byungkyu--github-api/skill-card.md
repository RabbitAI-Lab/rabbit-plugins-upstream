## Description:

Helps agents access GitHub repositories, issues, pull requests, commits, branches, and users through a managed GitHub connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other GitHub users can inspect repositories, search code, manage issues and pull requests, and set up approved automations using their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub account access may expose repositories and other data beyond the task's needs.

Mitigation: Review OAuth scopes and authorize only the accounts and repositories needed; prefer read-only access when possible.

Risk: Writes and automated actions may change or delete GitHub resources.

Mitigation: Confirm the target and effect of each write, hosted function, or automation before enabling it.

Risk: Persistent triggers can forward event data to third-party destinations.

Mitigation: Approve each destination separately and verify what data will be forwarded and for how long.

## Reference(s):

- [ClawHub GitHub skill](https://clawhub.ai/byungkyu/skills/github-api)
- [GitHub REST API documentation](https://docs.github.com/en/rest)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [GitHub event reference](references/github/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with inline commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and authorization for the requested GitHub resources.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release; skill frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
