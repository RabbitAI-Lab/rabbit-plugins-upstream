## Description: <br>
Local memory management for agents. Compression detection, auto-snapshots, and semantic search. Use when agents need to detect compression risk before memory loss, save context snapshots, search historical memories, or track memory usage patterns. Never lose context again. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marmikcfc](https://clawhub.ai/user/marmikcfc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to initialize, organize, search, snapshot, and monitor local agent memory across episodic, semantic, and procedural Markdown stores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Organizer and categorization commands can move, copy, append, or overwrite local Markdown memory files. <br>
Mitigation: Back up important memory files and review destination folders before running organize.sh or categorize.sh. <br>
Risk: Snapshots and legacy folders may duplicate sensitive agent memory content. <br>
Mitigation: Treat generated snapshot and legacy files as sensitive local data and review them before sharing or committing. <br>


## Reference(s): <br>
- [Memory Manager ClawHub Skill Page](https://clawhub.ai/marmikcfc/skills/memory-manager) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and local Markdown memory files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates local workspace memory directories, state JSON, snapshots, and categorized Markdown files.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
