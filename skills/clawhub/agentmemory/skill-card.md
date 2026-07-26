## Description: <br>
End-to-end encrypted cloud memory for AI agents. 100GB free storage. Store memories, files, and secrets securely. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[badaramoni](https://clawhub.ai/user/badaramoni) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use AgentMemory to give agents cloud-synced memory, semantic search, file storage, and secrets management through hosted API and CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can sync memories, files, secret metadata, and possibly credentials to a third-party cloud service with unclear operational security boundaries. <br>
Mitigation: Use the service only when third-party cloud memory is intended, avoid production credentials, regulated personal data, and confidential files unless the encryption and retention model has been verified. <br>
Risk: The documented CLI installation uses a globally installed npm package and automatic sync behavior. <br>
Mitigation: Pin and review the npm CLI before global installation, and require explicit confirmation before uploading files, storing sensitive memories, deleting memories, or revealing secrets. <br>


## Reference(s): <br>
- [AgentMemory skill page](https://clawhub.ai/badaramoni/skills/agentmemory) <br>
- [AgentMemory service](https://agentmemory.cloud) <br>
- [AgentMemory API](https://agentmemory.cloud/api) <br>
- [AgentMemory documentation](https://agentmemory.cloud/docs) <br>
- [AgentMemory issues](https://github.com/agentmemory/agentmemory/issues) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell commands, curl examples, and JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs guide agents to call AgentMemory APIs and CLI commands that can store, search, update, delete, upload, download, sync, and manage secrets.] <br>

## Skill Version(s): <br>
1.3.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
