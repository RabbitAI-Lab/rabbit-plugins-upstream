## Description: <br>
Access and manage Bitwarden/Vaultwarden passwords securely using the rbw CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asleep123](https://clawhub.ai/user/asleep123) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and other agent users use this skill to configure rbw and run Bitwarden or Vaultwarden vault commands for listing, searching, retrieving, adding, and syncing password entries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Vault secrets can be exposed to the agent session, terminal output, logs, or conversation transcript when rbw commands retrieve credentials. <br>
Mitigation: Review commands before execution, avoid printing full entries unless necessary, and treat any retrieved credentials as exposed. <br>
Risk: The skill can run rbw commands against a Bitwarden or Vaultwarden vault. <br>
Mitigation: Install and use it only when the user is comfortable granting the agent that level of vault access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/asleep123/skills/bitwarden) <br>
- [Publisher profile](https://clawhub.ai/user/asleep123) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the rbw CLI on Linux or macOS; command output may include vault item data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
