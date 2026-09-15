## Description:

预付账款核销台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users run this skill during month-end close, reconciliation, or inventory checks to validate prepaid-account offset ledgers. It checks row arithmetic, totals, duplicate supplier-contract rows, and missing key fields from user-provided ledger text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented optional paid-upgrade flow asks an agent to run an unpinned external installer and install unaudited skills.

Mitigation: Review the external installer, resolved package version, payment terms, and any newly installed skill instructions manually before proceeding; do not let an agent execute the upgrade prompt automatically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/prepayment-offset-check-free)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON findings with cited ledger rows and summary fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local Node.js input files; reports insufficient input instead of issuing unsupported conclusions.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
