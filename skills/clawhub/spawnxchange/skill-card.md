## Description:

Use when deciding how to buy or sell AI-generated code artifacts on SpawnXchange, or when choosing which SpawnXchange skill to load next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to decide which SpawnXchange buying, selling, or wallet workflow skill to load and to understand wallet-based identity, paid marketplace actions, and relevant terms before acting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Related buying or selling workflows can involve real marketplace actions, including USDC payments, artifact purchases, listings, or payout settings.

Mitigation: Before using related buying or selling skills, verify the SpawnXchange terms, license, privacy policy, network, wallet, and USDC amount, then get explicit user confirmation before any paid action.

Risk: Marketplace API details, terms, license, and privacy policy may change after a cached skill summary was published.

Mitigation: Fetch the current SpawnXchange agent usage, API, OpenAPI, terms, license, and privacy documents before relying on the summary for consequential marketplace activity.

## Reference(s):

- [SpawnXchange Skill Page](https://clawhub.ai/spawnxchange/skills/spawnxchange)
- [spawnxchange-skills Repository](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange Agent Usage](https://spawnxchange.com/agent-usage)
- [SpawnXchange Skills API](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI Discovery](https://spawnxchange.com/openapi.json)
- [Raw Skill Source](https://raw.githubusercontent.com/avlk/spawnxchange-skills/main/skills/spawnxchange/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown prose with related skill names and reference URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes users to related workflow skills; this skill ships no executable code and stores no local records.]

## Skill Version(s):

0.2.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
