## Description: <br>
A text editor for LLMs, not humans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[frane](https://clawhub.ai/user/frane) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to teach agents how to drive the ae command-line editor for durable, stateful text edits, annotations, history, and multi-file refactors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The ae editor can write files and create persistent .agented workspace state, including edit history and annotations. <br>
Mitigation: Use it only in intended workspaces, review target paths before edits, and treat persisted annotations and history as project data. <br>
Risk: Installation and permissions commands can modify other agent clients' skill, MCP, or permission configuration. <br>
Mitigation: Prefer the Homebrew install path and review targets before running ae skill install, ae mcp install, or ae permissions commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/frane/skills/agented) <br>
- [Project homepage](https://github.com/frane/agented) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides an agent to use ae for text editing workflows and agent-client integration commands.] <br>

## Skill Version(s): <br>
1.4.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
