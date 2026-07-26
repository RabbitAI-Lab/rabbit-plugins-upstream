## Description: <br>
Skill Auditor scans AI agent skill files for red-flag patterns, permission mismatches, and risk scores, producing structured audit reports for review before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoran-xc](https://clawhub.ai/user/zoran-xc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, maintainers, and security reviewers use Skill Auditor before installing, vendoring, or updating agent skills to scan files, score risky patterns, and document install decisions. Teams can also run it in CI to audit skill directories on pull requests or scheduled checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes intentionally harmful command snippets in malicious-skill test fixtures and sample reports. <br>
Mitigation: Treat nested malicious samples and copied report snippets as test data only; do not install them, run them, or reuse their commands. <br>
Risk: CI examples can upload or expose audited skill directories if enabled without review. <br>
Mitigation: Review workflow artifact settings and the scope of audited files before enabling CI uploads. <br>
Risk: The auditor uses static analysis and can produce false positives or miss behavior that requires context. <br>
Mitigation: Pair the generated report with human source, permission, and code review before making install decisions. <br>


## Reference(s): <br>
- [Skill Auditor on ClawHub](https://clawhub.ai/zoran-xc/skills/skill-auditor) <br>
- [Rules Reference](references/rules.md) <br>
- [Scoring Reference](references/scoring.md) <br>
- [CI Integration Reference](references/ci-integration.md) <br>
- [Trust Database Reference](references/trust-database.md) <br>
- [Sample Audit Report](examples/report-example.md) <br>
- [skill-vetter](https://clawhub.ai/spclaudehome/skill-vetter) <br>
- [SkillScan](https://clawhub.ai/tokauthai/skillscan) <br>
- [ClawHub Security Reporting](https://www.51cto.com/article/847901.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown audit report with optional JSON output, bash commands, and CI YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes risk scores, rule violations, permission mismatch notes, verdict guidance, and CI threshold options.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
