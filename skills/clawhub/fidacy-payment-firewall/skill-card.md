## Description: <br>
Use before any payment or money-moving tool call to gate the action against a signed mandate and return a signed, verifiable verdict before money moves. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fidacy](https://clawhub.ai/user/fidacy) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and agent operators use this skill to require a payment-safety decision before an agent authorizes transfers, invoice settlement, checkout, or other money-moving actions. It helps enforce mandates, payee rules, transaction caps, duplicate-invoice checks, and audit-proof collection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This skill becomes part of the payment authorization flow, so incorrect mandates, trusted payees, caps, or mode choices can affect real payment decisions. <br>
Mitigation: Review the mandate, trusted payees, transaction caps, and local or hosted mode before using the skill with real payments. <br>
Risk: Anonymous installs have a limited trial and then fail closed, which can pause payment authorization until activation is completed. <br>
Mitigation: Set FIDACY_ENGINE_API_KEY before production use and relay account activation messages when they appear. <br>
Risk: A money-moving action can still proceed incorrectly if the surrounding agent ignores a DENY verdict or pays without an ALLOW grant. <br>
Mitigation: Wire the skill into the pre-action hook and require operators or executors to stop on DENY and proceed only with a valid ALLOW grant. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fidacy/skills/fidacy-payment-firewall) <br>
- [Fidacy public JWKS](https://api.fidacy.com/.well-known/jwks.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides tool calls that return ALLOW or DENY verdicts, signed grants, mandate details, and audit proofs.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
