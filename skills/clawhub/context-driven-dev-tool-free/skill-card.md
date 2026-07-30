## Description: <br>
Guides agents through context-driven development by creating and maintaining project context documents for product goals, technical stack, workflows, task tracking, and session continuity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual users use this skill to initialize context documentation for new projects, adapt existing codebases, and keep AI-assisted development aligned across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests read, write, and command execution capabilities for project workspaces. <br>
Mitigation: Use it only in trusted workspaces, constrain access where possible, and review proposed file changes and shell commands before applying them. <br>
Risk: The optional callback_url parameter can send task data to an external endpoint. <br>
Mitigation: Avoid callback_url unless the endpoint is trusted and the data that may be transmitted is understood. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/context-driven-dev-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands, Code] <br>
**Output Format:** [Markdown guidance with examples, tables, JSON/YAML snippets, Python snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces context documentation guidance and structured response examples; the free edition is described as supporting single-task use.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
