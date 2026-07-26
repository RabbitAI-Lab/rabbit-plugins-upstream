## Description: <br>
Advanced filesystem operations - listing, searching, batch processing, and directory analysis for Clawdbot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gtrusler](https://clawhub.ai/user/gtrusler) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to list, search, analyze, and copy local files and directories with filtering, formatting, and dry-run support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent-accessible tool the ability to inspect and copy local files. <br>
Mitigation: Use narrow working paths, limit access to intended directories, and review proposed filesystem operations before execution. <br>
Risk: Copy operations may overwrite or move sensitive data if used carelessly. <br>
Mitigation: Prefer dry-run mode before copy operations and require explicit review before enabling overwrite behavior. <br>
Risk: The scanned artifact bundle did not include the executable implementation. <br>
Mitigation: Verify the actual CLI implementation from the package source before running or deploying the skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gtrusler/skills/clawdbot-filesystem) <br>
- [Node.js](https://nodejs.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown or terminal text with optional JSON and file operation results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and local filesystem access; network access is not indicated in the reviewed evidence.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
