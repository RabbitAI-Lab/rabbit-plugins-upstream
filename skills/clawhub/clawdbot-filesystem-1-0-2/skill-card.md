## Description: <br>
Advanced filesystem operations for listing, searching, batch processing, and directory analysis in Clawdbot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucky-2968](https://clawhub.ai/user/lucky-2968) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and agents use this skill to list, search, copy, visualize, and analyze local files and directories with filtering, dry-run copy workflows, and directory statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect and copy local files, which may expose sensitive files or process overly broad directories if paths are not scoped carefully. <br>
Mitigation: Keep paths narrow, avoid scanning secrets or full home directories unless necessary, and exclude directories that do not need inspection. <br>
Risk: Batch copy or overwrite operations can change files unexpectedly. <br>
Mitigation: Use dry-run before copy actions, keep confirmation requirements enabled, and require explicit confirmation before overwriting files. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/lucky-2968/skills/clawdbot-filesystem-1-0-2) <br>
- [Artifact-declared project homepage](https://github.com/gtrusler/clawdbot-filesystem) <br>
- [Clawdbot documentation](https://docs.clawd.bot) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text, table, tree, list, or JSON output with shell command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and local filesystem access; use dry-run and confirmation settings before copy or overwrite operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; package.json reports 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
