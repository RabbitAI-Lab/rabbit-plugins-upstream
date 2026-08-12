## Description:

Set up server-side conversion tracking so purchases are reported accurately to Facebook, TikTok, Google and Bing despite iOS restrictions, ad blockers and cookie loss.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autonnel](https://clawhub.ai/user/autonnel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing engineers, and ecommerce operators use this skill to design, implement, and verify server-side conversion reporting for paid advertising funnels. It focuses on preserving click identifiers, attaching them to orders, sending server-to-server purchase events, deduplicating browser and server events, and reconciling platform reports against order data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server-side conversion tracking can process ad-platform tokens, click identifiers, customer identifiers, IP addresses, user agents, and hashed PII.

Mitigation: Enable it only with appropriate user consent, legal basis, retention controls, and secure handling for tokens and customer identifiers.

Risk: Production deployment may expose development secrets or unreviewed service configuration if the external repository is run as-is.

Mitigation: Review the external Autonnel repository and docker-compose.yml before production use, and replace any development secrets before public deployment.

Risk: Incorrect deduplication or click-id capture can under-report, over-report, or misattribute purchases.

Mitigation: Use shared event IDs for browser and server events, preserve click IDs across funnel steps, and verify results against the order database before scaling spend.

## Reference(s):

- [Autonnel repository](https://github.com/autonnel/autonnel)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with tables, checklists, and inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes privacy-sensitive implementation considerations for ad-platform tokens, customer identifiers, consent, and retention controls.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
