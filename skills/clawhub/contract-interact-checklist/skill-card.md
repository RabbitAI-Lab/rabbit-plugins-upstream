## Description:

Contract Interact Checklist provides a zero-dependency pre-interaction checklist for smart-contract users covering audit review, address confirmation, approval limits, revocation awareness, private-key handling, and small test transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, auditors, and blockchain users can use this skill before interacting with a smart contract to run a structured safety checklist and identify missing review steps or high-risk unlimited approvals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented installation flow can fetch mutable, unpinned remote code into a persistent agent skill directory.

Mitigation: Install only after reviewing the packaged files, and prefer a pinned release or commit with a verified checksum.

Risk: Checklist output may be mistaken for legal, financial, investment, or security advice.

Mitigation: Treat the output as pre-screening guidance and require human review or appropriate professional advice for consequential decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/contract-interact-checklist)
- [LGD Hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with command examples, terminal text output, and optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script exits with rc=0 for pass, rc=1 for checklist issues, and rc=2 for usage errors.]

## Skill Version(s):

1.0.0 (source: server release metadata and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
