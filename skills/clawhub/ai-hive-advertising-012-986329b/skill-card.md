## Description:

This skill helps brand, ecommerce, agency, retail, and content marketing teams plan and produce theme-transformation advertising shorts with AI-HIVE by checking current model options and prices, preparing a work plan and sample, and requiring confirmation before paid generation, batch actions, sending, or publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, ecommerce, advertising, retail, and content marketing users use this skill to turn a product or campaign brief into an auditable AI-HIVE production flow for theme-transformation short ads. The flow produces planning artifacts, prompt guidance, model-routing steps, task records, and acceptance checks for commercially usable marketing assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables broad remote AI-HIVE MCP use and includes an environment-overridable endpoint that could send credentials to an untrusted service.

Mitigation: Use OAuth or a scoped API key, keep secrets in a managed secret store, and do not set AI_HIVE_MCP_URL unless the endpoint is trusted.

Risk: Uploads, paid generation, batch actions, sending, or publication could expose private or rights-sensitive material or incur cost.

Mitigation: Require explicit user confirmation before those actions and maintain the artifact's rights, budget, and publication checklists.

Risk: AI-HIVE model availability, parameters, prices, limits, and rules can change over time.

Mitigation: Query current AI-HIVE model information at execution time, save a price snapshot and task IDs, and avoid hard-coded model assumptions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-012-986329b)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [Original workflow implementation card](references/original-workflow.md)
- [AI-HIVE MCP login and binding guide](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API-key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and optional local JSON work orders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can guide AI-HIVE MCP use and can create a local, non-billable work order; paid generation, batch actions, sending, and publication require explicit confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
