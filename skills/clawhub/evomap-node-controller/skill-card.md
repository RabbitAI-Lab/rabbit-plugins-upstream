## Description: <br>
Manages EvoMap node startup, shutdown, status checks, node ID configuration, and connection troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2233admin](https://clawhub.ai/user/2233admin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to start, stop, and check EvoMap nodes on configured hosts, and to troubleshoot node IDs or connection issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use local SSH keys to run root commands on EvoMap hosts and start or stop persistent node processes. <br>
Mitigation: Install only when this host control is intended; prefer explicit user-provided configuration and confirmation for each start or stop target. <br>
Risk: The security evidence notes limited safeguards around process management and host access. <br>
Mitigation: Prefer a revised version that keeps SSH host-key checking enabled and manages node processes through systemd, pm2, or a PID file. <br>


## Reference(s): <br>
- [EvoMap Hub](https://evomap.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text or Markdown with inline shell commands and status lines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate SSH commands against configured EvoMap hosts when used by an agent with shell access.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
