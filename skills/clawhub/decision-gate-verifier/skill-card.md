## Description:

Decision Gate Verifier provides paid third-party checks that compare an AI agent action with its prior committed claim and return a signed verdict receipt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vaahl-dev](https://clawhub.ai/user/vaahl-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill when they need an independently checkable receipt showing whether an agent action matched a previously committed policy claim. It is aimed at workflows such as autonomous spending, donations, payouts, and other actions where a third-party PASS, REFUSE, or IN_DOUBT verdict is useful.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The verifier client handles a wallet private key and can sign USDC payment authorizations.

Mitigation: Use a dedicated low-balance wallet and avoid placing high-value private keys in agent-accessible code or configuration.

Risk: Payment signing is automated enough that an agent could authorize payment without sufficient user review.

Mitigation: Inspect payment terms before signing and restrict use to workflows that intentionally use Soulscore's paid decision-gate verifier.

Risk: Claim, action, and observed context are sent to an external verifier service.

Mitigation: Avoid submitting secrets or sensitive operational details unless the workflow has been reviewed for external disclosure.

## Reference(s):

- [ClawHub Decision Gate Verifier listing](https://clawhub.ai/vaahl-dev/skills/decision-gate-verifier)
- [Decision Gate product page](https://soulscore.xyz/decision-gate)
- [Soulscore methodology](https://soulscore.xyz/methodology)
- [Decision Gate proof example](https://soulscore.xyz/proof)

## Skill Output:

**Output Type(s):** [text, json, code, guidance]

**Output Format:** [JSON verdict receipts with Python client usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts are documented as PASS, REFUSE, or IN_DOUBT; use requires USDC on Base and signing payment authorization with a wallet private key.]

## Skill Version(s):

0.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
