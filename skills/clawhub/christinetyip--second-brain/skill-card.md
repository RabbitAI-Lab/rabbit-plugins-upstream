## Description: <br>
Second Brain helps agents capture, organize, retrieve, update, and delete a user's Ensue-backed personal knowledge entries after user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[christinetyip](https://clawhub.ai/user/christinetyip) <br>

### License/Terms of Use: <br>


## Use Case: <br>
People using agents use this skill to keep a persistent knowledge base of concepts, tools, patterns, references, toolbox entries, and private notes, then retrieve relevant context in later conversations. It is intended for confirmed saves and searches, not automatic capture. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent cloud storage may retain sensitive personal knowledge if users save secrets, private details, or credentials. <br>
Mitigation: Review drafts before saving, avoid secrets and highly sensitive personal details, and keep saved entries scoped to knowledge that is appropriate for Ensue storage. <br>
Risk: The skill requires an Ensue API key to search and modify the user's knowledge base. <br>
Mitigation: Configure ENSUE_API_KEY securely, do not log or display the key, and use an Ensue account trusted for this data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/christinetyip/skills/second-brain) <br>
- [Ensue Network](https://ensue-network.ai?utm_source=clawdbot&utm_medium=workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API arguments; API helper responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ENSUE_API_KEY and uses the Ensue API for persistent storage and semantic search.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
