## Description: <br>
Connect an agent to the Tulimoa MCP gateway, a remote EU-hosted endpoint that federates connected SaaS tools and provides persistent memory across turns and sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[florianbaraz](https://clawhub.ai/user/florianbaraz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to connect an agent to Tulimoa's remote MCP gateway, federate connected SaaS tools, and preserve working memory across turns and sessions. <br>

### Deployment Geography for Use: <br>
Global; memory storage is described as EU-hosted. <br>

## Known Risks and Mitigations: <br>
Risk: Persistent gateway memory may retain sensitive context beyond a single conversation. <br>
Mitigation: Avoid storing secrets or regulated data, store references instead of credentials, and use the provided forget, export, and erase controls when memory should not persist. <br>
Risk: Federating connected SaaS tools through one gateway can broaden the agent's data access. <br>
Mitigation: Review connected SaaS tools in the Tulimoa dashboard and use scoped read/write gateway keys appropriate to the task. <br>


## Reference(s): <br>
- [Tulimoa Gateway homepage](https://tulimoa.com/gateway) <br>
- [Tulimoa MCP gateway endpoint](https://gateway.tulimoa.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, API calls, Text] <br>
**Output Format:** [Markdown guidance plus MCP tool calls and text or structured tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The remote gateway can return remembered context, SaaS tool results, and deduplicated result pointers for later retrieval.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
