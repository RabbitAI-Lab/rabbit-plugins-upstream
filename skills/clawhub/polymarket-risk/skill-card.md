## Description:

Polymarket Risk helps agents add hard, trailing, and portfolio stop controls around Polymarket positions using a sidecar watcher and heartbeat checks because Polymarket does not provide native stops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-agent operators use this skill to configure Polymarket stop-loss, trailing-stop, portfolio-stop, watcher, and heartbeat workflows after installing place-only Polymarket skills. It is intended to help agents avoid increasing exposure when the risk sidecar is stale, disarmed, or not healthy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automate live sell exits when a wallet key such as AGENT_GUARD_EXIT_PK or EXIT_PK is configured.

Mitigation: Keep dry-run enabled until the wallet, markets, thresholds, signer scope, and intended sell behavior have been reviewed and tested.

Risk: Runtime npx or Docker install flows can execute package code in an environment that may contain live trading credentials.

Mitigation: Review dependencies and installation commands before use, and avoid running install flows with live credentials present.

Risk: Misconfigured or stale watcher and heartbeat state can leave an agent with unprotected positions or allow further sizing when protection is unhealthy.

Mitigation: Require a fresh healthy heartbeat before increasing position size and verify stop, trailing, and portfolio policies before live use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/polymarket-risk)
- [Nautilus Polymarket Stops repository](https://github.com/polyparlay/nautilus-polymarket-stops)
- [NautilusTrader Polymarket integration docs](https://nautilustrader.io/docs/latest/integrations/polymarket/)
- [NautilusTrader Polymarket live examples](https://github.com/nautechsystems/nautilus_trader/tree/develop/examples/live/polymarket)
- [Nautilus sidecar guide](artifact/NAUTILUS-SIDECAR.md)
- [Eliza companion guide](artifact/ELIZA-COMPANION.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup, watcher, dry-run, live-exit, heartbeat, and companion-install guidance for Node and npm based workflows.]

## Skill Version(s):

1.0.7 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
