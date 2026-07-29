## Description: <br>
Bash-based skill for configuring and supervising multiple key-based SSH forward and reverse tunnels from a plain-text rules file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to set up and maintain many SSH forward or reverse tunnels across one or more hosts from a single rules file. It is useful when tunnel sessions should reconnect automatically and be managed as a foreground process. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reverse tunnels can expose local services to remote hosts. <br>
Mitigation: Use reverse tunnel rules only with remote hosts you trust, and review each rules file before running the skill. <br>
Risk: Forward tunnels can expose remote services through the local machine. <br>
Mitigation: Forward only services and networks you are authorized to access, and bind local interfaces narrowly when possible. <br>
Risk: The rules file references SSH private key paths and the tool reconnects until stopped. <br>
Mitigation: Keep key files and rules files out of world-readable locations and source control, use tight key permissions, and stop the process when persistent tunnels are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/ssh-tunnel-swarm) <br>
- [Setup and configuration reference](artifact/references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell commands and plain-text configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides creation of SSH tunnel rules and environment-variable based invocation; it does not produce files on its own.] <br>

## Skill Version(s): <br>
1.4.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
