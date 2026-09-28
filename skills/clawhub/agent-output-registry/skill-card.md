## Description:

Registers AI outputs in a local ledger with SHA-256 fingerprints, model and prompt metadata, timestamps, and a stated rights holder for later integrity checks and lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (release metadata); bundled Python code: MIT; documentation and theory: all rights reserved

## Use Case:

Developers and teams register AI-generated work locally, check whether an output still matches its recorded fingerprint, and look up stated model and ownership metadata for audit trails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local ledger stores output summaries and metadata in plaintext, even though prompts are hashed.

Mitigation: Do not register secrets, confidential text, or regulated personal data unless local plaintext persistence is acceptable; protect access to the ledger.

Risk: A matching fingerprint establishes byte-level consistency, not factual correctness or legal ownership.

Mitigation: Review content and rights claims separately before relying on a registry entry.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-output-registry)
- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Command-line text and local JSONL, CSV, and Markdown ledgers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registration IDs and SHA-256 fingerprints; ledger entries include metadata and a plaintext output excerpt.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled SKILL.md says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
