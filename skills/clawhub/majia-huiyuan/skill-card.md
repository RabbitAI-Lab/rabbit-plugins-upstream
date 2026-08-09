## Description:

Membership data consultant for metric definitions, RFM and segmentation, CDP and OneID design, warehouse schemas, SQL/DDL, data-quality checks, and dashboard planning using a simulated chain-store membership data system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

Business analysts, data teams, and membership operations leads use this skill to answer membership metric questions, design CRM/CDP data structures, select target audiences for lifecycle actions, generate SQL/DDL patterns, and plan BI dashboards. It should be used as a reference system: simulated values are not business benchmarks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Simulated sample values could be mistaken for real operating benchmarks.

Mitigation: Use the included structures, fields, formulas, and dashboard patterns as references only; replace all sample values with validated production data before business decisions.

Risk: SQL and metric logic may produce wrong results if moved unchanged to a non-Spark engine or a different data model.

Mitigation: Review formulas, date functions, null handling, and joins for the target engine and reconcile outputs against known source-system totals.

Risk: Optional Guandata BI import or CLI replication steps may affect a workspace or rely on instance-specific resource IDs.

Mitigation: Review import commands before execution, regenerate platform IDs for the target instance, and test in a non-production workspace first.

Risk: Audience selection and lifecycle task guidance can lead to over-contacting customers if used without consent and frequency controls.

Mitigation: Apply consent, suppression, frequency-cap, and human review policies before operationalizing targeting or task-dispatch recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-huiyuan)
- [GitHub repository](https://github.com/maojiebc/majia-huiyuan)
- [README.en.md](README.en.md)
- [AGENTS.md](AGENTS.md)
- [Formula playbook index](公式库/README.md)
- [Architecture diagram](https://raw.githubusercontent.com/maojiebc/majia-huiyuan/main/docs/architecture.png)
- [GitHub releases](https://github.com/maojiebc/majia-huiyuan/releases)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown or text with SQL, DDL, file-path citations, and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Spark SQL examples; generated values should be treated as simulated reference data.]

## Skill Version(s):

1.4.0 (source: SKILL.md metadata and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
