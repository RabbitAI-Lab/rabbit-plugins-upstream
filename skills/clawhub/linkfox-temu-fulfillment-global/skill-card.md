## Description:

Temu 全球站（非 US/EU）电商履行/发货 API skill for Buy-Shipping labels, cooperative warehouse fulfillment, seller self-fulfilled shipments, logistics tracking, and related Global order-shipping workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers, ecommerce operators, and developers use this skill to manage Temu Global fulfillment through LinkFox, including label purchase, cooperative warehouse fulfillment, self-fulfilled shipment updates, pickup reservations, shipment documents, and tracking.

### Deployment Geography for Use:

Global, focused on Temu Global workflows outside the US/EU-specific fulfillment skill variants.

## Known Risks and Mitigations:

Risk: The skill handles LinkFox account credentials and Temu seller access tokens.

Mitigation: Install only when LinkFox is trusted for the seller operation, verify endpoint environment variables before use, and avoid exposing tokens in stdout, prompts, saved transcripts, or logs.

Risk: Fulfillment actions can affect live seller operations, including shipment submission, cancellation, package confirmation, file downloads, API-key generation, and paid plan ordering.

Mitigation: Require explicit user confirmation before executing operational or billing-affecting commands, and review request payloads before sending them.

Risk: Saved API responses may contain sensitive business data or personal information.

Mitigation: Treat local response files as sensitive data, limit access to the session directory, and remove files that are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-fulfillment-global)
- [Fulfillment API reference](artifact/references/api.md)
- [Global API catalog](artifact/references/partner-global-catalog.md)
- [API document index](artifact/references/apis/README.md)
- [Temu access token guide](artifact/references/access-token.md)
- [Authorization flow](artifact/references/authorization-flow.md)
- [Onboarding guide](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, JSON files]

**Output Format:** [Markdown guidance with shell commands and JSON request/response payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session directory; responses over 8 KB print summaries unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
