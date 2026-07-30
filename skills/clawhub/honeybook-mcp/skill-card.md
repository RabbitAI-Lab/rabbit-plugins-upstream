## Description: <br>
Helps agents work with HoneyBook client-portal data for wedding-vendor contracts, invoices, brochures, proposals, payments, and vendor workspaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to inspect HoneyBook portal workspaces, contracts, invoices, payment methods, and vendor file status, and to produce deep links for signing or payment when explicitly confirmed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may activate the skill for unrelated contract or invoice requests. <br>
Mitigation: Use it only when the request is clearly about HoneyBook portal contracts, invoices, vendors, or workspaces. <br>
Risk: Pasted HoneyBook magic links may create locally cached portal sessions. <br>
Mitigation: Treat magic links and cached sessions as sensitive and avoid using them outside the intended HoneyBook workflow. <br>
Risk: Payment-method metadata and signing or payment links may be exposed to the agent. <br>
Mitigation: Require clear user intent and explicit confirmation before returning signing or payment deep links. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain text guidance with portal status summaries and deep-link references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference locally cached HoneyBook portal sessions and requires explicit confirmation for signing or payment links.] <br>

## Skill Version(s): <br>
0.4.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
