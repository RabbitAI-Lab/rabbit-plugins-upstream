## Description: <br>
Guides agents through full-lifecycle development for the Link CRM+AI microservice system, covering requirements analysis, design, Java/Spring code generation, testing, deployment, troubleshooting, and operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ysh2ldd](https://clawhub.ai/user/ysh2ldd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan, implement, test, deploy, and operate changes in a Link CRM+AI Java microservice environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary reports exposed sensitive internal credentials or configuration. <br>
Mitigation: Rotate exposed credentials and keys, replace internal endpoints and secrets with placeholders, and scan the skill before installation. <br>
Risk: The skill provides deployment and operations guidance without enough explicit approval and rollback controls. <br>
Mitigation: Require production approval gates, rollback plans, and environment-specific review before applying deployment or operations steps. <br>
Risk: Signature-bypass or destructive examples could be misapplied outside isolated testing. <br>
Mitigation: Limit bypass and delete examples to local test environments and require reviewer confirmation before running them. <br>


## Reference(s): <br>
- [Project Architecture](references/project-architecture.md) <br>
- [Coding Standards](references/coding-standards.md) <br>
- [API Design Guide](references/api-design-guide.md) <br>
- [Database Guide](references/database-guide.md) <br>
- [Deployment Guide](references/deployment-guide.md) <br>
- [Testing Guide](references/testing-guide.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Java/XML templates, checklists, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should be reviewed before execution or deployment, especially for operations, credential, and environment-specific steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
