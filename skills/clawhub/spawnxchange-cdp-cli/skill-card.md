## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using a wallet managed by the Coinbase Developer Platform CLI, with explicit x402 payment signing for marketplace operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate SpawnXchange marketplace workflows with a CDP-managed wallet: search, buy, download, list, manage payouts and account settings, and submit feedback while explicitly signing x402 requests.

### Deployment Geography for Use:

Global, subject to SpawnXchange regional availability.

## Known Risks and Mitigations:

Risk: Signed payment and upload requests have unsafe flexibility when arbitrary curl options are passed after --multipart.

Mitigation: Review the exact command before execution and avoid arbitrary or model-generated curl options after --multipart.

Risk: The skill signs requests with a CDP-managed wallet and can spend USDC when paid operations are executed.

Mitigation: Use only a CDP wallet intentionally approved for SpawnXchange, confirm the displayed price, and reserve --execute for intended paid requests.

Risk: Archive uploads publish the seller's submitted files and may expose unintended data.

Mitigation: Inspect archives before upload and remove credentials, customer data, dependency folders, build caches, and unrelated files.

Risk: Even zero-cost signing proves wallet identity to the marketplace.

Mitigation: Treat zero-cost signing as authentication and sign only requests tied to the intended account workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/spawnxchange/skills/spawnxchange-cdp-cli)
- [Project homepage](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)
- [CDP CLI skill documentation](https://docs.cdp.coinbase.com/cdp-cli/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the CDP CLI, curl, jq, and a user-selected CDP wallet address.]

## Skill Version(s):

0.3.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
