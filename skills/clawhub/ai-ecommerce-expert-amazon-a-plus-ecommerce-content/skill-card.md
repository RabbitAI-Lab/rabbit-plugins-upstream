## Description:

Helps Amazon A+ merchants, operators, designers, advertising teams, and agency teams prepare product assets and call IMIVA MCP workflows to generate ecommerce detail-page images, product content, and video materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, brand teams, operators, designers, advertising teams, and agencies use this skill to turn verified product facts, local or HTTPS assets, channel goals, specifications, and budget constraints into IMIVA MCP task calls for Amazon A+ detail-page content. The skill also guides task tracking, result review, and follow-up iteration without requiring users to write upload, authentication, polling, or download logic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unpinned npm MCP package with an MCP token and passes the local environment to that process.

Mitigation: Review before installing, trust the IMIVA npm package before use, and run it in a clean or restricted shell containing only the required MCP_TOKEN, API_URL or IMIVA_API_URL, PATH, and basic locale variables.

Risk: Product assets and task details are sent to the IMIVA service, and image or video task creation may consume paid credits.

Mitigation: Use the skill only when sharing those assets with IMIVA is acceptable, check credits and costs before creating tasks, use video dry runs where available, and confirm model, quantity, duration, resolution, and budget with the user before submission.

Risk: Generated ecommerce media can be misleading or infringing if unsupported claims, unauthorized reference assets, trademarks, or competitor materials are used.

Mitigation: Use only user-provided or confirmed product facts, verify claims and channel requirements before publishing, and treat competitor or viral references as high-level composition guidance rather than material to copy.

## Reference(s):

- [IMIVA AI ecommerce expert homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-amazon-a-plus-ecommerce-content)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON MCP configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool parameters, task IDs, credit checks, budget confirmations, and result review criteria.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
