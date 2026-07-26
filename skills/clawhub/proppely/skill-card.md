## Description: <br>
Connect OpenClaw to Proppely's official MCP and operate a property-management portfolio with scoped OAuth, audited tools, local-file migration, and human approval for protected actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shabsi7700](https://clawhub.ai/user/shabsi7700) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External property-management teams and developers use this skill to connect an agent to Proppely's official MCP, inspect portfolio data, manage rentals, accounting, leasing, maintenance, documents, tenants, owners, and team access, and prepare protected actions for human approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OAuth scopes and organization selection can grant access to property-management data and write/proposal workflows. <br>
Mitigation: Before installing, confirm trust in Proppely and review the requested scopes and selected organization during OAuth. <br>
Risk: Payouts, legal actions, signatures, access changes, and irreversible actions can affect real portfolios. <br>
Mitigation: Use the Proppely approval flow for consequential actions and confirm what is waiting for approval before treating it as executed. <br>
Risk: Local-file migrations can accidentally include secrets, credentials, browser profiles, or unrelated personal files. <br>
Mitigation: Inventory and preview files before upload, map ambiguous folders to the correct destinations, and exclude sensitive or unrelated files. <br>


## Reference(s): <br>
- [Proppely agent setup](https://proppely.com/agents) <br>
- [Proppely MCP documentation](https://proppely.com/mcp) <br>
- [Proppely machine-readable connect guide](https://proppely.com/llms.txt) <br>
- [Proppely MCP discovery metadata](https://proppely.com/.well-known/mcp.json) <br>
- [Proppely ClawHub skill page](https://clawhub.ai/shabsi7700/skills/proppely) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [OAuth setup instructions and operational safeguards; no customer data or API keys are bundled.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
