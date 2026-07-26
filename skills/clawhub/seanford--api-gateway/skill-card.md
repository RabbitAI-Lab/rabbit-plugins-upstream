## Description: <br>
Connects agents to 100+ external service APIs through Maton-managed OAuth so they can call native API endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill when an agent needs to read from or act on connected external services such as Google Workspace, Microsoft 365, GitHub, Notion, Slack, Airtable, and HubSpot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route requests to live third-party accounts through a broad API gateway, including potentially high-impact write, delete, billing, sharing, messaging, webhook, or account-administration actions. <br>
Mitigation: Use least-privilege service connections and require explicit human confirmation before high-impact actions. <br>
Risk: MATON_API_KEY and service API-key connections are sensitive secrets. <br>
Mitigation: Store credentials only in approved secret stores or environment variables, avoid logging them, and rotate them if exposed. <br>
Risk: The security evidence reports that high-impact capabilities are under-scoped and inconsistently documented. <br>
Mitigation: Review the intended service, endpoint, OAuth scope, request body, and account connection before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/seanford/skills/api-gateway) <br>
- [Maton](https://maton.ai) <br>
- [Maton API Reference](https://www.maton.ai/docs/api-reference) <br>
- [API Gateway Skill Repository](https://github.com/maton-ai/api-gateway-skill) <br>
- [Slack Routing Reference](references/slack/README.md) <br>
- [GitHub Routing Reference](references/github/README.md) <br>
- [Gmail Routing Reference](references/google-mail/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with API paths, JSON examples, and Python or shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and the MATON_API_KEY environment variable; target services require user-authorized connections.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
