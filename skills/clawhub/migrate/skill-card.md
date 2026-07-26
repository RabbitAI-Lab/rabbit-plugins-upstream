## Description: <br>
Export and import Clawdbot installations for migration between machines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrgoodb](https://clawhub.ai/user/mrgoodb) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to back up, migrate, or restore a Clawdbot installation, including workspace files, configuration, managed skills, WhatsApp session data, and optional credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Export archives can contain sensitive WhatsApp session data and, when requested, credentials. <br>
Mitigation: Store and transfer archives securely, restrict access, and use --include-credentials only when necessary. <br>
Risk: Importing an archive can merge or overwrite an existing Clawdbot workspace and configuration. <br>
Mitigation: Import only trusted archives and avoid --force unless restoring onto a fresh or intentionally replaceable setup. <br>


## Reference(s): <br>
- [Migrate skill page](https://clawhub.ai/mrgoodb/skills/migrate) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command examples and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces migration instructions for creating and restoring tar.gz export archives.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
