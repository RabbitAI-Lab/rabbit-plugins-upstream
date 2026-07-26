## Description: <br>
Manage API keys securely via GNOME Keyring and inject them into OpenClaw config. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jswortz](https://clawhub.ai/user/jswortz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to store supported API keys in GNOME Keyring, update OpenClaw authentication configuration, propagate selected variables to the user service environment, and restart the OpenClaw Gateway. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles API keys and may expose secrets to service environments. <br>
Mitigation: Prefer the interactive prompt or stdin over command-line secret arguments, and review the service environment before installing. <br>
Risk: The skill can change OpenClaw credential files and restart or kill gateway processes. <br>
Mitigation: Install only after reviewing the affected OpenClaw paths and service behavior in a test environment. <br>
Risk: A configured SECRETS_ENV_FILE is sourced as shell code. <br>
Mitigation: Avoid plaintext .env files where possible and inspect any SECRETS_ENV_FILE before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jswortz/skills/secret-manager) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Shell script behavior with command-line output and configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores supported secrets in GNOME Keyring, can update OpenClaw auth profile configuration, imports selected variables into the systemd user environment, and restarts the OpenClaw Gateway service.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
