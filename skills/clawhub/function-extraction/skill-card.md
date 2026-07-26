## Description: <br>
Extracts the complete implementation chain for a selected project feature and generates technical development documentation covering business logic, data flow, exception handling, and Mermaid diagrams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[addxing](https://clawhub.ai/user/addxing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to trace a feature from an entry point through the relevant code path and produce implementation documentation that another engineer can use to understand or recreate the behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may produce detailed internal implementation documentation, including file paths, data flow, and configuration references. <br>
Mitigation: Use it only on project code the user is allowed to analyze and review or redact generated documentation before sharing it outside the intended audience. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/addxing/function-extraction) <br>
- [ClawHub skill page](https://clawhub.ai/addxing/skills/function-extraction) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Guidance] <br>
**Output Format:** [Markdown technical documentation with Mermaid diagram blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes feature overview, entry point, code paths and line references, business and data flow, exception handling, dependencies, configuration notes, and test guidance when applicable.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
