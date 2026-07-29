## Description: <br>
Build and run grounded business agents on agent4.io over MCP: agents, knowledge bases, load-on-demand skills, stateful Storylines, and page playbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hellojixian](https://clawhub.ai/user/hellojixian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure and manage agent4.io business agents through MCP, including grounded agents, knowledge bases, skills, Storylines, page playbooks, usage checks, and related tenant workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented installer runs a live remote shell script that changes local agent configuration. <br>
Mitigation: Review the installer before running it, or configure the MCP endpoint manually with the documented URL and X-API-Key header. <br>
Risk: The AGENT4_API_KEY authenticates local agent tooling to the tenant and may enable persistent platform changes. <br>
Mitigation: Use an API key with access you are comfortable granting, confirm the tenant with tenant_info(), and rotate the key if it is exposed. <br>
Risk: Importing private documents or publishing agents and Storylines can persist changes in the tenant. <br>
Mitigation: Review tenant, content, and publication targets before import or publish actions, and validate Storylines before publishing. <br>


## Reference(s): <br>
- [agent4.io Cookbook](https://agent4.io/cookbook) <br>
- [ClawHub skill page](https://clawhub.ai/hellojixian/skills/agent4-io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, MCP tool calls, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AGENT4_API_KEY for authenticated MCP access.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
