## Description:

Clusters and attributes related wallets using funding chains, shared signers, and CEX deposit patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to investigate wallet ownership and relationships across supported chains, compare candidate clusters, and document attribution signals with confidence levels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated research calls, particularly loops and traces, may consume credits or trigger wallet-funded x402 payments.

Mitigation: Review credentials, wallet authorization, payment policy, and spending limits before running calls; constrain traces and confirm each newly discovered address before expanding.

Risk: Weak relationship signals may lead to incorrect wallet-owner attribution.

Mitigation: Report the underlying signals and confidence, exclude single-signal matches, and stop expanding low-confidence clusters.

## Reference(s):

- [Wallet Attribution Reference](REFERENCE.md)
- [Nansen CLI Browser Login Platform Scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)
- [ClawHub Skill Release](https://clawhub.ai/nansen-devops/skills/nansen-wallet-clustering)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with wallet attribution entries and bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Attribution entries identify address, owner, confidence, signals, and role.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
