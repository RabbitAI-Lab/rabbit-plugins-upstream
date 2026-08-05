## Description: <br>
AI coding agent powered by CellCog Co-work. Code generation, debugging, refactoring, codebase exploration, terminal operations - executed directly on your machine. Lightweight with multimedia tools loaded on demand. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cellcog](https://clawhub.ai/user/cellcog) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI agents use this skill to delegate coding tasks to CodeCog through CellCog Co-work, including code generation, debugging, refactoring, codebase exploration, and terminal operations in a selected project directory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can let an AI coding agent read, edit, and run commands in a selected project directory through CellCog Desktop. <br>
Mitigation: Install only when that project-level access is acceptable, choose the working directory deliberately, and keep write auto-approval disabled unless the repository and task are trusted. <br>
Risk: Terminal, dependency, git, Docker, or deployment actions can change the local project or environment. <br>
Mitigation: Review requested terminal and write actions before approval, especially commands that install dependencies, modify version control state, or deploy software. <br>


## Reference(s): <br>
- [CellCog](https://cellcog.ai) <br>
- [ClawHub Skill Page](https://clawhub.ai/cellcog/skills/coding-agent-cellcog) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Python and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May request file edits and terminal operations through CellCog Desktop, with write and execute actions subject to user approval.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
