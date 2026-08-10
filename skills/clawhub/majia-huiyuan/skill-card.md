## Description:

Membership operations data consultant for metric definitions, RFM segmentation, CDP and OneID design, SQL examples, warehouse schemas, data-quality checks, and role-based BI dashboard planning using simulated chain-store data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

Business operators, analysts, and data teams use this skill to design or audit membership data systems, define customer and CRM metrics, plan dashboards, and draft reference SQL or DDL. The included data is simulated and the SQL is example material that should be validated against local schemas and controls before production use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Included numbers may be mistaken for real business data or industry benchmarks.

Mitigation: Use the numbers only as simulated examples; rely on the structures, fields, and metric definitions after validating them with local data.

Risk: Reference SQL may be copied into production without adapting schemas, SQL dialect, or business controls.

Mitigation: Review and test SQL against the target warehouse, map local fields explicitly, and run business-invariant checks before production use.

Risk: The optional GitHub clone path may fetch a larger upstream package than the packaged release.

Mitigation: Review the upstream source and release contents before installing or using files outside the validated package.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-huiyuan)
- [Project homepage from metadata/clawdis](https://github.com/maojiebc/majia-huiyuan)
- [README.en.md](README.en.md)
- [AGENTS.md](AGENTS.md)
- [Formula playbook index](公式库/README.md)
- [Shared metric definitions](ETL/公共口径/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise explanations, SQL or DDL snippets, checklists, and file-path references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Spark 3.4 SQL examples, schema guidance, dashboard plans, data-quality checks, and warnings when simulated data or non-portable platform IDs are involved.]

## Skill Version(s):

1.4.1 (source: server release, SKILL.md metadata, manifest.json, README version history)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
