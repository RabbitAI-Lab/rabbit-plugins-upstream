## Description: <br>
Save conversations to a local memory index with FTS5 rebuilds, conversation-log cross-references, and saved-conversation dispatch. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mirza42](https://clawhub.ai/user/mirza42) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to save session summaries as durable local Markdown memory, keep a conversation log, and rebuild a local full-text search index for later retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local memory can capture private or sensitive conversation content in saved files and searchable metadata. <br>
Mitigation: Review the workspace path before installing, avoid saving secrets or private data, and use off-the-record handling for conversations that should not be logged or indexed. <br>
Risk: The index builder scans Markdown files in the configured workspace, which can make unrelated local Markdown content searchable. <br>
Mitigation: Set OPENCLAW_WORKSPACE and SAVED_CONVERSATIONS_DIR deliberately, and run the skill only in workspaces intended for local memory indexing. <br>
Risk: Initialization or reinstall steps may overwrite the conversation log and regenerate searchable metadata on disk. <br>
Mitigation: Inspect or back up the saved conversation directory before reinstalling or reinitializing the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mirza42/skills/save) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown summaries and conversation-log entries with shell command snippets for local index operations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local saved conversation files, conversation-log entries, and searchable index metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
