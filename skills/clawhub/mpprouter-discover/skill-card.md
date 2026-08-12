## Description:

Discover paid API services available via MPP Router (apiserver.mpprouter.dev) that accept Stellar USDC payments, fetch the live service catalog, select a matching service, and hand off to the pay-per-call sub-skill for invocation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover MPP Router services that fit a requested API task, inspect service documentation, and route paid Stellar USDC API calls through a confirmation-gated payment flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent toward real Stellar USDC charges for MPP Router services.

Mitigation: Use only when paid MPP Router calls are intended, and rely on the pay-per-call confirmation gate or an explicit auto-spend ceiling before payment.

Risk: Service catalog entries, prices, availability, and upstream documentation can change between uses.

Mitigation: Fetch the live catalog before each selection, read the matched service documentation, and avoid caching catalog results beyond the skill's stated short window.

Risk: Some services may be session-only or unverified for Stellar charge mode, which can produce failed paid calls or no upstream result.

Mitigation: Follow the skill's payment-mode decision rules: refuse session-only calls by default, warn on unverified services, and proceed only with explicit user acceptance where required.

## Reference(s):

- [MPP Router](https://www.mpprouter.dev)
- [MPP Router service catalog](https://apiserver.mpprouter.dev/v1/services/catalog)
- [Verified run audit trail](https://github.com/mpprouter/rozo-mpprouter/blob/main/docs/verified-runs.json)
- [ClawHub skill page](https://clawhub.ai/shawnmuggle/skills/mpprouter-discover)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and structured service details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe live catalog results, service documentation requirements, payment-mode caveats, and confirmation-gated payment handoff steps.]

## Skill Version(s):

1.0.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
