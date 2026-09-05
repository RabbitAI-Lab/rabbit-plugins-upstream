## Description:

Convert whole-book PDF, scanned PDF, DOCX, or TXT sources into a publication-grade hierarchical electronic edition with authoritative printed-TOC reconstruction, reviewed OCR cleanup, per-chapter TXT, combined TXT, structured JSON/TSV, deterministic validation, safe API upload, backup, and full read-back verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yasmineliu](https://clawhub.ai/user/yasmineliu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge-base operators use this skill to convert complete book sources into auditable structured JSON and deterministic TXT/TSV derivative bundles. It is intended for full-book rebuilding workflows where printed table-of-contents structure, OCR review, validation, and optional remote read-back evidence matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may produce a traceable draft when TOC or OCR review is incomplete.

Mitigation: Treat exit code 3 and pending review ledgers as unfinished work; require reviewed TOC/OCR decisions and strict bundle validation before publication.

Risk: Remote upload can replace target content and the evidence says the skill should not be treated as a complete turnkey API upload tool.

Mitigation: Require explicit upload authorization, exact target confirmation, a verified backup/export process, and post-upload read-back comparison before accepting remote changes.

Risk: Generated TXT/TSV derivatives can become stale after canonical JSON edits.

Mitigation: Regenerate derivatives from the reviewed JSON and run the fail-closed validator with artifact and OCR-review checks before delivery.

## Reference(s):

- [End-to-end pipeline](references/pipeline.md)
- [ClawHub skill page](https://clawhub.ai/yasmineliu/skills/book-pdf-to-structured-json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands plus generated JSON, TSV, and TXT files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a canonical book tree, OCR review ledger, validation logs, per-node TXT, combined TXT, and deterministic comparison fingerprints.]

## Skill Version(s):

2.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
