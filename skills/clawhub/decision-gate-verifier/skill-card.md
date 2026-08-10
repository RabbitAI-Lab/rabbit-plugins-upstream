## Description:

Decision Gate Verifier provides paid, independent third-party checks that an AI agent's action matched its prior committed claim, returning a PASS or REFUSE receipt anchored on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vaahl-dev](https://clawhub.ai/user/vaahl-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to submit committed agent actions for paid independent verification, receive a PASS or REFUSE receipt, and optionally record that receipt on Base for later audit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a wallet private key for client-side signing and paid Base transactions.

Mitigation: Use a wallet intended for this verifier flow, keep only necessary ETH and USDC available, and review invocation prompts before approving broad audit or transaction-check requests.

Risk: Claim and action data is sent to the external verifier API.

Mitigation: Submit only data appropriate for Soulscore's verifier and confirm that external verification and Base anchoring fit the user's privacy and compliance needs.

Risk: Each verification costs the disclosed USDC fee plus Base gas regardless of PASS or REFUSE.

Mitigation: Confirm expected fees, USDC allowance, and gas cost before use; treat REFUSE receipts as paid verification outcomes.

## Reference(s):

- [Decision Gate product page](https://soulscore.xyz/decision-gate)
- [Soulscore methodology](https://soulscore.xyz/methodology)
- [ClawHub skill listing](https://clawhub.ai/vaahl-dev/skills/decision-gate-verifier)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python code snippets and JSON-like receipt data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call an external verifier API and Base smart contracts when used.]

## Skill Version(s):

0.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
