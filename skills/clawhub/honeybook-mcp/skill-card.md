## Description: <br>
This skill helps an agent work with HoneyBook client-portal data for wedding-vendor contracts, invoices, brochures, proposals, payments, and related portal status checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to inspect HoneyBook client-portal sessions, review vendor-shared contracts and invoices, summarize workspace status, and return deep links for signing or payment when explicitly confirmed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: HoneyBook magic-link URLs can create local cached sessions for sensitive contracts, invoices, and payment-related information. <br>
Mitigation: Only provide magic-link URLs to agents you trust for HoneyBook portal access, and treat those URLs like login credentials. <br>
Risk: The skill can surface sensitive vendor portal data, including contract, invoice, and payment-method information. <br>
Mitigation: Install and use it only in contexts where the agent is authorized to access the relevant HoneyBook vendor portal data. <br>
Risk: Signing contracts and paying invoices are consequential portal actions, even when returned as deep links. <br>
Mitigation: Require explicit user confirmation before returning signing or payment links and review the target vendor, contract, invoice, and amount before proceeding. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or plain text responses with HoneyBook portal status details and deep links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include sensitive contract, invoice, payment-method, and portal-session information from HoneyBook.] <br>

## Skill Version(s): <br>
0.4.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
