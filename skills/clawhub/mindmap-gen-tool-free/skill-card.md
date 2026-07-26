## Description: <br>
Generates structured mind maps from topics or documents, with support for Markmap-style Markdown and basic layout options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to turn a topic, document, or learning goal into a structured mind map for planning, study, research, writing, or analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad command and file permissions for a mind-map generation workflow. <br>
Mitigation: Review requested file writes, dependency installs, and shell commands before approving execution, and keep the agent limited to the mind-map task. <br>
Risk: The skill includes an optional callback URL without detailed scoping or user-control guidance. <br>
Mitigation: Use callback URLs only when the destination is trusted and avoid sending sensitive document content through callbacks. <br>
Risk: The security verdict is suspicious due to broad authority and insufficient scoping detail. <br>
Mitigation: Avoid giving the skill sensitive documents unless the publisher is trusted and the execution environment is constrained. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/mindmap-gen-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and JSON-style structured responses, with optional shell commands and code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Markmap-compatible Markdown and single-task output for the free edition.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
