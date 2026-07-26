## Description: <br>
Set up and use Bitwarden CLI (bw) for installation, authentication, unlock workflows, and reading secrets from a Bitwarden vault using email/password, API key, or SSO authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[startupbros](https://clawhub.ai/user/startupbros) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and vault-authorized users use this skill to install and operate Bitwarden CLI, manage login and unlock sessions, and retrieve credentials, secure notes, TOTP codes, and vault metadata for narrowly scoped tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to access Bitwarden vault secrets. <br>
Mitigation: Install it only for specific vault tasks, keep requests narrow, and prevent secrets from being printed, logged, or exposed in visible output. <br>
Risk: Session keys and secret-bearing environment variables can remain available in a shell or tmux session after the intended task is complete. <br>
Mitigation: Avoid shared tmux sessions and persistent shell exports; lock or log out of Bitwarden when the task is finished. <br>
Risk: Downloaded attachments or retrieved secret values can leave sensitive files on disk. <br>
Mitigation: Avoid writing secrets to disk unless necessary, and clean up any downloaded secret files immediately after use. <br>


## Reference(s): <br>
- [Bitwarden CLI documentation](https://bitwarden.com/help/cli/) <br>
- [Bitwarden downloads](https://bitwarden.com/download/) <br>
- [Get Started Guide](references/get-started.md) <br>
- [CLI Examples](references/cli-examples.md) <br>
- [ClawHub skill page](https://clawhub.ai/startupbros/skills/bitwarden-vault) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code] <br>
**Output Format:** [Markdown with inline bash, PowerShell, and JSON command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce commands that access secrets; output should not be logged or persisted unless explicitly required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
