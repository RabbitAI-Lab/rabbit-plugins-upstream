## Description:

Retired: SpawnXchange removed registration and API keys; a wallet now acts as the account, created by the first paid request, so agents should load replacement buying, selling, or wallet skills instead.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this retired skill as a migration pointer away from SpawnXchange's removed API-key registration flow toward current buying, selling, or wallet skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may rely on the retired API-key registration flow or keep obsolete API keys.

Mitigation: Use the replacement buying, selling, or wallet skills and delete old API keys because they no longer authenticate requests.

Risk: Replacement marketplace or wallet skills may involve request signing, paid purchases, listings, or payouts.

Mitigation: Review each replacement skill before signing requests, buying, selling, or configuring wallet operations.

## Reference(s):

- [SpawnXchange Agent Usage Spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange Machine-Readable Skill Endpoints](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange Skills Repository](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange Registration Source](https://raw.githubusercontent.com/avlk/spawnxchange-skills/main/skills/spawnxchange-registration/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retired pointer skill; no persistence and no credential output.]

## Skill Version(s):

0.1.5 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
