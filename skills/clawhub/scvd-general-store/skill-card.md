## Description:

SCVD General Store guides agents through a live x402 commerce and verification service for testing real payments, checking signed offers and receipts, and accessing SCVD store APIs, MCP endpoints, and browser workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill to test and verify x402 payment flows against a live store, inspect conformance and signed artifacts, and choose the right SCVD endpoint or tool path before spending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill points agents at a live x402 store where payments are real, not sandboxed.

Mitigation: Use wallet spend controls, confirm prices from the live menu, and require user-directed signing before payment.

Risk: The skill references a separate scvd-tab npm package for an MCP server running on the user's machine.

Mitigation: Review the scvd-tab package before adding that MCP server to an agent environment.

Risk: Wallet secrets, credentials, or private keys could be exposed if a caller ignores the stated consent boundaries.

Mitigation: Do not provide secrets to the store or skill flows; use only wallet-mediated signing and explicit user consent.

## Reference(s):

- [SCVD Store Homepage](https://scvd.store)
- [ClawHub Skill Page](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [SCVD OpenAPI Specification](https://scvd.store/openapi.json)
- [SCVD Live Menu](https://scvd.store/menu.json)
- [x402 Conformance Vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json)
- [SCVD Attestation Model](https://scvd.store/attestation)
- [SCVD Criteria](https://scvd.store/criteria)
- [SCVD Browser and Six-Door Checks](https://github.com/seancrecord/scvd-general-store-repo/blob/main/SIX_DOORS.md)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Configuration]

**Output Format:** [Markdown with inline HTTP requests, JSON snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes live-service guidance; prices and stock should be confirmed from the live menu before payment.]

## Skill Version(s):

3.15.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
