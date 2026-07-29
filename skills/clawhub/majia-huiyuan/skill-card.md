## Description: <br>
Membership Ops - Majia Field Edition helps agents answer membership metric, RFM, retention, SQL, data-warehouse, data-quality, and dashboard-design questions using a simulated chain-retail reference system. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maojiebc](https://clawhub.ai/user/maojiebc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, business analysts, data analysts, and data teams use this skill to design membership analytics systems, define metric formulas, generate SQL or schema guidance, troubleshoot data quality, and plan role-based BI dashboards. The included examples are simulated and should be used for structure, fields, and calculation patterns rather than real business benchmarks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be applied to real customer data or marketing workflows without adequate authorization or consent. <br>
Mitigation: Use it for analytics, schema, SQL, and dashboard design; require separate authorization, consent checks, masking or tokenization, and human review before using outputs with real customer records. <br>
Risk: Identity stitching and segmentation guidance can affect sensitive customer profiles. <br>
Mitigation: Require human review before applying identity linkage or sending any segments to marketing, CDP, or outreach systems. <br>
Risk: Simulated example values may be mistaken for real operating data or industry benchmarks. <br>
Mitigation: Treat bundled values as synthetic; reuse only structures, field definitions, metric formulas, and design patterns unless validated against the user's own data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-huiyuan) <br>
- [Project homepage from metadata](https://github.com/maojiebc/majia-huiyuan) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Agent guidance](artifact/AGENTS.md) <br>
- [Formula library](artifact/公式库/README.md) <br>
- [Machine-readable index](artifact/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with SQL, DDL, file references, and concise analysis] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should cite artifact paths when using bundled formulas, schemas, ETL logic, or dashboard definitions.] <br>

## Skill Version(s): <br>
1.3.2 (source: SKILL.md metadata.version, server release.version, and version history released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
