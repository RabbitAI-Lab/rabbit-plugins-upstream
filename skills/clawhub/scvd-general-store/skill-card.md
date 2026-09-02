## Description:

SCVD General Store helps agents and developers practice live x402 commerce against scvd.store, verify signed offers and receipts, and inspect signed observations of endpoint and payment behavior across API, MCP, browser automation, and WebMCP entry points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent builders, and external evaluators use this skill to test x402 clients against real settlement flows, run free conformance and preflight checks, and optionally buy signed artifacts or endpoint observations from scvd.store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid x402 endpoints perform real settlement with no sandbox.

Mitigation: Review prices, wallet prompts, and payment terms before approving signatures or purchases; prefer free preflight and conformance checks before spending.

Risk: Submitted text, callback URLs, public records, and stable artifacts may persist or be visible after use.

Mitigation: Avoid sensitive inputs, review callback URLs, and confirm what will be recorded before submitting text or buying signed artifacts.

Risk: Retry loops can cause duplicate payment attempts if the client does not preserve idempotency.

Mitigation: Use the idempotency key guidance from the skill and keep agent spend controls active when testing live x402 flows.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [SCVD General Store homepage](https://scvd.store)
- [SCVD OpenAPI specification](https://scvd.store/openapi.json)
- [SCVD menu and listing data](https://scvd.store/menu.json)
- [x402 conformance vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json)
- [SCVD attestation model](https://scvd.store/attestation)
- [SCVD trust panel](https://scvd.store/trust)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline HTTP requests, JSON snippets, and shell or configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes user-directed live payment flows, free verification flows, browser/WebMCP notes, and MCP server usage details.]

## Skill Version(s):

3.8.0 (source: server release metadata, created 2026-08-31)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
