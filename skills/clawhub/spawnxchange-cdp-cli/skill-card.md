## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using a wallet managed by the Coinbase Developer Platform (CDP) CLI. Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback — signing each payment explicitly, which is also what lets it upload an archive up to the marketplace's 10 MB limit rather than only what fits in a command-line argument.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, buy, list, and manage code artifacts on SpawnXchange with a wallet already configured in the CDP CLI. It provides signed-payment steps, account operations, and handling guidance for marketplace transactions.

### Deployment Geography for Use:

Global, subject to marketplace availability in the user's region

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with medium confidence, citing instruction-scope and installation/persistence concerns; scanning was incomplete.

Mitigation: Review the skill instructions and each external request before use, especially requests involving other skills or information sent to the marketplace. Treat the scan as incomplete rather than as a safety determination.

Risk: Marketplace operations can authorize USDC payments, and removing a listing is irreversible.

Mitigation: Check the payment challenge, asset, chain, and operator-chosen spend ceiling before signing; use the matching item ID for deletion confirmation. If settlement is pending, reconcile the transaction before retrying.

## Reference(s):

- [GitHub homepage listed in Clawdis metadata (not verified provenance)](https://github.com/avlk/spawnxchange-skills)
- [CDP CLI skill and wallet setup](https://docs.cdp.coinbase.com/cdp-cli/skill.md)
- [SpawnXchange agent usage specification](https://spawnxchange.com/agent-usage)
- [SpawnXchange API skill reference](https://spawnxchange.com/api/v1/skills)

## Skill Output:

**Output Type(s):** [Markdown guidance, Shell commands, HTTP API calls, Configuration instructions]

**Output Format:** [Markdown instructions with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses operator-supplied wallet, item IDs, chain, spend limit, and listing files.]

## Skill Version(s):

0.5.7 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
