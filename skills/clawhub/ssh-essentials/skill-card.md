## Description: <br>
Essential SSH commands for secure remote access, key management, tunneling, and file transfers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arnarsson](https://clawhub.ai/user/arnarsson) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and administrators use this skill as a concise SSH reference for remote access, key management, tunneling, file transfer, configuration, troubleshooting, and hardening tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Copied SSH examples could weaken connection security, such as disabling host-key checking or enabling broad forwarding behavior. <br>
Mitigation: Verify the server identity another way before bypassing host-key checks, and treat agent forwarding and tunnels as privileged operations. <br>
Risk: File synchronization commands can remove remote files when delete options are used incorrectly. <br>
Mitigation: Run rsync with --dry-run before any sync that uses --delete. <br>
Risk: Automation keys without passphrases can increase blast radius if exposed. <br>
Mitigation: Prefer passphrases or tightly scoped deploy keys for automated access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arnarsson/skills/ssh-essentials) <br>
- [Publisher profile](https://clawhub.ai/user/arnarsson) <br>
- [OpenSSH homepage](https://www.openssh.com/) <br>
- [OpenSSH manual pages](https://www.openssh.com/manual.html) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Markdown, Guidance] <br>
**Output Format:** [Markdown with inline bash and SSH configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an ssh client binary for applying command examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
