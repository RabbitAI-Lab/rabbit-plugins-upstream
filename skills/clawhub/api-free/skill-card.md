## Description: <br>
Api Free is a free REST API reference skill covering AI/ML, payment, and communication services with authentication notes, endpoint references, curl examples, and common error guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to look up basic integration details for common REST APIs and draft reference-only curl examples before implementing calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution authority while presenting live API and payment curl examples. <br>
Mitigation: Treat curl snippets as reference only, require review before execution, and adapt them with test-mode credentials first. <br>
Risk: API credentials could be exposed or used against real services if examples are copied without controls. <br>
Mitigation: Keep credentials out of URLs and version control, prefer scoped or disposable keys, and verify each target endpoint before use. <br>


## Reference(s): <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reference-only output; review examples before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
