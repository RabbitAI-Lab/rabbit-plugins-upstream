## Description: <br>
Memory Maintenance helps OpenClaw agents review daily notes, suggest MEMORY.md updates, monitor memory directory health, and clean up old files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maxlauriehutchinson](https://clawhub.ai/user/maxlauriehutchinson) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to keep OpenClaw memory files organized by reviewing recent notes, generating human-reviewed MEMORY.md suggestions, and applying scheduled retention cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local agent memory may be analyzed by Gemini. <br>
Mitigation: Install only when this data flow is acceptable, and avoid placing unrelated secrets in files the skill reviews. <br>
Risk: Scheduled maintenance can change local memory files. <br>
Mitigation: Inspect scripts before enabling automation, use dry-run or review modes first, and confirm a recoverable trash or backup path is available. <br>
Risk: .env files may be sourced during setup or review. <br>
Mitigation: Keep only required environment variables in the workspace .env and avoid storing unrelated secrets there. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maxlauriehutchinson/skills/memory-maintenance) <br>
- [Publisher profile](https://clawhub.ai/user/maxlauriehutchinson) <br>
- [README](artifact/README.md) <br>
- [Skill documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [JSON and Markdown review files with shell-command workflows and configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces review reports, structured suggestions, status summaries, and maintenance actions for local OpenClaw memory files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
