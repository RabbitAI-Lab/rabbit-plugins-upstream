## Description:

Tracks Solana smart-money Jupiter DCA targets and checks their token fundamentals and labeled flows with Nansen research commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and researchers use this skill to identify Solana tokens targeted by smart-money DCA strategies and review token fundamentals and labeled fund flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repeated research calls may trigger x402 wallet payments under existing authorization.

Mitigation: Review wallet spending controls and payment limits before running calls or loops.

Risk: Research commands require a valid selected Nansen API key or browser session.

Mitigation: Check authentication status first and stop if authentication fails; do not retry anonymously.

## Reference(s):

- [Nansen DCA Tracker on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-dca-tracker)
- [Nansen CLI browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [DCA targets, token fundamentals, and labeled net flows depend on Nansen CLI access.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
