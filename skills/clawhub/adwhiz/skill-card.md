## Description:

Manage Google Ads & Meta (Facebook) Ads from your AI coding tool with 113 MCP tools for auditing, creating, and optimizing ad accounts using natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External advertisers, marketing operators, and developers use AdWhiz to connect AI coding tools to Google Ads and Meta Ads accounts for account audits, reporting, campaign creation, and confirmed campaign management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized write actions can change campaigns, budgets, targeting, audiences, and ad status.

Mitigation: Review each proposed write action before confirming it and connect only the ad accounts intended for agent-assisted management.

Risk: Customer-list workflows can upload hashed customer data when authorized.

Mitigation: Use these tools only with approved customer lists and confirm that the upload matches internal data-handling requirements.

Risk: The skill relies on a third-party hosted service with access to linked Google Ads and Meta Ads accounts.

Mitigation: Install only after deciding to trust the AdWhiz publisher and revoke account access if the skill is no longer needed.

## Reference(s):

- [AdWhiz homepage](https://adwhiz.ai)
- [AdWhiz documentation](https://adwhiz.ai/docs)
- [AdWhiz OpenAPI specification](https://mcp.adwhiz.ai/api/v1/openapi.json)
- [AdWhiz tool listing](https://mcp.adwhiz.ai/api/v1/tools)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with MCP configuration snippets and ad-account analysis or action guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ADWHIZ_API_KEY for API-key authentication; write operations depend on user confirmation and linked Google or Meta ad accounts.]

## Skill Version(s):

2.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
