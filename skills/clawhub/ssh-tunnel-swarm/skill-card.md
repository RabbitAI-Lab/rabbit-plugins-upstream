## Description: <br>
Bash tool that spins up and holds open many concurrent SSH tunnels, both forward (-L) and reverse (-R), from a plain-text rules file with key-based SSH, reconnect loops, and environment-variable configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to configure and run multiple persistent SSH forward and reverse tunnels across one or more hosts from a single rules file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The one-line installer pipes an unpinned remote GitHub script directly into bash. <br>
Mitigation: Avoid or review the remote installer before execution; prefer cloning the repository or downloading a pinned release and inspecting the script first. <br>
Risk: Forward and reverse SSH tunnels can expose local or remote services to hosts and networks named in the rules file. <br>
Mitigation: Create tunnel rules only for trusted hosts and services, keep StrictHostKeyChecking enabled, and review reverse tunnels before exposing local services. <br>
Risk: The tool reads SSH private key paths from the rules file and uses those keys to open long-running connections. <br>
Mitigation: Keep private keys and rules files permission-restricted, avoid committing them to repositories, and use dedicated keys with limited access where practical. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/ssh-tunnel-swarm) <br>
- [Setup and configuration reference](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes rules-file syntax, environment variables, SSH tunnel behavior, and operational cautions.] <br>

## Skill Version(s): <br>
1.4.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
