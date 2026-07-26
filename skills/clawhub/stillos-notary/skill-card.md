## Description: <br>
Stillos Notary helps agents verify machine-checkable claims against external sources such as GitHub, on-chain transactions, Kalshi markets, HTTP/JSON endpoints, and price feeds, then returns Ed25519-signed, hash-chained receipts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stillmarcus24](https://clawhub.ai/user/stillmarcus24) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill when a claim needs to be checked against machine-readable external state and preserved as a signed receipt for later review. It is suited to settlement disputes, agent-to-agent handoffs, and other workflows where receipt integrity alone is not enough. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Claim text and an agent identifier may be sent to the hosted StillOS Notary service. <br>
Mitigation: Use the hosted verifier only for claim text and identifiers you are comfortable sending to that service. <br>
Risk: The pip install path relies on an external Python package that is not bundled in this artifact. <br>
Mitigation: Review the external package before using the pip install path; the bundled offline verifier is local and read-only. <br>
Risk: Offline verification proves a receipt is unforged and unmodified, but it does not re-check whether the underlying claim is currently true. <br>
Mitigation: Use the live resolver when you need current claim truth; use the offline verifier for receipt integrity checks. <br>


## Reference(s): <br>
- [Stillos Notary ClawHub page](https://clawhub.ai/stillmarcus24/skills/stillos-notary) <br>
- [Claim vocabulary specification](https://nolawealthfinancial.com/evidence/notary-doctrine/claim-vocabulary-spec.json) <br>
- [Notary API base endpoint](https://nolawealthfinancial.com/notary) <br>
- [Notary claim-verdict endpoint](https://nolawealthfinancial.com/notary/claim-verdict) <br>
- [Notary export endpoint](https://nolawealthfinancial.com/notary/export) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration, text] <br>
**Output Format:** [Markdown with inline shell commands, code examples, HTTP examples, and JSON verification output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for hosted claim verification and local receipt verification; live claim checks call the external notary service.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
