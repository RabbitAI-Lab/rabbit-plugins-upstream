## Description: <br>
Specs a dbt model by defining its grain, lineage, transformation logic, columns, tests, materialization, and starter SQL/YAML. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analytics engineers, and data teams use this skill to design dbt staging, intermediate, or mart models before implementation, including grain, lineage, transformations, tests, materialization, and starter SQL/YAML. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated dbt SQL or YAML may contain incorrect assumptions because the skill creates design skeletons rather than validating a live warehouse. <br>
Mitigation: Review the generated model spec, tests, SQL, and YAML against project conventions and warehouse behavior before committing or running them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/dbt-model-spec) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/dbt-model-spec.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with SQL and YAML skeletons] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are planning artifacts and implementation starters; users should review generated SQL and YAML before committing them.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
