## Description: <br>
Settlement Witness verifies signed SAR v0.1 settlement receipts locally with Ed25519 and RFC 8785 canonicalization, and can optionally request DefaultVerifier-signed receipts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nutstrut](https://clawhub.ai/user/nutstrut) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to verify whether a SAR receipt is cryptographically valid before trusting task-completion, settlement-adjacent, or downstream agent claims. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote receipt issuance sends the task_id, acceptance spec, and claimed output to defaultverifier.com when explicitly requested. <br>
Mitigation: Use local verification only for sensitive outputs, and request remote issuance only with data you are comfortable sending to DefaultVerifier. <br>
Risk: A receipt signed by a verifier_kid missing from the pinned local registry will fail offline verification after key rotation. <br>
Mitigation: Update the skill package or set SAR_KEYS_REGISTRY_PATH only to a registry you deliberately trust. <br>
Risk: A cryptographically valid receipt does not prove legal settlement finality, payment finality, custody of funds, or approval of downstream actions. <br>
Mitigation: Treat verification as signed evidence about the receipt only, and apply separate business, legal, or operational checks before acting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nutstrut/skills/settlement-witness) <br>
- [DefaultVerifier Homepage](https://defaultverifier.com) <br>
- [DefaultVerifier Receipt Explorer](https://defaultverifier.com/verified) <br>
- [DefaultVerifier SAR Public Key Registry](https://defaultverifier.com/.well-known/sar-keys.json) <br>
- [SAR v0.1 Canonicalization and Verification](spec/canonicalization.md) <br>
- [SettlementWitness Network Behavior](EGRESS.md) <br>
- [SettlementWitness Trust Model](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON verifier output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local verification can run offline; optional remote issuance contacts defaultverifier.com only when explicitly requested.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata and CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
