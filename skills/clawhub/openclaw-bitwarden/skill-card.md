## Description: <br>
Set up and use Bitwarden CLI (bw) for installing the CLI, unlocking a vault, and reading or generating secrets with BW_SESSION session management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jimihford](https://clawhub.ai/user/jimihford) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to work with Bitwarden CLI vault workflows from an agent session, including login checks, vault unlock, synchronization, item lookup, password retrieval, TOTP retrieval, and password generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access Bitwarden vault data when authenticated commands are run. <br>
Mitigation: Use it only for specific vault tasks, prefer narrow lookups over broad listings, and avoid sharing captured terminal output. <br>
Risk: Authenticated tmux sessions and terminal history can retain sensitive vault context. <br>
Mitigation: Treat tmux history as sensitive, lock Bitwarden, and kill the tmux session when finished. <br>
Risk: The sample Vaultwarden credentials are intended only for disposable local testing. <br>
Mitigation: Do not reuse the sample credentials outside local test environments. <br>


## Reference(s): <br>
- [Bitwarden CLI documentation](https://bitwarden.com/help/cli/) <br>
- [Vaultwarden](https://github.com/dani-garcia/vaultwarden) <br>
- [ClawHub skill page](https://clawhub.ai/jimihford/skills/openclaw-bitwarden) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include commands that access vault data; terminal captures and tmux session history should be treated as sensitive.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
