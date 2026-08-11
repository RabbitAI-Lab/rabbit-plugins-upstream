## Description:

Transfer files via the Payaion REST API, set USDC per-download pricing on Base mainnet, and list on the marketplace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jan-blockbites](https://clawhub.ai/user/jan-blockbites)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to transfer selected files or URLs through Payaion, share download links, and optionally publish paid marketplace listings settled in USDC on Base mainnet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected local files or URL contents to Payaion.

Mitigation: Use it only for files or URLs intended for transfer, and avoid secrets, private documents, and internal data unless disclosure is deliberate.

Risk: Paid listings involve wallet/API-key flows and real USDC settlement on Base mainnet.

Mitigation: Confirm paid listing details and prefer least-privilege API keys instead of allowing an agent to mint credentials from a local wallet.

Risk: Marketplace listing metadata and download links may expose information about the uploaded asset.

Mitigation: Review generated titles, descriptions, categories, tags, pricing, and link sharing before publishing.

## Reference(s):

- [Payaion Homepage](https://payaion.com)
- [Payaion Documentation](https://payaion.com/docs)
- [Payaion Agent Flow](https://payaion.com/docs/agent-flow)
- [Payaion OpenAPI Specification](https://payaion.com/openapi.yaml)
- [ClawHub Skill Page](https://clawhub.ai/jan-blockbites/skills/payaion-transfer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses curl-based REST calls; PAYAION_API_KEY is optional for guest transfers and required for selling or buying.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
