## Description:

DumplingAI helps agents search catalog data, read account and usage information, and run DumplingAI capabilities through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect DumplingAI balances, transactions, usage, request logs, catalog metadata, and to run DumplingAI capabilities through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags the generic run action as potentially state-changing or credit-consuming despite mostly read-oriented positioning.

Mitigation: Require explicit user confirmation and schema review before using run, especially for managed provider endpoints.

Risk: Actions depend on an authenticated OOMOL-connected DumplingAI account and may fail when credentials, scopes, or billing are unavailable.

Mitigation: Use the documented setup and troubleshooting flow only after command failures, and resolve connection, scope, or credit issues before retrying.

## Reference(s):

- [ClawHub DumplingAI skill](https://clawhub.ai/oomol/skills/oo-dumplingai)
- [DumplingAI homepage](https://www.dumplingai.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON payloads and command output from oo connector actions.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
