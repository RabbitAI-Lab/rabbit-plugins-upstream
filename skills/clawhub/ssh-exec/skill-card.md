## Description: <br>
Run a single command on a remote Tailscale node via SSH without opening an interactive session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to have an agent run a specific command or local script on a known remote Tailscale host over SSH, then return stdout and stderr for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables remote command execution over SSH, which can affect files, services, or data on the target host. <br>
Mitigation: Use least-privilege SSH keys and accounts, verify the host and port before execution, and review each command or local script before allowing it to run. <br>
Risk: A command sent to the wrong SSH target could expose data or change the wrong system. <br>
Mitigation: Set and verify the intended SSH target for each session, especially when using environment-driven host and port configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xejrax/skills/ssh-exec) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an ssh binary, SSH access to the target host, and explicit host and port configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
