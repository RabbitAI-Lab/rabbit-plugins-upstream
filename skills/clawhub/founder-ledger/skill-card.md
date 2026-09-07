## Description:

Founder Ledger is a one-file Python income ledger and milestone registry for solo founders tracking progress toward their first $1,000.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulscode](https://clawhub.ai/user/paulscode)

### License/Terms of Use:

MIT

## Use Case:

External developers and solo founders use this skill to run a local CLI ledger that records revenue entries, lists totals, and tracks first-$1,000 milestones in a JSON file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Revenue notes are stored in a local plaintext JSON file.

Mitigation: Use it only for low-sensitivity personal tracking, and avoid sensitive accounting records that require encryption, audit controls, multi-user access, or sync.

Risk: Milestones remain recorded after undo removes a revenue entry.

Mitigation: Treat milestones as historical first-crossing records, and review the ledger manually when correcting revenue reversals or refunds.

## Reference(s):

- [README](README.md)
- [Provenance](docs/provenance.md)
- [ClawHub skill listing](https://clawhub.ai/paulscode/skills/founder-ledger)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance]

**Output Format:** [CLI text output and optional JSON, with local ledger.json file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Python 3 standard library only; stores user-entered revenue data in a local plaintext JSON file.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
