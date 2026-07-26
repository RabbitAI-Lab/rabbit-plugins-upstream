## Description: <br>
OpenKM Document Management via REST API (folders, documents, metadata, versioning, search, workflows). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pes0](https://clawhub.ai/user/pes0) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent manage OpenKM folders, documents, metadata, version history, search, and workflow tasks through the local REST CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, modify, move, delete, restore, upload, and manage OpenKM documents with the permissions of the configured account. <br>
Mitigation: Use a least-privilege OpenKM account and require explicit confirmation before delete, move, restore-version, upload/checkin, or workflow task actions. <br>
Risk: The OPENKM_PASSWORD credential could be exposed through mishandling of environment variables or shared logs. <br>
Mitigation: Protect OPENKM_PASSWORD as a secret and avoid sharing logs, especially when OPENKM_DEBUG is enabled. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pes0/skills/openkm-rest) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Text, shell commands, JSON responses, and downloaded or uploaded files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python and OPENKM_BASE_URL, OPENKM_USERNAME, and OPENKM_PASSWORD; actions run with the configured OpenKM account permissions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
