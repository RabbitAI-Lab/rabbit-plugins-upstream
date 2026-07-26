## Description: <br>
Revolut Business provides a Python CLI for accounts, balances, transactions, counterparties, payments, FX exchange, CSV export, and OAuth token refresh for business accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[christianhaberl](https://clawhub.ai/user/christianhaberl) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect Revolut Business accounts, export transactions, and prepare or execute business banking actions through the Revolut Business API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent live Revolut Business banking authority, including payments, FX exchange, and internal transfers. <br>
Mitigation: Avoid autonomous use for money movement; require human review of amounts, currencies, recipients, and references, and prefer draft payments that must be approved in Revolut. <br>
Risk: Revolut private keys, OAuth tokens, certificates, and config are stored under ~/.clawdbot/revolut/ by default. <br>
Mitigation: Restrict filesystem permissions, protect or vault the directory, limit which agents can read it, and rotate credentials if exposure is suspected. <br>
Risk: CSV export can write sensitive transaction data to user-specified paths. <br>
Mitigation: Review export paths before execution and handle generated CSV files as confidential financial records. <br>
Risk: API access depends on the configured certificate, OAuth redirect domain, and production IP allowlist. <br>
Mitigation: Limit the Revolut certificate and IP allowlist to intended hosts, and revoke or replace credentials when deployment context changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/christianhaberl/skills/revolut-business) <br>
- [Revolut Business API dashboard](https://business.revolut.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, CSV files, Configuration guidance] <br>
**Output Format:** [Terminal text, JSON responses, CSV exports, and Markdown setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3; the skill stores Revolut private key, certificate, tokens, and config under ~/.clawdbot/revolut/ unless REVOLUT_DIR overrides the location.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
