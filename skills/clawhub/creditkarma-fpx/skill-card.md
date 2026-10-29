## Description:

Query Credit Karma (creditkarma.com) transactions from a shell with the fpx CLI (@fetchproxy/cli) instead of running the creditkarma-mcp server — capture the signed-in session cookie once, then curl the GraphQL transactions endpoint directly. Use when you want Credit Karma transaction data without the MCP, in a script, or on a machine where the MCP isn't installed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to retrieve and paginate transactions from their signed-in Credit Karma account using shell commands, without running the Credit Karma MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples can leave account tokens and financial records exposed in fixed temporary files.

Mitigation: Use an owner-only temporary directory with automatic cleanup; keep tokens and financial records out of logs and shared outputs; approve only the stated domain and cookies, and revoke pairing when finished.

## Reference(s):

- [Credit Karma requests for fpx + curl](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Credit Karma](https://www.creditkarma.com)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/creditkarma-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Tabular text]

**Output Format:** [Markdown instructions with shell commands; JSON responses and tab-separated transaction records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transaction output and session tokens may contain sensitive financial and account data.]

## Skill Version(s):

3.3.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
