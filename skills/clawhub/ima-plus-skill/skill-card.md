## Description: <br>
IMA.plus Skill manages IMA notes and knowledge bases, including search, note creation and editing, file uploads and exports, tags, permissions, and public discovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwqww1](https://clawhub.ai/user/wwqww1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate an IMA account's notes and knowledge bases through agent-guided workflows. It supports reading, creating, editing, uploading, exporting, tagging, permission management, and public discovery tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has access to IMA notes, knowledge bases, and API credentials. <br>
Mitigation: Install only when the publisher and skill are trusted, and prefer environment variables or a protected secret store over config.json. <br>
Risk: Bulk export and permission-change workflows can expose or alter private IMA content. <br>
Mitigation: Review bulk export, join, tag deletion, and permission-change requests before approving execution. <br>
Risk: The wrapper performs automatic update checks and writes state to config.json. <br>
Mitigation: Review local configuration handling before deployment and avoid storing long-lived secrets in writable skill directories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wwqww1/skills/ima-plus-skill) <br>
- [Publisher profile](https://clawhub.ai/user/wwqww1) <br>
- [IMA OpenAPI credential page](https://ima.qq.com/agent-interface) <br>
- [IMA API reference](artifact/knowledge-base/references/api.md) <br>
- [IMA Notes API reference](artifact/notes/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Files, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and user-provisioned IMA OpenAPI credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact display name references V1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
