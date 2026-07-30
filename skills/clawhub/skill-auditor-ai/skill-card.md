## Description: <br>
Skill Auditor audits existing agent skills across structure, security, triggers, effectiveness, competition, platform compliance, documentation, and code quality, with optional user-authorized remediation and regression review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this skill to inspect an existing agent skill, receive a standardized audit report, and optionally apply authorized remediation followed by regression review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Normal audits write report files into the audited skill directory, and remediation or originality cleanup can modify target skill files after confirmation. <br>
Mitigation: Use the skill only on repositories where local report files and optional edits are acceptable, and keep version control or backups for audited skills. <br>
Risk: Audit findings and remediation suggestions can be incomplete or incorrect for a target skill. <br>
Mitigation: Review generated reports and proposed edits before relying on them for release decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/skill-auditor-ai) <br>
- [ClawHub metadata homepage](https://github.com/EdwardWason/skill-auditor) <br>
- [Maturity model](references/maturity-model.md) <br>
- [Audit dimensions](references/audit-dimensions.md) <br>
- [Security scan methodology](references/security-scan.md) <br>
- [Benchmarking methodology](references/benchmarking.md) <br>
- [Report template](references/report-template.md) <br>
- [Regression audit methodology](references/regression.md) <br>
- [Originality check methodology](references/originality-check.md) <br>
- [Skill authoring guide](references/skill-authoring-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown audit reports with findings, scoring tables, remediation notes, and regression summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes .audit-report.md in the audited skill directory during normal audits and may update target skill files only after user confirmation.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
