## Description:

SCVD General Store helps agents and developers practice live x402 payments, check signed offer and receipt conformance, and request signed observations or artifacts from scvd.store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to test x402 clients against live payment endpoints, inspect conformance of signed offers and receipts, recover or verify purchases, and request signed observations through HTTP, browser, WebMCP, or MCP routes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid actions are real USDC transfers rather than sandbox transactions.

Mitigation: Review each quote before signing, rely on buyer-authorized wallet action, and use the provided idempotency guidance for retries.

Risk: Wallet keys, credentials, or secrets could be exposed if placed in prompts, skill context, or MCP server environments.

Mitigation: Keep wallet keys and secrets outside the skill and MCP environments; do not use tools that ask for credentials or wallet secrets.

Risk: Public memory anchors can preserve sensitive data in a retrievable record.

Mitigation: Do not place passwords, private keys, seed phrases, access tokens, personal data, or confidential business information into anchors; review summaries before submission.

Risk: The optional scvd-tab MCP server is local code execution and reads a local JSONL file.

Mitigation: Install the pinned scvd-tab version, verify npm provenance when possible, and run it with no secrets in its environment and access only to the needed local file.

## Reference(s):

- [SCVD General Store on ClawHub](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [SCVD Store](https://scvd.store)
- [SCVD Store OpenAPI](https://scvd.store/openapi.json)
- [SCVD Store Menu](https://scvd.store/menu.json)
- [x402 Conformance Vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json)
- [Six Doors Report](https://github.com/seancrecord/scvd-general-store-repo/blob/main/SIX_DOORS.md)
- [SCVD Criteria](https://scvd.store/criteria)
- [SCVD Attestation](https://scvd.store/attestation)
- [SCVD Rights](https://scvd.store/rights)
- [scvd-tab Source Directory](https://github.com/seancrecord/scvd-general-store-repo/tree/main/tab)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with HTTPS examples, JSON request bodies, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference real x402 payments; paid actions require external wallet authorization.]

## Skill Version(s):

3.16.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
