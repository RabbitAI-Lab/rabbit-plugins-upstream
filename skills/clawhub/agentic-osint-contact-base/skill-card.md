## Description: <br>
Method for a verified B2B contact base with registry mapping, per-field proof, no guessed emails, and GDPR-oriented guardrails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and developers use this skill to design a sourced B2B contact research workflow that maps organizations, enriches only proved business contact fields, and prepares a deliverable contact base with suppression and retention controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Professional contact data could be collected without a defined lawful purpose or jurisdictional check. <br>
Mitigation: Define the business purpose and destination jurisdiction before collection, and collect only fields needed for that purpose. <br>
Risk: Unproved or guessed contact values could enter a deliverable contact base. <br>
Mitigation: Require a source URL and confidence for every populated field, and leave unproved fields empty. <br>
Risk: Suppression and retention controls may be declared but not enforced by the operator's implementation. <br>
Mitigation: Implement suppression filtering before delivery and run a retention purge across every run directory. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/alexbloch-ia/skills/agentic-osint-contact-base) <br>
- [Publisher Homepage](https://blochagents.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown instructions with JSON schemas, decision tables, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a method for local contact-base generation; it does not ship or execute a pipeline.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
