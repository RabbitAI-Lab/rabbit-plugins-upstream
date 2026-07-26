## Description: <br>
Project management for AI agents using markdown files, helping agents install and use the Cairn CLI to create projects, manage tasks, track status, and coordinate human-AI collaboration through a shared workspace of markdown files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gregoryehill](https://clawhub.ai/user/gregoryehill) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI agents use letcairn.work to install and operate the Cairn CLI for markdown-backed project and task management, including task creation, status tracking, work logs, and project artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Global npm installation runs third-party package code and leaves a global CLI on the system. <br>
Mitigation: Install only after trusting the cairn-work npm package and publisher, and review package updates before running cairn upgrade. <br>
Risk: Onboarding creates a local workspace and context files that agents may read and act on. <br>
Mitigation: Review the selected workspace path and generated AGENTS.md and .cairn/planning.md files before relying on them for agent work. <br>
Risk: The execute autonomy level can allow deploy, publish, send, or similar side effects. <br>
Mitigation: Use execute only for tasks where those side effects are explicitly intended; use draft or propose when human review is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gregoryehill/skills/cairn-cli) <br>
- [Cairn website](https://letcairn.work/) <br>
- [cairn-work npm package](https://www.npmjs.com/package/cairn-work) <br>
- [Cairn CLI command reference](COMMANDS.md) <br>
- [Cairn CLI discussions](https://github.com/letcairnwork/cairn-cli/discussions) <br>
- [Cairn CLI issues](https://github.com/letcairnwork/cairn-cli/issues) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to create and update local markdown workspace files with YAML frontmatter.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
