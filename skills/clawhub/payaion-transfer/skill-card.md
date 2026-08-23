## Description:

Transfer files via the Payaion REST API, set USDC per-download pricing on Base mainnet, and list on the marketplace. Use for agent-to-human, agent-to-agent, and agent-to-marketplace file flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jan-blockbites](https://clawhub.ai/user/jan-blockbites)

### License/Terms of Use:

MIT-0

## Use Case:

External OpenClaw agents use this skill to transfer local files or URLs through Payaion, share download links, and optionally create paid marketplace listings settled in USDC on Base mainnet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send selected local files or URLs to Payaion.

Mitigation: Confirm the exact file or URL before transfer, and avoid sensitive paths unless the user explicitly intends to upload them.

Risk: Paid marketplace flows can expose an item publicly with a price and payout destination.

Mitigation: Confirm the file, price, payout address, and public listing intent before using paid listing flows.

Risk: Deleting a storage folder does not delete the files inside it; files move back to the storage root.

Mitigation: Use the upload delete operation when the goal is to remove a file, and use folder deletion only for organization changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jan-blockbites/skills/payaion-transfer)
- [Payaion homepage](https://payaion.com)
- [Payaion documentation](https://payaion.com/docs)
- [Payaion agent flow documentation](https://payaion.com/docs/agent-flow)
- [Payaion OpenAPI specification](https://payaion.com/openapi.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl commands, JSON response interpretation, and concise transfer status reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and optionally PAYAION_API_KEY; outputs may include external Payaion download or marketplace URLs.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
