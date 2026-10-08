## Description:

Helps agents and their users audit long-term memory for duplicates, orphaned entries, stale records, and missing provenance, then plan reversible cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and theory)

## Use Case:

Agent developers and users review Markdown or JSONL memory stores for duplicate, orphaned, stale, or unsourced entries, then consolidate records with backups and human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auditing unintended memory folders or JSONL files may expose sensitive memory content in reports.

Mitigation: Run the auditor only on memory files you intend to inspect and handle its output appropriately.

Risk: Incorrect or premature cleanup may discard useful memory or preserve misleading entries.

Mitigation: Review findings manually and back up memory before changing or deleting entries.

Risk: The package-level license label may be mistaken for permission to redistribute all included materials.

Mitigation: Check the included license: MIT applies to Python code, while documentation and theory text reserve rights.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-memory-keeper)
- [LGD project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [LGD theory](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Markdown guidance and human-readable or JSON audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit reports list entry counts and issues; no memory changes are made by the bundled auditor.]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
