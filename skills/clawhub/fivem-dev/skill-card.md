## Description: <br>
Provides FiveM RP server engineering guidance for QBCore, ESX, and QBox, covering scripting, resource validation, debugging, optimization, framework compatibility, and SFTP key-handling guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dktrn9ne](https://clawhub.ai/user/dktrn9ne) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and FiveM server operators use this skill to plan, debug, and review roleplay server resources, framework migrations, performance fixes, hardening steps, and SFTP key-handling procedures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SSH key and SFTP guidance could affect sensitive credentials. <br>
Mitigation: Treat generated keys as secrets, avoid overwriting existing keys, and use least-privilege SFTP accounts. <br>
Risk: Server, resource, or database changes could disrupt a live FiveM environment if applied directly. <br>
Mitigation: Review proposed changes, test them in a staging server, and keep backups before production deployment. <br>
Risk: Framework, artifact, and gamebuild advice may not match every QBCore, ESX, QBox, or FiveM deployment. <br>
Mitigation: Verify compatibility against the target framework version, pinned gamebuild, and installed dependencies before rollout. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dktrn9ne/skills/fivem-dev) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code, configuration examples, and command suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory output for manual review before applying server, database, SFTP, or production changes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
