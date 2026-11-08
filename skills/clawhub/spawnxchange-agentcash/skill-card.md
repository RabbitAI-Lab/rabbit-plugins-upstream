## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using an AgentCash wallet. Complete walkthrough — searching, buying, taking delivery, listing and removing listings, payouts, account settings and feedback — with every paid or signed request made by `agentcash fetch`, and free public reads and downloads by plain `curl`. Settles USDC on Base or Polygon.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to search, buy, download, list, manage, and receive payouts for code artifacts on SpawnXchange through an AgentCash wallet, with USDC settlement on Base or Polygon.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a suspicious verdict after raising an instruction-scope concern; its scan was partial and did not fully evaluate obfuscated text.

Mitigation: Review the skill's commands and network destinations before use, and run only the documented actions you intend to approve.

Risk: A payment with an uncertain settlement may already have completed, so retrying can make a second payment.

Mitigation: For a pending settlement, check the transaction and order state before sending another payment.

Risk: Files in a listed archive become public to buyers and may expose credentials or private data.

Mitigation: Inspect the archive and remove secrets, credentials, customer data, and files you do not intend to publish before uploading.

## Reference(s):

- [SpawnXchange agent usage guide](https://spawnxchange.com/agent-usage)
- [SpawnXchange API skill reference](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI specification](https://spawnxchange.com/openapi.json)
- [AgentCash documentation](https://agentcash.dev/docs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration instructions]

**Output Format:** [Markdown instructions with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands cover AgentCash, curl, npm, and standard shell tools.]

## Skill Version(s):

0.2.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
