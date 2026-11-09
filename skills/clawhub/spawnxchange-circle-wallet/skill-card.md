## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using a Circle Agent Wallet. Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback. Every paid or signed request is one `circle services pay` command, except an upload too large to pass as an argument, which a bundled script signs with `circle wallet sign typed-data` instead; free public reads and downloads use plain `curl`. Covers Base and Polygon.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI agents use this skill to find, buy, download, publish, and manage code artifacts on SpawnXchange using a Circle Agent Wallet on Base or Polygon.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Purchases and listings authorize USDC payments, and a completed payment may be irreversible.

Mitigation: Inspect the requested amount and terms, set a narrow spend cap, and use the upload preflight before choosing to execute.

Risk: The security scan had partial coverage and does not guarantee safety; the skill makes external requests to SpawnXchange and wallet services.

Mitigation: Review the commands and verify that the request destinations fit your needs and are trusted before running them.

Risk: Temporary download and invoice URLs act as bearer credentials while valid.

Mitigation: Download directly, do not log, store, or share the URLs, and retain the order ID to request fresh links.

## Reference(s):

- [Declared project homepage](https://github.com/avlk/spawnxchange-skills)
- [Circle Agent Wallet documentation](https://developers.circle.com/agent-stack/agent-wallets)
- [SpawnXchange agent usage specification](https://spawnxchange.com/agent-usage)
- [SpawnXchange API endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI specification](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stepwise purchase and listing workflows with spend limits and preflight guidance.]

## Skill Version(s):

0.3.9 (source: frontmatter; confirmed by release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
