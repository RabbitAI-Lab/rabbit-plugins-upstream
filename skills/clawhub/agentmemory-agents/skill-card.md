## Description: <br>
How agentmemory wires into host coding agents via the connect command. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rohitg00](https://clawhub.ai/user/rohitg00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to connect agentmemory to supported host coding agents and verify that the memory server tools are available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to make persistent host coding-agent configuration changes to add agentmemory. <br>
Mitigation: Review the exact connect command, affected configuration path, and rollback or backup plan before allowing the agent to run it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rohitg00/skills/agentmemory-agents) <br>
- [Server-resolved GitHub provenance](https://github.com/rohitg00/agentmemory/tree/main/plugin/skills/agentmemory-agents) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent to run agentmemory connect for a selected host agent, restart or reload the host, and verify the available tools.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
