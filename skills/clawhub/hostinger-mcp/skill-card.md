## Description: <br>
Operational guide for managing Hostinger VPS, hosting, domains, DNS, Reach, and billing through the official Hostinger MCP server across one or more Hostinger accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benkalsky](https://clawhub.ai/user/benkalsky) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, operators, and site owners use this skill to configure and operate Hostinger MCP tools for infrastructure, DNS, domain, hosting, email marketing, and billing tasks. It is especially useful when an agent needs account-aware, confirmation-gated guidance before read, write, destructive, or money-spending Hostinger actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connected MCP server can exercise full Hostinger account authority through the configured account token. <br>
Mitigation: Use separate tokens per account, load only the needed category binary, keep user-level MCP persistence in mind, and require explicit confirmation before any write, destructive, or billing-related action. <br>
Risk: Money-spending and destructive Hostinger operations can create charges, change subscriptions, delete resources, or wipe VPS data. <br>
Mitigation: Confirm the account, target resource, intended action, expected impact, and cost before spending actions; double-confirm destructive actions and verify recovery points when data could be lost. <br>
Risk: Multiple Hostinger accounts can expose similar resource names or IDs that are not interchangeable across MCP connections. <br>
Mitigation: Identify the account before every operation, tag cross-account read results by account, and stop to ask the user when ownership or target account is unclear. <br>
Risk: API tokens and stored OAuth credentials can expose broad account access if printed, reused, or persisted unexpectedly. <br>
Mitigation: Never print tokens in responses, prefer per-account API tokens for multi-account use, and direct users to hPanel for credential management. <br>


## Reference(s): <br>
- [Installation - Hostinger MCP Server](references/installation.md) <br>
- [Tools Catalog - Hostinger MCP](references/tools-catalog.md) <br>
- [Workflows - VPS](references/workflows-vps.md) <br>
- [Official Hostinger MCP server](https://github.com/hostinger/api-mcp-server) <br>
- [Hostinger API documentation](https://developers.hostinger.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and confirmation blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Operational guidance emphasizes read-only defaults, smallest-needed MCP tool loading, account verification, and explicit confirmation for write, destructive, and billing-related actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
