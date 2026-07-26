## Description: <br>
Persistent Memory Engine helps agents maintain a local, structured long-term memory store under ~/memory with indexing, retrieval, lifecycle management, conflict versioning, and trash recovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to persist long-running project, relationship, decision, preference, and knowledge records across sessions in a local Markdown memory tree. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist and index personal conversation details in a durable local memory folder. <br>
Mitigation: Require explicit confirmation before saving new memories and avoid storing secrets or sensitive personal details. <br>
Risk: Optional vector or semantic retrieval may expose memory content to a configured provider if a cloud service is chosen. <br>
Mitigation: Keep semantic and vector retrieval local unless a provider is explicitly approved for the data being indexed. <br>
Risk: Lifecycle cleanup can move or permanently delete memory records after retention windows. <br>
Mitigation: Review trash retention settings and backups before enabling cleanup of important records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/persistent-memory-engine) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell-command examples and local memory file operations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads and writes local Markdown memory files under ~/memory; optional semantic retrieval may require a configured vector provider.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
