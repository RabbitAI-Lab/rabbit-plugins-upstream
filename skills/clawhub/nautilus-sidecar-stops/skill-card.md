## Description:

Configures and runs a Polymarket stop-loss watcher beside a NautilusTrader live node so hard, trailing, and portfolio exits can run outside Nautilus.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-agent operators use this skill to install and run a sidecar that watches Polymarket positions for a NautilusTrader setup and issues protective exit actions when configured stop policies are breached.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run live trading code with wallet key access.

Mitigation: Use dry-run first, prefer a dedicated low-authority exit wallet, and enable live exits only after verifying the package, policy limits, kill switch, and rollback path.

Risk: Private keys may be exposed if pasted into shell history or broad environment files.

Mitigation: Avoid entering production private keys directly in shell history or shared environment files; use a narrower secret-handling path for the configured exit key.

Risk: The watcher depends on npm wrappers and runtime dependencies.

Mitigation: Install only after reviewing the pinned package and running the setup in a controlled environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/nautilus-sidecar-stops)
- [NautilusTrader Polymarket documentation](https://nautilustrader.io/docs/latest/integrations/polymarket/)
- [NautilusTrader Polymarket examples](https://github.com/nautechsystems/nautilus_trader/tree/develop/examples/live/polymarket)
- [NAUTILUS-SIDECAR.md](artifact/NAUTILUS-SIDECAR.md)
- [BOT.md](artifact/BOT.md)
- [ELIZA-COMPANION.md](artifact/ELIZA-COMPANION.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup and runtime guidance for Node/npm scripts, MCP startup, watcher startup, dry-run operation, and live exit-key configuration.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter, scripts/package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
