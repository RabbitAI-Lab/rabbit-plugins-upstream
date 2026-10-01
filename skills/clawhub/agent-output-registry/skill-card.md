## Description:

Registers AI-generated outputs in a local ledger with content fingerprints and generation metadata, and helps verify integrity or look up recorded ownership.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

Developers and teams register AI-generated outputs to retain a local record of content fingerprints, model details, timestamps, and claimed ownership, then check files against that record or retrieve entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local ledger entries retain short output summaries and metadata that may expose sensitive information.

Mitigation: Do not register secrets, confidential text, or internal identifiers; review inputs before adding them to the ledger.

Risk: A matching fingerprint establishes byte-for-byte integrity, not the correctness or legal ownership of an output.

Mitigation: Independently review content and ownership claims before relying on ledger records.

## Reference(s):

- [Agent Output Registry on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-output-registry)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [CLI text and local JSONL, CSV, and Markdown registry files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records SHA-256 fingerprints, short output summaries, model details, timestamps, and supplied ownership metadata; supports add, verify, lookup, and report.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata; bundled files show differing versions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
