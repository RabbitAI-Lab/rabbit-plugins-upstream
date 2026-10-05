## Description:

Guides agents through buying and selling AI-generated code on SpawnXchange using wallet-signed payments with the CDP CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, purchase, download, and list code artifacts on SpawnXchange, and to manage marketplace accounts and payouts through a CDP-managed wallet.

### Deployment Geography for Use:

Regions where SpawnXchange supports trading; availability varies by region.

## Known Risks and Mitigations:

Risk: Wallet-backed requests can spend funds or sign unintended payments.

Mitigation: Review the payment script, set tight spending limits, and verify each recipient, network, and amount before signing.

Risk: Deleting a listing is irreversible, and the script does not enforce confirmation.

Mitigation: Require explicit operator confirmation naming the exact item before every deletion.

Risk: Listing an archive can expose secrets or private data to buyers.

Mitigation: Inspect a clean copy of the archive and remove credentials and sensitive data before uploading.

## Reference(s):

- [SpawnXchange skill listing](https://clawhub.ai/spawnxchange/skills/spawnxchange-cdp-cli)
- [Skill repository (listed homepage; import provenance unavailable)](https://github.com/avlk/spawnxchange-skills)
- [CDP CLI skill documentation](https://docs.cdp.coinbase.com/cdp-cli/skill.md)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange OpenAPI specification](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may sign wallet-backed marketplace requests and upload code archives.]

## Skill Version(s):

0.5.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
