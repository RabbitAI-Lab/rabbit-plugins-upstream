## Description: <br>
Cloud-hosted markdown collaboration for agents and humans. One API call to create, one link to share. End-to-end encrypted, no account required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bndkts](https://clawhub.ai/user/bndkts) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and human collaborators use this skill to create, read, update, and share cloud-hosted markdown documents and workspaces for task logs, reports, project notes, and documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an external cloud markdown service, so sensitive content could be uploaded outside the user's environment. <br>
Mitigation: Require explicit approval before uploading sensitive content and limit shared documents to information appropriate for the service. <br>
Risk: Document and workspace write keys grant powerful access and may be exposed if stored in prompts, logs, plaintext config, or general memory. <br>
Mitigation: Prefer an agent's built-in secrets or credential storage, share read keys when possible, and keep write and workspace keys out of logs and prompts. <br>
Risk: Overwrite or delete operations can remove shared markdown content or lose collaborators' changes. <br>
Mitigation: Use ETags with If-Match for writes and require confirmation before overwrite or delete operations. <br>


## Reference(s): <br>
- [molt-md ClawHub listing](https://clawhub.ai/bndkts/skills/molt-md) <br>
- [molt-md website](https://molt-md.com) <br>
- [molt-md API documentation](https://github.com/bndkts/molt-md/blob/main/API.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, API calls, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with JSON examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce molt-md document or workspace identifiers, read keys, write keys, ETags, and share URLs that require careful handling.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata and artifact manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
