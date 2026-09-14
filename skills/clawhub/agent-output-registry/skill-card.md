## Description:

Registers AI-generated outputs in a local ledger with SHA-256 output fingerprints, model, version, prompt hashes, timestamps, and ownership fields, then supports integrity verification, ownership lookup, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and audit-focused teams use this skill to register AI-generated outputs, verify whether later files match the registered fingerprint, and look up declared ownership and license metadata in a local ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned global install instructions may fetch code that differs from the reviewed release.

Mitigation: Install from a pinned, reviewed commit or release and verify the release hash before use.

Risk: The local registry can expose sensitive output summaries or metadata if confidential material is registered.

Mitigation: Run the tool in a dedicated directory and avoid registering sensitive outputs, secrets, internal identifiers, or confidential source text.

Risk: CSV registry exports can be unsafe when opened in spreadsheet software.

Mitigation: Treat generated CSV files as untrusted input and review or sanitize cells before opening them in spreadsheets.

Risk: The short LGD-REG identifier alone is not enough for high-stakes provenance decisions.

Mitigation: Use the full SHA-256 fingerprint, prompt hash, source metadata, and independent review when provenance has legal, compliance, or ownership consequences.

Risk: The mutable local ledger is useful for traceability but is not independently tamper-resistant.

Mitigation: Preserve registry backups or signed snapshots when audit integrity matters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-output-registry)
- [Project Homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command-line examples and local registry outputs in JSONL, CSV, and Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic command-line outcomes use rc=0/1/2; registry entries include output fingerprints, prompt hashes, model/version fields, timestamps, ownership, license, and summary text.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
