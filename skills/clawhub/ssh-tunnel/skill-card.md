## Description: <br>
SSH tunneling, port forwarding, and remote access patterns for local, remote, and dynamic forwards, jump hosts, SSH key management, file transfer, and connection debugging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to draft and adapt SSH commands and configuration for tunneling, jump hosts, key management, secure file transfer, and connection troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote forwards bound to 0.0.0.0 can expose local services to remote networks. <br>
Mitigation: Use remote exposure only when intended, prefer localhost-bound forwards, and confirm server GatewayPorts settings before running commands. <br>
Risk: Disabling host-key checks can hide server identity changes during troubleshooting. <br>
Mitigation: Keep host-key checking enabled for normal use and disable it only in controlled troubleshooting contexts. <br>
Risk: SSH agent forwarding can let an untrusted remote host use the local agent for authentication. <br>
Mitigation: Forward agents only to trusted hosts and prefer ProxyJump when possible. <br>
Risk: Background tunnels may continue running after the immediate task is finished. <br>
Mitigation: Track and stop background tunnel sessions when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gitgoodordietrying/skills/ssh-tunnel) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/gitgoodordietrying) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with SSH command examples and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the ssh command-line tool; examples should be reviewed and adapted before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
