## Description:

Polymarket Stops helps agents configure and run a sidecar watcher for hard stops, trailing stops, portfolio stops, heartbeat checks, and protective exits around Polymarket positions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-agent operators use this skill to add stop-loss, trailing-stop, portfolio-stop, and heartbeat workflows to Polymarket agents that can place or monitor positions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The sidecar can run live Polymarket exits with wallet-selling authority.

Mitigation: Keep dry-run enabled until live exit behavior is intentionally approved, and use a dedicated low-value exit signer instead of a main wallet key.

Risk: Private keys or exit signer credentials may be exposed through shell history, process environments, or Docker environment configuration.

Mitigation: Avoid placing private keys directly in shell history or long-lived Docker environment files; use a purpose-limited signer and rotate credentials if exposure is suspected.

Risk: The skill depends on the third-party @hypelens/hypelens-agent-guard package for watcher and MCP behavior.

Mitigation: Inspect the package source and pinned dependency before installation, and scan the installed skill before deployment.

Risk: Protective sells may include Zac builderCode attribution and possible fee implications.

Mitigation: Confirm the attribution and fee behavior is acceptable before switching from dry-run to live mode.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/polymarket-stops)
- [Nautilus Polymarket Stops sidecar](https://github.com/polyparlay/nautilus-polymarket-stops)
- [NautilusTrader Polymarket integration docs](https://nautilustrader.io/docs/latest/integrations/polymarket/)
- [NautilusTrader live Polymarket examples](https://github.com/nautechsystems/nautilus_trader/tree/develop/examples/live/polymarket)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Node/npm setup, watcher startup commands, MCP heartbeat guidance, and dry-run versus live-mode notes.]

## Skill Version(s):

1.0.15 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
