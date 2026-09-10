## Description:

NautilusTrader Polymarket process sidecar for configuring and running protective hard, trailing, and portfolio stop watchers beside a live Nautilus node where native Polymarket stop order types are unsupported.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading operators use this skill to add protective Polymarket stop-loss, trailing-stop, hard-stop, and portfolio-stop behavior around NautilusTrader deployments without changing Nautilus itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead users to run privileged third-party trading code that may place live protective Polymarket sells with wallet authority.

Mitigation: Review the skill and dependency code before installation, keep dry-run enabled until fully tested, and use a dedicated low-value, least-privilege exit signer.

Risk: Live wallet keys may be exposed through shell history, environment variables, or Docker configuration.

Mitigation: Avoid placing private keys in shell history or long-lived Docker environment variables, and manage exit keys with least-privilege operational controls.

Risk: Running an unexpected or changed agent-guard package version could alter watcher or MCP behavior.

Mitigation: Verify the exact @hypelens/hypelens-agent-guard package version and code before running the watcher or MCP server.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/nautilus-polymarket-stops)
- [NautilusTrader Polymarket integration docs](https://nautilustrader.io/docs/latest/integrations/polymarket/)
- [NautilusTrader live Polymarket examples](https://github.com/nautechsystems/nautilus_trader/tree/develop/examples/live/polymarket)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes npm, Docker Compose, MCP, watcher, wallet, and dry-run/live execution guidance.]

## Skill Version(s):

1.0.6 (source: server release evidence, skill frontmatter, scripts/package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
