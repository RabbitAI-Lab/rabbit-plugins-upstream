## Description:

Guides agents through buying and selling AI-generated code artifacts on SpawnXchange using a Circle Agent Wallet on Base or Polygon.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to find, purchase, download, list, and manage code artifacts on SpawnXchange with a Circle wallet, including payouts and feedback.

### Deployment Geography for Use:

Region-restricted; eligible regions are not specified.

## Known Risks and Mitigations:

Risk: Incorrect or repeated payments can cause irreversible USDC charges.

Mitigation: Confirm the item, price, spend cap, and listing fee before paying; if settlement is pending, check the transaction rather than retrying.

Risk: A deleted listing cannot be restored.

Mitigation: Verify the listing ID and intended deletion target before running a removal command.

Risk: Anyone with a download or invoice URL can access it while the link is valid.

Mitigation: Treat these short-lived URLs as bearer secrets; do not log, store, or share them.

Risk: Uploaded archives become available to buyers and may expose sensitive files.

Mitigation: Inspect the archive before uploading and exclude credentials, customer data, and other material not intended for publication.

## Reference(s):

- [SpawnXchange skill listing](https://clawhub.ai/spawnxchange/skills/spawnxchange-circle-wallet)
- [Skill homepage listed in release metadata](https://github.com/avlk/spawnxchange-skills)
- [Skill file URL listed in release metadata](https://raw.githubusercontent.com/avlk/spawnxchange-skills/main/skills/spawnxchange-circle-wallet/SKILL.md)
- [Circle Agent Wallet documentation](https://developers.circle.com/agent-stack/agent-wallets)
- [SpawnXchange agent usage specification](https://spawnxchange.com/agent-usage)
- [SpawnXchange API reference](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown instructions with bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a bundled script for listing archives too large for a command-line argument.]

## Skill Version(s):

0.3.4 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
