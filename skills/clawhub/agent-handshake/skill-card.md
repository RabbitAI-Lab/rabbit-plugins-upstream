## Description: <br>
Agent Handshake helps agents discover, register, remember, and connect to AI agent servers across local networks, cloud hosts, and NAT tunnels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lyliefeng](https://clawhub.ai/user/lyliefeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect local agent workflows to known remote AI agent servers, remember server identities, and run follow-up handshakes or commands through LAN, cloud, or tunnel endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes a VPS deployment mode that exposes an HTTP service capable of running broad file and shell commands on the target machine. <br>
Mitigation: Treat that mode as remote administrative access: avoid public exposure, use strong unique credentials, restrict network access, and review the persistent service before use. <br>
Risk: Tunnel-based access can make an agent endpoint reachable outside the local network. <br>
Mitigation: Use tunnels only when needed, stop temporary tunnels after use, and confirm the endpoint and credentials before sending tasks. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/lyliefeng/skills/agent-handshake) <br>
- [Server-resolved GitHub provenance](https://github.com/lyliefeng/agent-handshake) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, endpoint examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update server identity records, local connection configuration, and command examples for agent handshakes.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
