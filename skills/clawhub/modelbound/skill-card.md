## Description: <br>
Pull team skills, rules, and knowledge from the ModelBound hosted MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[modelbound](https://clawhub.ai/user/modelbound) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use ModelBound to search, sync, and propose reviewed updates to team-managed AI skills, rules, prompts, and knowledge from a hosted MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad ModelBound MCP access beyond basic sync and search workflows. <br>
Mitigation: Install only for trusted ModelBound workspaces and API key permissions; use read-only search and fetch workflows by default. <br>
Risk: Fetched or proposed team-managed skill files may introduce incorrect or misleading instructions. <br>
Mitigation: Review and scan fetched skills before saving or deploying them, and route skill edits through reviewable draft proposals. <br>
Risk: Write-capable actions such as uploads, webhooks, agent or eval runs, exports, deployments, and generic tool calls can change remote state. <br>
Mitigation: Require explicit user confirmation before any non-read action, and avoid direct skill updates in favor of skills.proposeDraft. <br>


## Reference(s): <br>
- [ModelBound homepage](https://clawhub.ai/modelbound/modelbound) <br>
- [ModelBound MCP recipes](reference/examples.md) <br>
- [ModelBound MCP tool index](reference/tools.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown guidance with JSON-RPC examples and fetched file content when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MODELBOUND_API_KEY; write-capable ModelBound actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
