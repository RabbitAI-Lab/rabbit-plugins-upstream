## Description:

Guides agents in accessing Crown Town Compost customer portal data and account actions using authenticated curl requests without the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Crown Town Compost customers and their authorized agents use the skill to review pickups, invoices, and upcoming service, or request account changes through the customer portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated actions can skip service or change account details and requests.

Mitigation: Require explicit approval before skips, account updates, support or missed-pickup submissions, and cancellation requests; verify changes afterward.

Risk: Stored session cookies and portal credentials can expose a customer account.

Mitigation: Protect credentials, restrict cookie-jar permissions, and delete the cookie jar after use.

Risk: Billing exports and invoice links can expose private financial information.

Mitigation: Limit access to billing CSVs and invoice links, and avoid sharing them publicly.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)
- [Crown Town Compost portal](https://portal.crowntowncompost.com)
- [Portal endpoint reference](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include portal responses and billing CSV exports when commands are run.]

## Skill Version(s):

1.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
