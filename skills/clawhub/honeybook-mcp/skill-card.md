## Description: <br>
Honeybook helps an agent use a HoneyBook client-portal MCP server to review vendor contracts, invoices, workspace files, payment methods, and portal deep links for signing or paying. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their agents use this skill to inspect HoneyBook client-portal data across wedding vendors, including contracts, invoices, brochures, proposals, payment methods, and workspace status. It can return portal deep links for signing contracts or paying invoices after explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: HoneyBook magic links and cached sessions can provide access to client-portal data. <br>
Mitigation: Paste magic links only when intentionally authenticating, treat cached sessions like credentials, and clear ~/.honeybook-mcp/sessions.json when access is no longer needed or the device is shared. <br>
Risk: Signing and payment flows can affect vendor contracts or invoices if a user follows returned portal links. <br>
Mitigation: Require explicit confirmation before returning signing or payment deep links, then review the HoneyBook portal page before completing the action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or plain text summaries with HoneyBook portal links and file, workspace, invoice, contract, or payment-method details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Signing and payment links require explicit confirmation; cached HoneyBook sessions should be treated as login credentials.] <br>

## Skill Version(s): <br>
0.4.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
