## Description:

Polymarket exit sidecar that helps agents configure hard stops, trailing stops, portfolio stops, heartbeat checks, and watcher or MCP launch commands for place-only Polymarket workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to add exit-risk controls around Polymarket trading flows, especially after place-only skills have opened positions. It provides setup guidance, watcher and MCP entrypoints, and operating cautions for automated protective sells.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The watcher can run long-lived automated trading code that uses a sell-authorizing private key.

Mitigation: Keep dry-run enabled while reviewing behavior, then use a dedicated least-privilege exit key and clear stop or rollback procedures before live use.

Risk: The skill launches an external package through setup, watcher, MCP, npx, and Docker-style paths.

Mitigation: Review the exact @hypelens/hypelens-agent-guard version and install only the intended pinned dependency before running any launch path.

Risk: Private keys can be exposed through shell history, process environments, or Docker environment inspection.

Mitigation: Avoid entering keys in shared shell history, prefer isolated accounts or containers, and handle exit keys through controlled environment or secret-management practices.

Risk: If the guard heartbeat is stale, not ok, or disarmed, position size could increase without active exit protection.

Mitigation: Check the heartbeat before sizing or increasing exposure, and do not increase size when the guard reports stale, failed, or disarmed status.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/polymarket-exits)
- [Nautilus sidecar repository](https://github.com/polyparlay/nautilus-polymarket-stops)
- [NautilusTrader Polymarket documentation](https://nautilustrader.io/docs/latest/integrations/polymarket/)
- [NautilusTrader Polymarket examples](https://github.com/nautechsystems/nautilus_trader/tree/develop/examples/live/polymarket)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JavaScript entrypoints, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and npm; live exit execution depends on an explicit sell-authorizing exit key and dry-run policy settings.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
