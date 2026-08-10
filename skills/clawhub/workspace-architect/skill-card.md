## Description: <br>
Workspace Architect creates, analyzes, and optimizes OpenClaw workspace configuration files with guided workflows, best-practices validation, pattern analysis, and sandboxed draft changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luanvha2550-hash](https://clawhub.ai/user/luanvha2550-hash) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw workspace maintainers use this skill to create new workspace configuration files, audit existing files for clarity and placement issues, and prepare optimized drafts for review before applying changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workspace analysis may expose OpenClaw configuration, profile, memory, and tool notes to the agent running the skill. <br>
Mitigation: Use the skill only when that review is intended, keep secrets out of workspace files, and remove sensitive data before analysis. <br>
Risk: Generated drafts or recommendations may introduce incorrect, incomplete, or misleading workspace instructions. <br>
Mitigation: Review proposed diffs and analysis reports before applying changes, and require explicit confirmation for any modification. <br>


## Reference(s): <br>
- [OpenClaw Skills Documentation](https://docs.openclaw.ai/tools/skills) <br>
- [Arquivo Specifications](references/arquivo-specs.md) <br>
- [Best Practices](references/best-practices.md) <br>
- [Workspace Patterns](references/patterns.md) <br>
- [Workspace Questionnaire](references/questionnaire.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown reports, configuration file drafts, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Draft modifications are described as sandboxed workspace files that require explicit user confirmation before application.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
