## Description: <br>
A long-term memory skill for self-hosted mem0 servers that stores, searches, lists, retrieves, updates, and deletes user memories with semantic search and CRUD operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zjial](https://clawhub.ai/user/zjial) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to connect an agent to a trusted self-hosted mem0 service for long-term memory storage, semantic recall, and memory CRUD operations. It is intended for workflows where user-provided memories should persist in the configured remote mem0 service rather than local Markdown files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles personal memories and credentials and can automatically capture user-provided information for retention. <br>
Mitigation: Review before installing, disclose the retention behavior to users, and avoid providing highly sensitive information unless it is intended to be stored in the configured mem0 service. <br>
Risk: The skill sends memory content and an API key to the configured mem0 server. <br>
Mitigation: Use only a trusted mem0 server, prefer HTTPS, and avoid HTTP except for local testing. <br>
Risk: The API key is stored in a workspace .env file during setup. <br>
Mitigation: Limit access to the workspace and rotate the API key if the workspace or .env file may have been shared. <br>
Risk: The delete-all operation can remove all memories for the configured user without a built-in confirmation barrier. <br>
Mitigation: Require explicit user confirmation before invoking delete-all and review the target user ID before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zjial/skills/ecloud-mem0-memory-service) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MEM0_BASE_URL, MEM0_USER_ID, and MEM0_API_KEY; memory operations are scoped to the configured user ID.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
