## Description:

Check unfamiliar EVM contracts before trading, approving, bridging, or integrating them; reports support decision-making and are not audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bosacks](https://clawhub.ai/user/bosacks)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to review unfamiliar EVM contracts before transactions or integrations, using quick flags or a paid report approved by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid examples can authorize up to $0.05 although each report costs $0.02 USDC.

Mitigation: Set every payment path's hard cap to $0.02 and obtain explicit user approval for each paid report.

## Reference(s):

- [Magneta Contract Risk Service](https://x402.magneta.finance)
- [Coinbase x402 Buyer Quickstart](https://docs.cdp.coinbase.com/x402/buyer/quickstart)
- [ClawHub Release Page](https://clawhub.ai/bosacks/skills/magneta-contract-risk)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, JSON]

**Output Format:** [Structured contract risk report with a score, level, flags, findings, caveats, and decision-support guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results concern a specified EVM chain and contract address; a low score is not an endorsement.]

## Skill Version(s):

0.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
