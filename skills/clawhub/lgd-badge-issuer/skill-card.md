## Description:

Issues an lgd-certified badge certificate only when all three LGD evidence categories are present, recording SHA-256 fingerprints and an issuance ledger while refusing and logging incomplete submissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and governance teams use this skill to run a lightweight badge issuance workflow that records accepted or refused LGD evidence submissions. It is intended as an auxiliary governance framework and requires human or organizational review for consequential compliance decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create authoritative-looking badge certificates from evidence references that are not independently validated.

Mitigation: Require real evidence validation, trusted evaluator signatures, and human or organizational review before treating a badge as proof of compliance.

Risk: Generated badges may be mistaken for official legal, medical, clinical, or regulated professional determinations.

Mitigation: Use the output only as an auxiliary governance record and defer consequential regulated decisions to official sources and qualified reviewers.

Risk: Installing or running an unreviewed release could make local ledger output appear more trustworthy than the release warrants.

Mitigation: Pin installation to a reviewed release and verify the packaged files against the server-provided hashes before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-badge-issuer)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance plus CLI commands; runtime output is JSON or plain text with optional JSON certificate and ledger files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SHA-256 fingerprints and process exit codes to report issued, refused, or usage-error outcomes.]

## Skill Version(s):

1.0.0 (source: server release metadata and manifest.json; SKILL.md frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
