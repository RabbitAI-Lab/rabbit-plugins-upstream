## Description: <br>
Keystone guides an agent through importing files, URLs, and Markdown into Keystone knowledge bases and retrieving grounded context through the Keystone REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[justaboyhai-wq](https://clawhub.ai/user/justaboyhai-wq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to connect an agent to a Keystone knowledge base, import documents or web content, browse stored knowledge, and retrieve relevant context through hybrid search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can be directed to read from or write to user-selected Keystone knowledge bases. <br>
Mitigation: Install only for intended Keystone workspaces, configure KEYSTONE_BASE_URL and KEYSTONE_API_KEY carefully, and review upload, edit, and delete actions before allowing them. <br>
Risk: Keystone API credentials could be exposed in shared output, commands, or saved files. <br>
Mitigation: Keep KEYSTONE_API_KEY in the agent environment and do not print, log, or persist the key in generated content. <br>
Risk: Imports, overwrites, or deletions may affect the wrong knowledge base or knowledge entry. <br>
Mitigation: Require an explicit target knowledge base and user confirmation before destructive actions or content-changing imports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/justaboyhai-wq/skills/keystone) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, curl examples, and JSON request bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires KEYSTONE_BASE_URL and KEYSTONE_API_KEY; the skill provides API usage guidance rather than executing requests by itself.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
