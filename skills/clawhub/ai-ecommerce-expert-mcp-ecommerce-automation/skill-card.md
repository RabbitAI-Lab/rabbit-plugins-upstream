## Description:

AI电商专家｜MCP 电商内容自动化 helps developers, ecommerce operations teams, agent teams, and enterprise content centers connect IMIVA MCP to automate product lookup, content task creation, progress polling, and delivery management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, ecommerce operators, AI Agent teams, and enterprise content teams use this skill to connect IMIVA MCP with a local token, inspect product and credit state, create ecommerce content tasks, query task progress, and manage generated image or video delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an unpinned npm package for the IMIVA MCP client.

Mitigation: Review and pin the IMIVA npm package to a known version before deployment.

Risk: The helper process can inherit the user's full environment, which may expose unrelated local secrets.

Mitigation: Run the skill in a clean environment containing only the required MCP token and API URL.

Risk: IMIVA MCP tasks may access product data or consume account credits.

Mitigation: Require explicit confirmation before submitting paid tasks or accessing sensitive product data.

## Reference(s):

- [IMIVA AI Ecommerce Expert Homepage](https://imiva.ecpro.com/)
- [ClawHub Skill Release](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-mcp-ecommerce-automation)
- [mcp-config.example.json](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces IMIVA MCP setup guidance, task-planning instructions, JSON tool arguments, and local helper commands.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
