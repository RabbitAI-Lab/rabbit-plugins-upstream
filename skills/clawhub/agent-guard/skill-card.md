## Description:

agent-guard helps agents and operators configure hard stops, trailing stops, portfolio stops, and heartbeat checks for Polymarket and optional Hyperliquid positions using a watcher sidecar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, trading-agent builders, and operators use this skill to add stop-loss, trailing-stop, portfolio-exit, and heartbeat workflows around Polymarket and optional Hyperliquid automation. It is intended as a protective companion after place-only trading skills rather than as an entry or betting skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live private-key trading authority can allow the watcher to place fund-affecting protective exits.

Mitigation: Review the external npm package, start in dry-run, and use only a dedicated limited wallet or delegated signer.

Risk: Providing EXIT_PK or AGENT_GUARD_EXIT_PK can intentionally enable real protective exits.

Mitigation: Do not set live exit-key environment variables unless live exit automation has been approved for that wallet and strategy.

Risk: Credentials or private keys could be exposed through unsafe operational handling.

Mitigation: Avoid primary wallets and do not commit, paste, or log private keys.

## Reference(s):

- [NautilusTrader Polymarket live examples](https://github.com/nautechsystems/nautilus_trader/tree/develop/examples/live/polymarket)
- [NautilusTrader Polymarket integration docs](https://nautilustrader.io/docs/latest/integrations/polymarket/)
- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/agent-guard)
- [Publisher profile](https://clawhub.ai/user/polyparlay)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that install or run npm-based watcher and MCP processes.]

## Skill Version(s):

1.0.25 (source: server release evidence, SKILL.md frontmatter, scripts/package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
