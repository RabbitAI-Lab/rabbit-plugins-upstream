## Description: <br>
Checks multi-chain wallet balances across EVM, supported non-EVM chains, and Bitcoin, using Antalpha AI MCP where available with public-data fallback and remembered-address queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bevanding](https://clawhub.ai/user/bevanding) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to look up wallet holdings, total USD value, and saved-address balance summaries across supported chains. It is intended for balance visibility only and does not require seed phrases, private keys, or signing credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local gateway can persist, list, modify, and query saved wallet addresses without built-in authentication or per-user isolation. <br>
Mitigation: Use only in a trusted single-user local setup unless authentication, localhost binding, and per-user or per-session memory isolation are added. <br>
Risk: Saved wallet addresses persist on disk and may reveal sensitive portfolio associations. <br>
Mitigation: Store memory files in a protected location, limit filesystem access, and remove saved addresses when they are no longer needed. <br>
Risk: Balance lookups may send wallet addresses or names to Antalpha MCP and public blockchain or pricing providers. <br>
Mitigation: Tell users which data sources are used for a lookup and never request seed phrases, private keys, or signing credentials. <br>
Risk: Optional MCP credentials can be configured for upstream access. <br>
Mitigation: Keep credentials in environment configuration, avoid logging them, and do not include them in distributable packages. <br>


## Reference(s): <br>
- [README.md](README.md) <br>
- [ClawHub skill page](https://clawhub.ai/bevanding/wallet-balance) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Localized natural language with Markdown balance tables and inline curl commands for gateway calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Redacts wallet addresses in user-visible responses and adds a memory prompt after successful balance lookups.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release evidence, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
