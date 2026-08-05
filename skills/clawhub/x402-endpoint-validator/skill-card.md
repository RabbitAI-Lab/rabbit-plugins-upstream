## Description: <br>
Validate x402 endpoints by testing 402 responses, checking Bazaar extension metadata, verifying payment schemas, and confirming .well-known/x402 discovery manifests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marketingkioldenburg](https://clawhub.ai/user/marketingkioldenburg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to validate whether an x402-protected endpoint returns the expected payment challenge, payment fields, Bazaar metadata, and discovery manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The validation examples send test requests to whichever endpoint URL the user provides. <br>
Mitigation: Use endpoints and request bodies intended for testing, and review the target URL before running the curl commands. <br>
Risk: Using the linked external validator may disclose the endpoint URL to that validator service. <br>
Mitigation: Avoid submitting sensitive or private endpoint URLs to external validation services unless disclosure is acceptable. <br>


## Reference(s): <br>
- [x402 Homepage](https://www.x402.org) <br>
- [Agentic Market Validator](https://agentic.market/validate) <br>
- [ClawHub Skill Page](https://clawhub.ai/marketingkioldenburg/skills/x402-endpoint-validator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash commands and validation checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl for the documented endpoint checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
