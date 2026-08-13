## Description:

Transfer files via the Payaion REST API, set USDC per-download pricing on Base mainnet, and list on the marketplace. Use for agent-to-human, agent-to-agent, and agent-to-marketplace file flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jan-blockbites](https://clawhub.ai/user/jan-blockbites)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw agents use this skill to upload local files or URL-sourced files to Payaion, share download links, and optionally create paid marketplace listings. It supports agent-to-human, agent-to-agent, and agent-to-marketplace file transfer workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected files to Payaion and manage uploaded files.

Mitigation: Be explicit about which file or upload ID the agent should upload, share, list, refresh, or delete.

Risk: Paid marketplace listings can publish generated titles, descriptions, tags, categories, and per-download pricing.

Mitigation: Review marketplace metadata and confirm pricing before creating paid listings.

Risk: The skill uses the PAYAION_API_KEY environment variable for authenticated uploads, selling, buying, and account-scoped limits.

Mitigation: Install only when the agent should interact with Payaion on the user's behalf, and restrict the key to the intended account and scopes.

## Reference(s):

- [Payaion homepage](https://payaion.com)
- [Payaion dashboard and API keys](https://payaion.com/dashboard)
- [Payaion agent flow documentation](https://payaion.com/docs/agent-flow)
- [Payaion OpenAPI specification](https://payaion.com/openapi.yaml)
- [ClawHub skill page](https://clawhub.ai/jan-blockbites/skills/payaion-transfer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include upload IDs, download URLs, marketplace URLs, status values, pricing details, and error guidance.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
