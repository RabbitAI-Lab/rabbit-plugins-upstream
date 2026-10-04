## Description:

Guides agents through buying, selling, and managing AI-generated code artifacts on SpawnXchange with a Circle Agent Wallet on Base or Polygon.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find, purchase, download, and list code artifacts, and to manage marketplace orders, payouts, account settings, and feedback through a Circle wallet.

### Deployment Geography for Use:

Region-dependent; marketplace trading may be unavailable in some regions.

## Known Risks and Mitigations:

Risk: Wallet payments and listing fees can spend USDC, and repeating a pending payment can cause a second charge.

Mitigation: Review prices and spending caps before signing; reconcile any pending payment before retrying.

Risk: Anyone with a download or invoice URL may access it while the link remains valid.

Mitigation: Keep these short-lived URLs private; save the purchased file and order ID instead of the URL.

Risk: Uploaded archives become available to buyers and may expose sensitive files or content the seller cannot license.

Mitigation: Inspect the exact archive before uploading; remove secrets and personal data and confirm rights to sell its contents.

Risk: Deleting a listing is irreversible.

Mitigation: Confirm the exact item ID and title with the operator before deletion and retain the source archive.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/spawnxchange/skills/spawnxchange-circle-wallet)
- [Publisher-listed project homepage](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange agent usage specification](https://spawnxchange.com/agent-usage)
- [SpawnXchange API endpoint reference](https://spawnxchange.com/api/v1/skills)
- [Circle Agent Wallet documentation](https://developers.circle.com/agent-stack/agent-wallets)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Marketplace guidance]

**Output Format:** [Markdown with Bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a Circle wallet and USDC on Base or Polygon; users keep local order and listing records.]

## Skill Version(s):

0.3.2 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
