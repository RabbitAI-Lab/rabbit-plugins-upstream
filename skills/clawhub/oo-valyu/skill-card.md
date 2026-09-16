## Description:

Valyu lets an agent search and read web, academic, financial, and proprietary data through the OOMOL Valyu connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route Valyu search requests through the oo CLI, inspect live action schemas, and handle setup, authentication, connection, credential, or billing failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts in a shell.

Mitigation: Prefer a pinned, verifiable oo CLI release or trusted package manager, and review the installer before running shell-based installation commands.

Risk: Normal use depends on an authenticated OOMOL account, a connected Valyu provider, valid credentials, and available billing credit.

Mitigation: Run setup steps only after matching command failures, use the server-side credential injection path, and avoid handling raw API tokens directly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-valyu)
- [Valyu homepage](https://valyu.ai)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId when actions run.]

## Skill Version(s):

1.0.4 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
