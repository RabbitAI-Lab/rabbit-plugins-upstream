## Description:

Guides analysis of a Polymarket wallet's trades, profit and loss, and market context using Nansen.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to inspect a Polymarket trader's wallet activity, compare profit and loss across markets, and understand what the trader is betting on.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repeated research calls can consume credits or trigger wallet payments under the configured payment policy.

Mitigation: Confirm credentials, wallet authorization, payment policy, and spending limits before issuing calls or running loops.

Risk: Cached authentication status may not establish that a selected credential remains usable.

Mitigation: Confirm a selected API key or browser session, check authentication status, and stop on authentication failure rather than switching to anonymous access.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-polymarket-trader-profile)
- [Nansen CLI browser login platform scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Analysis]

**Output Format:** [Markdown with bash commands and narrative analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a Polymarket wallet address; Nansen research calls may consume credits or trigger authorized payments.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
