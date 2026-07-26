## Description: <br>
Export a Codex session JSONL from ~/.codex/sessions into a clean Markdown transcript in ~/Documents/Exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bestisblessed](https://clawhub.ai/user/bestisblessed) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Codex users use this skill to export a current or specified Codex conversation from local session JSONL into a Markdown transcript for review, archiving, or sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exported transcripts can contain sensitive chat content such as private code, credentials, tokens, or personal details. <br>
Mitigation: Run this skill only when you intend to create a local transcript, review the Markdown before sharing it, and avoid exporting chats with sensitive content unless local storage under ~/Documents/Exports is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bestisblessed/export) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown transcript file plus a printed local file path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads local Codex session JSONL files under ~/.codex/sessions and writes Markdown exports under ~/Documents/Exports.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
