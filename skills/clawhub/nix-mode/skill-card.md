## Description: <br>
Handle Clawdbot operations in Nix mode (configuration management, environment detection). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chronicuser21](https://clawhub.ai/user/chronicuser21) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to help an agent recognize Nix-managed Clawdbot environments, avoid unsupported auto-install flows, and provide Nix-appropriate configuration and troubleshooting guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Nix-mode guidance may be inaccurate if the runtime is not actually using the expected Nix-mode environment and config/state paths. <br>
Mitigation: Confirm CLAWDBOT_NIX_MODE, CLAWDBOT_CONFIG_PATH, CLAWDBOT_STATE_DIR, and local Nix package-management expectations before applying the guidance. <br>
Risk: The skill can steer an agent away from auto-install flows, which may be inappropriate outside a Nix-managed installation. <br>
Mitigation: Use this skill for Nix-managed environments; outside Nix mode, follow the normal dependency installation and configuration workflow. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Configuration guidance, Troubleshooting guidance] <br>
**Output Format:** [Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only skill; requires nix and bash, and expects CLAWDBOT_NIX_MODE for Nix-mode behavior.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
