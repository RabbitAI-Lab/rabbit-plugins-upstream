## Description: <br>
Api Dev Tool Free helps an agent support API development workflows including API design decisions, OpenAPI specification generation, endpoint scaffolding, testing, documentation, and version-management guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan, generate, review, and document APIs across REST, GraphQL, OpenAPI, testing, security-check, and version-migration tasks. It is aimed at personal daily use and single-task API development assistance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests file-writing and command-execution authority for broad API development tasks. <br>
Mitigation: Use it in a project-specific workspace, review generated file changes before applying them, and approve local commands only after checking intent and scope. <br>
Risk: Callback URLs or sensitive API and project data may be sent externally if the user provides them for API workflow tasks. <br>
Mitigation: Do not provide callback URLs, credentials, private API details, or sensitive project data unless external sharing is intended and authorized. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/api-dev-tool-free) <br>
- [SkillHub](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks and structured JSON-style responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or write project files and run local commands when the host agent grants write and exec tools.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
