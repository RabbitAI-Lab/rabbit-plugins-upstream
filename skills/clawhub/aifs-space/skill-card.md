## Description: <br>
Store and retrieve files via AIFS.space cloud storage API. Use when persisting notes, documents, or data to the cloud; syncing files across sessions; or when the user mentions AIFS, aifs.space, or cloud file storage. Not to be used for any sensitive content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deploydon](https://clawhub.ai/user/deploydon) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, engineers, and agents use this skill to persist non-sensitive notes, documents, and data in AIFS.space, then list, read, patch, delete, and summarize remote files across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External file storage can expose sensitive or private content if the skill is used for secrets or regulated data. <br>
Mitigation: Use the skill only for non-sensitive content, as stated in the release evidence and skill description. <br>
Risk: Write, patch, and delete operations make real remote changes in AIFS.space storage. <br>
Mitigation: Confirm target paths before destructive actions and review generated commands before execution. <br>
Risk: Over-privileged API keys increase the impact of mistakes or credential exposure. <br>
Mitigation: Use the least-privilege AIFS API key that fits the task. <br>


## Reference(s): <br>
- [AIFS.space](https://aifs.space) <br>
- [ClawHub skill page](https://clawhub.ai/deploydon/skills/aifs-space) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with curl examples, JSON API responses, and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an AIFS_API_KEY. Remote writes, patches, and deletes affect AIFS.space storage.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
