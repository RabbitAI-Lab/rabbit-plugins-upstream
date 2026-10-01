## Description:

Helps agents discover trending Polymarket events, screen markets by activity, and search prediction markets using the Nansen CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and analysts use the Nansen CLI to browse Polymarket events, compare markets by volume or liquidity, and find specific or closed markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research calls use the selected Nansen CLI authentication.

Mitigation: Install only if the agent is intended to use that account; check authentication before research and stop if it fails.

Risk: Authenticated calls may consume credits or trigger wallet-backed payments, particularly in loops.

Mitigation: Set spending limits and bound repeated calls before running research workflows.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nansen-devops/skills/nansen-prediction-markets)
- [Nansen CLI browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Market research guidance]

**Output Format:** [Markdown with inline shell commands and market summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authenticated Nansen CLI access; research calls may consume credits or incur wallet-backed payments.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
