## Description: <br>
Build and run grounded business agents on agent4.io over MCP — agents, knowledge bases, load-on-demand skills, stateful Storylines and page playbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hellojixian](https://clawhub.ai/user/hellojixian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to agent4.io over MCP, configure business agents, build knowledge bases, create load-on-demand skills, publish Storylines, and manage page playbooks for tenant workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a user-provided agent4.io tenant API key to create or modify remote tenant resources. <br>
Mitigation: Use a scoped and revocable key where possible, confirm the tenant before changes, and review proposed actions before execution. <br>
Risk: Agent configuration, knowledge-base content, and queries may be sent to agent4.io when the user chooses to build or run tenant resources. <br>
Mitigation: Confirm before sending private documents or creating public share links. <br>
Risk: The setup flow may use a curl-to-shell installer. <br>
Mitigation: Review the installer source before running it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hellojixian/skills/agent4-io) <br>
- [agent4.io Cookbook](https://agent4.io/cookbook) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and MCP tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an agent4.io API key for remote MCP access.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
