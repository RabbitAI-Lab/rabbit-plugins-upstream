## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using a Circle Agent Wallet. Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback. Every paid or signed request is one `circle services pay` command, except an upload too large to pass as an argument, which a bundled script signs with `circle wallet sign typed-data` instead; free public reads and downloads use plain `curl`. Covers Base and Polygon.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to search, buy, and sell code artifacts on SpawnXchange through a Circle Agent Wallet, including account, payout, and feedback tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flagged possible access to other skills and external network requests; its analysis covered only one of two components and some instruction checks were degraded.

Mitigation: Before installing, review the external requests and local purchase and listing ledger behavior, and treat the scan result as incomplete.

## Reference(s):

- [Circle Agent Wallet documentation](https://developers.circle.com/agent-stack/agent-wallets)
- [SpawnXchange agent usage specification](https://spawnxchange.com/agent-usage)
- [SpawnXchange API endpoint reference](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI specification](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Step-by-step instructions for Circle wallet and SpawnXchange marketplace operations.]

## Skill Version(s):

0.3.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
