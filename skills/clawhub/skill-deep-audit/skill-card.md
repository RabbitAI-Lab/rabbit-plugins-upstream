## Description:

skill-deep-audit audits agent skills with deterministic L1/L2 checks across seven dimensions, producing scored ERR/WARN findings and guarded fix guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to evaluate whether an agent skill is ready to ship by running static or read-only dry-run checks and receiving a scored audit report with findings and fix guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads the target skill folder and creates an AUDIT-YYYY-MM-DD.md report in that folder.

Mitigation: Run it on a copy when the target directory must remain unchanged, and review the generated report before using findings for release decisions.

Risk: Fix mode can edit audited skill files.

Mitigation: Use fix mode only after explicit authorization and rely on the documented backup workflow before applying changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/skill-deep-audit)
- [Check rules](references/check-rules.md)
- [Output template](references/output-template.md)
- [Scan commands](references/scan-commands.md)
- [Controlled domains](references/controlled-domains.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown scorecard file and concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ERR/WARN severity, score totals, cited findings, dependency notes, and fix recommendations.]

## Skill Version(s):

1.1.0 (source: server release metadata and artifact documentation)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
