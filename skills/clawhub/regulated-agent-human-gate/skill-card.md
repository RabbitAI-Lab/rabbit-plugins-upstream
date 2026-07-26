## Description: <br>
Build, review, or test KYA (Know Your Agent) human-gate controls for AI agents that prepare or execute regulated financial actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, reviewers, and regulated-finance teams use this skill to design, review, and test human approval gates for agent-prepared payments, withdrawals, stablecoin off-ramps, lending workflows, onboarding, identity changes, account-control changes, and MCP execution chains. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill addresses regulated-finance agent controls, where incorrect authorization or missing controls could allow unsafe financial actions. <br>
Mitigation: Implement deterministic policy evaluation, trusted audit storage, key management, legal and compliance review, and fail-closed behavior before deployment. <br>
Risk: The bundled HMAC receipt helper is a reference and testing aid, not a production authorization service. <br>
Mitigation: Use a managed KMS or HSM for production signing, rotate keys by key ID, authenticate callers, and combine nonce consumption with an idempotent execution record. <br>
Risk: Approvals can become unsafe if they are applied to mutable actions or reused after expiry or replay. <br>
Mitigation: Freeze and hash the final action, bind decisions and receipts to that hash, verify and consume each receipt once, and reject mutation, expiry, replay, tenant mismatch, policy mismatch, and signer mismatch. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/regulated-agent-human-gate) <br>
- [Human Gate Policy](artifact/resources/human-gate-policy.md) <br>
- [Risk Taxonomy](artifact/resources/risk-taxonomy.md) <br>
- [Identity Verification Routing](artifact/resources/identity-verification-routing.md) <br>
- [Audit Evidence Checklist](artifact/resources/audit-evidence-checklist.md) <br>
- [Agent Evaluation Guide](artifact/resources/agent-evaluation-guide.md) <br>
- [Regulated Finance Use Cases](artifact/resources/regulated-finance-use-cases.md) <br>
- [MCP Tool Contract Example](artifact/templates/mcp-tool-contract-example.json) <br>
- [Policy Template](artifact/templates/policy-template.yaml) <br>
- [Reference Receipt Helper](artifact/scripts/kya_receipt.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON/YAML schemas, example commands, and reference code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes policy, audit, evaluation, MCP contract, and receipt-helper materials for review before implementation.] <br>

## Skill Version(s): <br>
0.2.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
