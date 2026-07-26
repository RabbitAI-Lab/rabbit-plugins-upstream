## Description: <br>
Bash-based agent skill that helps developers and operators set up and use ssh-tunnel-swarm to run multiple key-based SSH forward and reverse tunnels from a rules file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure rules files and run ssh-tunnel-swarm for persistent SSH forward and reverse tunnels across one or more hosts. It is suited to managing several tunnel connections from one declarative file rather than hand-running individual ssh commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install instructions pipe a downloader from a mutable GitHub branch directly into bash. <br>
Mitigation: Download the installer to a file, inspect it, prefer a tagged release or verified checksum or signature, and execute it explicitly. <br>
Risk: Reverse tunnels can expose a local service to a remote host. <br>
Mitigation: Use reverse rules only with trusted remote hosts and bind only the local services intended for remote access. <br>
Risk: Rules files reference SSH private key paths and can connect to real hosts. <br>
Mitigation: Use only rules files that point to hosts and key files you control, keep key files permission-restricted, and avoid storing sensitive rules files in public repositories. <br>


## Reference(s): <br>
- [setup.md](references/setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/ssh-tunnel-swarm) <br>
- [GitHub repository](https://github.com/psyb0t/ssh-tunnel-swarm) <br>
- [Downloader script](https://raw.githubusercontent.com/psyb0t/ssh-tunnel-swarm/master/tools/downloader.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and rules-file configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash and ssh; tunnel behavior is controlled by RULES_FILE, LOG_ENABLED, LOG_FILE, and LOG_LEVEL.] <br>

## Skill Version(s): <br>
1.4.1-alpha (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
