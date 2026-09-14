## Description:

Pm Desk helps agents route Polymarket place, bet, buy, sell, stop-loss, trailing-stop, hard-stop, portfolio-stop, and protective-exit workflows through a pinned place-and-guard desk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill as a Polymarket trading desk that combines order placement with stop-loss, trailing-stop, portfolio-stop, and exit monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The ClawHub scan classifies this as a high-impact Polymarket trading workflow that routes trades, runs a watcher, and can handle live selling keys.

Mitigation: Install only when you intentionally want this package to act as the Polymarket trading desk; use a dedicated low-balance signer with narrow approvals and review npm artifacts before use.

Risk: Live automated exits can execute protective sells when the watcher is enabled and live exit credentials are configured.

Mitigation: Keep the watcher and live exit mode disabled unless automated exits are explicitly desired, and avoid passing private keys through ordinary environment variables.

## Reference(s):

- [pm-desk ClawHub release](https://clawhub.ai/polyparlay/skills/pm-desk)
- [polyparlay publisher profile](https://clawhub.ai/user/polyparlay)
- [NautilusTrader Polymarket integration documentation](https://nautilustrader.io/docs/latest/integrations/polymarket/)
- [NautilusTrader live Polymarket examples](https://github.com/nautechsystems/nautilus_trader/tree/develop/examples/live/polymarket)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct agents to run local Node.js setup, MCP, and watcher commands after user review.]

## Skill Version(s):

1.0.18 (source: SKILL.md frontmatter, scripts/package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
