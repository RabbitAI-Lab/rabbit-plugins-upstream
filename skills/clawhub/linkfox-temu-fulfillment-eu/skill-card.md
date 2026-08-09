## Description:

Temu EU fulfillment skill for Buy-Shipping labels, co-warehouse fulfillment, self-fulfilled shipment updates, logistics tracking, and self-delivery proof-of-delivery workflows across 30 Partner EU fulfillment APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to run Temu Europe fulfillment tasks through LinkFox, including buying shipping labels, confirming shipment, managing pickup reservations, handling co-warehouse fulfillment, tracking packages, and uploading POD evidence.

### Deployment Geography for Use:

Europe

## Known Risks and Mitigations:

Risk: The skill can perform live fulfillment operations such as shipment creation, updates, confirmations, cancellations, pickup reservations, and POD upload through LinkFox.

Mitigation: Confirm every shipping, cancellation, pickup, payment, or proof-of-delivery action before running a script with live credentials.

Risk: The skill handles LinkFox tokens and Temu access tokens, including optional local token storage.

Mitigation: Use scoped credentials, avoid pasting real credentials into shared chats or logs, rotate exposed tokens, and review the local token store path before saving tokens.

Risk: Full API responses may be persisted to a local linkfox session data directory and can include order, shipment, or tracking details.

Mitigation: Review saved response locations, avoid sharing generated data folders, and remove stored responses that contain sensitive operational data when no longer needed.

Risk: Environment variables can override the gateway base URL, which could redirect requests away from the expected LinkFox service.

Mitigation: Use gateway URL overrides only in controlled environments and verify the target service before sending tokens or fulfillment payloads.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-fulfillment-eu)
- [Temu EU fulfillment API reference](references/api.md)
- [Partner EU fulfillment interface catalog](references/partner-eu-catalog.md)
- [Fulfillment API document index](references/apis/README.md)
- [Temu accessToken authorization and retrieval](references/access-token.md)
- [Authentication and credit onboarding](references/onboarding.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON responses, saved JSON files, stdout summaries, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are written to a linkfox session data directory; small responses print in full and large responses print summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
