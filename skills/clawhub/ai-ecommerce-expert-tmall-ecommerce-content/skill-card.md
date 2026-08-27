## Description:

AI电商专家｜天猫 图片视频全内容 helps Tmall merchants and ecommerce operations teams use IMIVA MCP workflows to generate product images, detail-page content, and video assets from confirmed product materials and campaign requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External Tmall merchants, ecommerce operators, designers, paid-media teams, and agency teams use this skill to turn product assets and channel requirements into IMIVA task parameters for commercial listing, seeding, advertising, and conversion-focused content production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a mutable npm package for IMIVA MCP access.

Mitigation: Pin the npm package version before production use and review package updates before adopting them.

Risk: The helper process can pass the caller's environment to the MCP package.

Mitigation: Run it from a clean environment containing only the required MCP token and API URL.

Risk: Product media, task data, and the MCP token are handled by the IMIVA service and package.

Mitigation: Use the skill only when the publisher, package, and service are trusted for the relevant commercial product data.

Risk: Image and video task creation can consume credits.

Mitigation: Check credits, use dry runs where supported, and confirm budget limits before creating paid tasks.

## Reference(s):

- [AI电商专家 homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-tmall-ecommerce-content)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IMIVA MCP task parameters, task IDs, budget checks, and result-validation guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
