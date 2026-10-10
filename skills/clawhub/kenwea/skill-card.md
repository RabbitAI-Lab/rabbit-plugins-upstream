## Description:

Check an npm package or file in a no-network sandbox before installing it, and browse, sell or buy digital products on the Kenwea marketplace over MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenwea-protocol](https://clawhub.ai/user/kenwea-protocol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect package install-time behavior before installation and, when requested, browse or trade digital products on Kenwea.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned npm tool can execute unexpected code.

Mitigation: Review the tool before use and pin the Kenwea CLI version before running npx.

Risk: Marketplace actions can spend wallet funds.

Mitigation: Require the user's explicit request for each purchase or bid and review marketplace permissions before use.

Risk: A marketplace API key could be exposed in chat or project files.

Mitigation: Store the key only in a secret manager, not chat or committed files.

## Reference(s):

- [Kenwea MCP documentation](https://www.kenwea.com/docs/mcp)
- [Kenwea verification guidance](https://www.kenwea.com/verify)
- [Kenwea homepage](https://www.kenwea.com)
- [Kenwea ClawHub skill](https://clawhub.ai/kenwea-protocol/skills/kenwea)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and MCP usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes package-check results and marketplace actions for the user.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
