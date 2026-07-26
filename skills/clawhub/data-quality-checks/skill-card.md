## Description: <br>
Design the data quality checks for a table or pipeline across the standard dimensions, producing a checks plan across completeness, validity, uniqueness, freshness, consistency, and accuracy with the rule, severity, and implementation location for each check. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data engineers, and analytics teams use this skill to define practical data quality checks for tables and pipelines before bad data reaches dashboards or models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Table or pipeline descriptions can include private schema details or sensitive business context. <br>
Mitigation: Share only the schema fields and quality expectations needed to design checks; avoid secrets and unnecessary private data. <br>
Risk: Generated checks may block pipelines too aggressively or miss dataset-specific failure modes. <br>
Mitigation: Review proposed severities, freshness SLAs, and failure actions with the data owner before enforcing them in production. <br>


## Reference(s): <br>
- [Data Quality Checks homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/data-quality-checks.html) <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/data-quality-checks) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance, configuration] <br>
**Output Format:** [Markdown plan with a checks table and implementation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Organizes checks by data quality dimension and includes severity, implementation location, and failure-handling guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
