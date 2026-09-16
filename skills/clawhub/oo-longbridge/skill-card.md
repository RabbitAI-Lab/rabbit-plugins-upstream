## Description:

Longbridge (longbridge.com). Use this skill for Longbridge requests that read, create, or update data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Longbridge through an OOMOL-connected account, including market data lookup, company and news research, account balances, positions, orders, executions, cash flows, and portfolio performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run an unverified remote installer for a finance-account connector.

Mitigation: Install only if OOMOL and the oo CLI distribution path are trusted, and verify or separately inspect the installer before running it.

Risk: The connected Longbridge account may expose financial account data or allow account-state changes through granted scopes.

Mitigation: Connect only the intended Longbridge account and scopes, and require clear user approval before any action that could change account state.

## Reference(s):

- [ClawHub Longbridge skill page](https://clawhub.ai/oomol/skills/oo-longbridge)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Longbridge homepage](https://longbridge.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before submitting oo CLI action requests.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
