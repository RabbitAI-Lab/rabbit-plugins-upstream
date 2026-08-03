## Description: <br>
Helps migrate AI-assistant context, such as skills, rules, prompts, commands, and MCP configuration, between supported IDEs or agent tools with preview-first safety gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to preview and apply scoped migrations of agent context between supported IDEs and agent tools. It emphasizes dry-run review, named-path inspection, secret redaction, conflict handling, and manual boundaries for unsupported or UI-managed settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: MCP migration can change tool or server configuration and may expose credential-handling mistakes if the dry-run is not reviewed. <br>
Mitigation: Review the dry-run output before any approved apply, verify credential redaction, and re-authorize target IDE tools manually. <br>
Risk: Unsupported formats, opaque project trees, and UI-managed settings can be misrepresented if treated as direct file migrations. <br>
Mitigation: Use only named source and target paths, respect documented manual boundaries, and reconstruct unclear or unsupported settings manually. <br>


## Reference(s): <br>
- [IDE Reference Index](references/ide-registry.md) <br>
- [Migration safety and conflicts](references/migration-safety.md) <br>
- [MCP migration](references/mcp-migration.md) <br>
- [MCP transport](references/mcp-transport.md) <br>
- [Object migration](references/object-migration.md) <br>
- [Verification](references/verification.md) <br>
- [Script usage](scripts/README.md) <br>
- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/agent-skills-setup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON evidence summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preview-first workflow; approved applies may produce target configuration files and backup paths.] <br>

## Skill Version(s): <br>
0.7.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
