## Description:

LYGO Mint Walkthrough is an interactive tutorial for minting, verifying, creating anchor snippets, and optionally backfilling local ledger records with standard-library SHA-256 hashing and no automated posting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Developers and skill authors use this skill to walk through a local mint, verify, and anchor-snippet flow for LYGO-style packs while keeping the human responsible for any publication step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected pack files may contain secrets or sensitive content that should not be minted or referenced.

Mitigation: Review pack contents before minting and avoid using the walkthrough on files that contain credentials, private keys, passwords, or confidential material.

Risk: Consent-gated ledger writes can store absolute file paths and anchor identifiers in the skill state directory.

Mitigation: Use write operations only when local recordkeeping is intended, and inspect or remove state files before sharing the skill directory or workspace.

Risk: Anchor snippets are public receipts and can still reveal titles, hashes, timestamps, and tool metadata.

Mitigation: Review snippet text before manually posting it and choose non-sensitive titles or anchor identifiers.

## Reference(s):

- [Security Notes](references/SECURITY.md)
- [OpenClaw Homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-mint-walkthrough)
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-mint-walkthrough)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [JSON responses, plain text guidance, Markdown examples, and anchor snippet text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write consent-gated local ledger and canonical metadata files under the skill state directory.]

## Skill Version(s):

1.0.0 (source: frontmatter, claw.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
