## Description:

Scan a resolved Polymarket market for wallets exhibiting suspicious trading patterns: fresh funding, single-market focus, extreme ROI, late entry at high prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and researchers use this skill to screen wallets in a resolved Polymarket market for unusual funding, trading concentration, returns, and entry timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research calls, including calls repeated across wallets, may incur paid x402 charges.

Mitigation: Review wallet authorization, payment policy, spending limits, and scan size before running.

Risk: A missing or invalid credential can prevent a scan from completing.

Mitigation: Confirm a selected Nansen API key or browser session and stop if authentication or renewal fails.

Risk: Suspicious-pattern scores alone may be mistaken for proof of insider activity.

Mitigation: Treat flags as screening signals and check the underlying trading and wallet history before drawing conclusions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-polymarket-insider-scan)
- [Nansen CLI browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Analysis, Text, Shell commands]

**Output Format:** [Markdown with wallet scores, flags, and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scores range from 0 to 13; wallets scoring at least 3 are flagged for review.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
