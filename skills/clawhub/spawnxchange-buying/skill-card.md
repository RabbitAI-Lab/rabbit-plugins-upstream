## Description:

Use when searching for and purchasing AI-generated code artifacts on SpawnXchange through POST /api/v1/items/{uuid}/acquire, retrieving the delivered artifact and invoice, re-accessing past orders, and leaving item feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to search SpawnXchange listings, confirm price, chain, license, and terms, acquire code artifacts with wallet-backed x402 payments, retrieve invoices and artifacts, and manage purchase records and feedback.

### Deployment Geography for Use:

Global where SpawnXchange is available

## Known Risks and Mitigations:

Risk: The skill can guide an agent through paid SpawnXchange purchases that spend wallet funds.

Mitigation: Confirm item price, chain, license, and terms before any paid request, and cap spend at the listed item price when the wallet supports it.

Risk: Wallet signing keys or payment credentials could be exposed through prompts or logs.

Mitigation: Keep wallet keys in wallet-managed storage and out of prompt context, chat transcripts, logs, and local purchase records.

Risk: Delivered artifacts may contain code that is unsafe or unsuitable to run directly.

Mitigation: Inspect and scan downloaded artifacts before execution or integration.

Risk: Signed download URLs are short-lived bearer credentials that can expose purchased artifacts.

Mitigation: Fetch artifacts promptly, do not save or share signed URLs, and persist only the order ID and local artifact path.

Risk: Local purchase records can reveal buying behavior, wallet linkage, order IDs, and cached artifacts.

Mitigation: Store purchase records in owner-only local state, avoid committing or sharing them, and use encrypted backups if records are backed up.

## Reference(s):

- [Buyer purchase persistence notes](references/purchase-store.md)
- [SpawnXchange skills homepage](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange machine-readable endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP request examples, JSON bodies, and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include paid x402 purchase requests, zero-amount signed requests, public HTTPS fetches, and local purchase-record handling.]

## Skill Version(s):

0.2.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
