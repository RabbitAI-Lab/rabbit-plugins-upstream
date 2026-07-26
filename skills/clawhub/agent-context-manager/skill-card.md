## Description: <br>
Agent Context Manager helps agents create, organize, fetch, update, archive, clone, and version reusable AgentPMT context documents for shared knowledge such as brand guidance, SOPs, product facts, pricing rules, and policies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use this skill to let agents manage shared AgentPMT context documents that are reused across workflows. It is suited for maintaining brand voice, SOPs, product facts, pricing rules, policy documents, public templates, and version history from one controlled source. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create, update, archive, and request_unlock actions can persist changes to context documents that downstream agents and workflows may reuse. <br>
Mitigation: Confirm the target document and intended change before allowing mutating actions, and review retained versions before or after large edits. <br>
Risk: The skill depends on authenticated AgentPMT MCP or REST access for remote tool calls. <br>
Mitigation: Use the referenced AgentPMT setup skill for credential handling and keep account secrets, wallet keys, signatures, and payment headers out of prompts and logs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/agent-context-manager) <br>
- [AgentPMT Marketplace Page](https://www.agentpmt.com/marketplace/agent-context-manager) <br>
- [Agent Context Manager Schema](schema.md) <br>
- [What AgentPMT Is](https://clawhub.ai/agentpmt/what-is-agentpmt) <br>
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance, API calls] <br>
**Output Format:** [Markdown guidance with JSON request examples and action schemas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [AgentPMT tool and API calls return JSON responses; the skill itself declares no local command runtime.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
