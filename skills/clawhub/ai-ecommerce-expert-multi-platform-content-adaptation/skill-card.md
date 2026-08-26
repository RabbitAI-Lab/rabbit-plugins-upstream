## Description:

Helps ecommerce, brand, and marketplace operations teams adapt product assets into channel-specific images, video prompts, and IMIVA MCP task parameters for storefront, social commerce, and cross-border publishing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand teams, agencies, and cross-border sellers use this skill to prepare verified product facts, budget checks, MCP calls, and acceptance criteria for multi-platform product image and video content adaptation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external MCP package is unpinned and may change behavior between runs.

Mitigation: Review or pin the MCP package version before deployment.

Risk: The MCP process inherits environment variables, including the IMIVA token and any other variables present in the agent runtime.

Mitigation: Run the skill in a clean environment with a scoped MCP_TOKEN and no unrelated secrets.

Risk: Automatic invocation can submit paid ecommerce content generation tasks if the agent proceeds without clear operator intent.

Mitigation: Require explicit user confirmation for model, quantity, budget, and task submission before calling generation tools.

## Reference(s):

- [IMIVA AI Ecommerce Expert](https://imiva.ecpro.com/)
- [MCP configuration example](references/mcp-config.example.json)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-multi-platform-content-adaptation)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON arguments, shell command examples, and MCP task-handling steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead an agent to submit IMIVA image or video generation tasks after user confirmation, then return task IDs, status, and result links from IMIVA.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
