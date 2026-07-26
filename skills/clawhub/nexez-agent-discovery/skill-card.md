## Description: <br>
Use when a user explicitly asks to discover, compare, shortlist, book, buy, or negotiate products or services through Nexez or the Nexez marketplace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nexez](https://clawhub.ai/user/nexez) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search Nexez marketplace listings, compare relevant businesses or offers, and prepare checkout, booking, quote, or negotiation handoffs only after explicit user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches and dry runs may send request details to Nexez. <br>
Mitigation: Review the details being sent and avoid including unnecessary sensitive information. <br>
Risk: Checkout, negotiation, contact sharing, payment handoff, and booking can create side effects. <br>
Mitigation: Use dry-run or validation steps when available and require explicit user approval before any real handoff. <br>
Risk: Changing NEXEZ_BASE_URL changes the destination for requests. <br>
Mitigation: Only set NEXEZ_BASE_URL to a trusted Nexez-compatible endpoint. <br>


## Reference(s): <br>
- [Nexez Agent Discovery on ClawHub](https://clawhub.ai/nexez/skills/nexez-agent-discovery) <br>
- [Nexez Publisher Profile](https://clawhub.ai/user/nexez) <br>
- [Nexez Homepage](https://nexez.ai) <br>
- [Nexez Endpoint Contract](references/endpoint-contract.md) <br>
- [Nexez Discovery Rubric](references/discovery-rubric.md) <br>
- [Nexez Skill Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, shell commands, guidance] <br>
**Output Format:** [Concise Markdown recommendations with structured shortlist details, requested approvals, and optional tool or API request guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include candidate fit rationale, missing information, safe next actions, and approval language before checkout, negotiation, contact, payment, or booking handoffs.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
