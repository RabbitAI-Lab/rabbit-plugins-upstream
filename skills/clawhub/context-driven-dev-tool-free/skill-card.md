## Description: <br>
Helps agents manage structured project-context documents for project initialization, technology-stack tracking, workflow notes, and consistent AI-assisted development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual users use this skill to create, inspect, and maintain project context documents such as product notes, technology-stack records, workflow guidance, and task registers so AI coding sessions stay aligned across time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask an agent to read project files and create or update context Markdown files. <br>
Mitigation: Scope use to the intended workspace and review proposed file writes before approval. <br>
Risk: The skill includes command-execution capabilities for setup checks, package installation, and network troubleshooting. <br>
Mitigation: Review any proposed write, delete, pip install, or network-troubleshooting command before approving execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/context-driven-dev-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with optional code blocks, shell commands, and structured JSON-style responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local file reads, context-document writes, simple command execution, and single-task free-edition workflows.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
