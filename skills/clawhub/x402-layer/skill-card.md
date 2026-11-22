## Description:

x402-layer helps agents pay for APIs with USDC and manage monetized endpoints, credits, webhooks, marketplace listings, and on-chain agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivaavimusic](https://clawhub.ai/user/ivaavimusic)

### License/Terms of Use:

MIT-0

## Use Case:

External developers can use this skill to pay for APIs, deploy and manage monetized endpoints, and operate related credits, webhooks, marketplace listings, and on-chain agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports serious payment and transaction-signing weaknesses.

Mitigation: Avoid installation or payment/signing workflows until those checks have been independently reviewed.

Risk: The assessment reports an unverified remote installer and an incomplete scan.

Mitigation: Verify the installer source and package versions before installation; do not treat the incomplete scan as evidence that unreviewed material is safe.

Risk: Some workflows can use private keys, signer keys, API keys, or personal access tokens, and the assessment notes capabilities may exceed the stated purpose.

Mitigation: Choose a specific runbook first, use read-only discovery when sufficient, and provide only the credentials needed for that workflow.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/ivaavimusic/skills/x402-layer)
- [x402 Studio](https://studio.x402layer.cc)
- [Agentic access documentation](https://docs.x402layer.cc/agentic-access/openclaw-skill)
- [Singularity MCP documentation](https://studio.x402layer.cc/docs/agentic-access/mcp-server)
- [SDK receipt documentation](https://studio.x402layer.cc/docs/developer/sdk-receipts)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance, command examples, and text or JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow-dependent; signing and owner-scoped actions require applicable credentials.]

## Skill Version(s):

1.16.0 (source: SKILL.md frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
