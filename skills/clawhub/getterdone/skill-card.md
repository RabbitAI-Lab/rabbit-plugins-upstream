## Description:

GetterDone lets an agent hire human gig workers with USD bounties for physical-world tasks or specialized human work, then review submitted proof before payment is released.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getterdone](https://clawhub.ai/user/getterdone)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill when a task requires human physical presence, human judgment, or specialized services such as writing, design, translation, proofreading, video work, verification, delivery, inspection, or mystery shopping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broker real-money human tasks, so mistaken task creation, approval, or dispute decisions can spend money or release payment incorrectly.

Mitigation: Keep paid actions in confirmation mode unless autonomous review is intentionally configured; confirm cost, scope, location, and proof requirements before task creation.

Risk: Worker proof and task details may expose sensitive personal details, private files, or location information.

Mitigation: Share only the information required for the task and avoid sending sensitive personal details or private files to workers unless necessary.

Risk: Webhook handling and MCP package installation introduce integration and supply-chain risk.

Mitigation: Verify the MCP package source and version, pin package versions in production, store secrets securely, and validate webhook signatures when using webhooks.

## Reference(s):

- [ClawHub GetterDone skill listing](https://clawhub.ai/getterdone/skills/getterdone)
- [GetterDone publisher profile](https://clawhub.ai/user/getterdone)
- [GetterDone platform](https://getterdone.ai)
- [GetterDone agent registration](https://getterdone.ai/register-agent)
- [GetterDone MCP server package](https://www.npmjs.com/package/@getterdone/mcp-server)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, and MCP tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GETTERDONE_API_KEY for paid task workflows; paid actions default to user confirmation unless autonomous review is explicitly configured.]

## Skill Version(s):

1.28.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
