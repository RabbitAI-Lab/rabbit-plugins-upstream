## Description:

Batch-profile wallet addresses to identify smart-money or fund labels in a single Nansen CLI call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to screen batches of wallet addresses for smart-money or fund labels, with optional balance data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch calls may consume credits or trigger authorized wallet payments.

Mitigation: Confirm the selected account, wallet authorization, payment policy, and spending limits before running calls or loops.

Risk: An unverified or failed login could lead to unintended anonymous paid access.

Mitigation: Check authentication status, stop on failed or uncertain authentication, and do not switch to anonymous access for this workflow.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-wallet-batch)
- [Nansen CLI browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with a bash code block]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers label filtering, optional balances, and per-address errors.]

## Skill Version(s):

0.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
