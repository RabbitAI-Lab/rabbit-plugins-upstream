## Description: <br>
会员运营 · 马甲实战版 is an agent skill that helps users design, diagnose, and explain a simulated chain-store membership data platform, including dataset structures, Spark SQL metric formulas, ETL references, dashboard planning, DDL guidance, and data-quality troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maojiebc](https://clawhub.ai/user/maojiebc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Business, operations, and data teams use this skill as a membership-data consultant for caliber and formula Q&A, staged data-warehouse design, gap checks against a 54-dataset checklist, DDL drafting, role-based dashboard planning, data-quality troubleshooting, and training material. The included business data is simulated, so structures and metric definitions are reusable but sample values are not evidence of real performance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dashboard templates may include custom card scripts that fetch card data through the viewer's BI session. <br>
Mitigation: Review or remove custom card scripts that call /api/card/.../data before importing the Guandata dashboard JSON into a live BI tenant. <br>
Risk: Production adaptation for member, employee, or customer-contact data can introduce sensitive-data handling obligations. <br>
Mitigation: Apply access controls, consent checks, and internal data-governance review before using the skill's structures with real operational data. <br>
Risk: The included sample values are simulated and can be mistaken for real business benchmarks. <br>
Mitigation: Use the structures, field definitions, and metric formulas as references, but do not use sample values as real operating data or industry baselines. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-huiyuan) <br>
- [Project homepage](https://github.com/maojiebc/majia-huiyuan) <br>
- [Agent task guide](artifact/AGENTS.md) <br>
- [Machine-readable index](artifact/llms.txt) <br>
- [Formula library index](artifact/公式库/README.md) <br>
- [Architecture diagram](https://raw.githubusercontent.com/maojiebc/majia-huiyuan/main/docs/architecture.png) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with SQL, DDL, checklists, file-path citations, and occasional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Answers should cite artifact-relative source paths and distinguish simulated sample values from reusable structures and formulas.] <br>

## Skill Version(s): <br>
1.3.1 (source: evidence.release.version, manifest.json, and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
