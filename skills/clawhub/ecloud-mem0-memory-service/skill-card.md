## Description: <br>
ecloud-mem0-memory-service provides a self-hosted mem0 long-term memory workflow for saving, searching, listing, retrieving, updating, and deleting user memories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zjial](https://clawhub.ai/user/zjial) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to connect to a trusted self-hosted mem0 service and manage long-term user memories through semantic search and CRUD operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Personal statements may be stored as long-term memories. <br>
Mitigation: Avoid sharing secrets or sensitive data in memory prompts, and require explicit confirmation before saving sensitive personal details. <br>
Risk: Configuration includes a local API key and server/user identifiers. <br>
Mitigation: Keep the generated .env file out of version control, restrict local file access, and rotate the API key if it is exposed. <br>
Risk: The skill supports destructive deletion of all memories for the configured user. <br>
Mitigation: Require explicit confirmation before running delete-all or other destructive memory operations. <br>
Risk: Memory operations depend on the configured mem0 server. <br>
Mitigation: Install and use the skill only with a mem0 server the user trusts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zjial/skills/ecloud-mem0-memory-service) <br>
- [Publisher profile](https://clawhub.ai/user/zjial) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MEM0_BASE_URL, MEM0_USER_ID, and MEM0_API_KEY configuration for a trusted mem0 server.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact manifest reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
