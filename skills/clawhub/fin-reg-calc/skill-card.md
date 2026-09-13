## Description:

fin-reg-calc provides an offline CLI for financial AI compliance self-checks, including investor suitability matching and large-transaction reporting threshold checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance teams, and operators of financial or licensed-institution AI systems can use this skill to run local suitability and transaction-threshold checks as an auxiliary compliance self-check. Final compliance decisions still require qualified human review and current official requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned or global installation can make the installed skill differ from the reviewed release.

Mitigation: Pin the installer and repository commit before use, and avoid global installation where possible.

Risk: Invalid numeric financial inputs may be marked compliant by the calculator.

Mitigation: Add and review numeric input validation before relying on the exit code, especially in automated workflows.

Risk: Compliance output may be mistaken for legal or regulatory authority.

Mitigation: Use the skill only as an auxiliary local checker and require qualified compliance staff to review final decisions against official current requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/fin-reg-calc)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON CLI output with process exit codes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally and offline; exit code 0 indicates pass, 1 indicates an issue, and 2 indicates usage or environment error.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
