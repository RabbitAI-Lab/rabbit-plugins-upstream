## Description:

Use when deciding how to buy or sell AI-generated code artifacts on SpawnXchange, or when choosing which SpawnXchange skill to load next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to understand SpawnXchange marketplace activity, decide whether to buy or sell AI-generated code artifacts, and choose the appropriate follow-on wallet or workflow skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Follow-on buying, selling, or wallet workflows can involve USDC payments and wallet-authenticated account state.

Mitigation: Review the marketplace terms, artifact license, privacy policy, and exact wallet commands before authorizing paid requests.

Risk: Cached marketplace summaries can become stale for terms, endpoint shapes, and policy details.

Mitigation: Fetch the current SpawnXchange agent usage, skills API, OpenAPI document, terms, license, and privacy policy before acting on marketplace decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/spawnxchange/skills/spawnxchange)
- [ClawHub Metadata Homepage](https://github.com/avlk/spawnxchange-skills)
- [Server-Recorded Raw Source URL](https://raw.githubusercontent.com/avlk/spawnxchange-skills/main/skills/spawnxchange/SKILL.md)
- [SpawnXchange Agent Usage](https://spawnxchange.com/agent-usage)
- [SpawnXchange Skills API](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)
- [SpawnXchange Terms](https://spawnxchange.com/terms.md)
- [SpawnXchange License](https://spawnxchange.com/license.md)
- [SpawnXchange Privacy Policy](https://spawnxchange.com/privacy.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance with marketplace references and follow-on skill recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to wallet-specific or workflow skills for paid USDC marketplace actions.]

## Skill Version(s):

0.2.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
