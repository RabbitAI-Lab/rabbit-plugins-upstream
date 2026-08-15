## Description:

Supports Temu US fulfillment workflows through LinkFox, including buy-shipping labels, cooperative warehouse fulfillment, seller self-fulfilled shipments, scan forms, pickup reservations, and tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to prepare and manage Temu US fulfillment actions such as purchasing shipping labels, confirming shipments, creating scan forms, managing pickup reservations, and checking tracking information through LinkFox gateway scripts.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Credential and token exposure through LinkFox API keys, Temu access tokens, and local token storage.

Mitigation: Use least-privilege Temu and LinkFox credentials, avoid shared machines, restrict access to saved token files, and treat all access tokens and API keys as sensitive.

Risk: High-impact fulfillment, shipping, billing, and token-generation actions may affect orders, labels, pickups, scan forms, payments, or account access.

Mitigation: Confirm every label purchase, fulfillment submit or cancel, shipment confirmation, pickup reservation, scan form creation, payment order, and token-generation step before execution.

Risk: Saved full API responses can contain sensitive order identifiers, labels, tracking data, or business records.

Mitigation: Review where response files are written, limit workspace access, remove sensitive saved files when no longer needed, and disable automatic persistence if it is not required.

Risk: Generic proxy and onboarding/payment scripts broaden the actions available to the agent beyond a single fulfillment task.

Mitigation: Remove or disable the generic proxy, onboarding/payment scripts, plaintext token store, and automatic full-response persistence when they are not needed for the deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-fulfillment-us)
- [Temu fulfillment API reference](references/api.md)
- [Fulfillment API index](references/apis/README.md)
- [Partner US catalog](references/partner-us-catalog.md)
- [Temu accessToken authorization and storage](references/access-token.md)
- [LinkFox onboarding and account setup](references/onboarding.md)
- [Temu Partner US documentation](https://partner-us.temu.com/documentation?menu_code=fd19c5c9a430407a8c587d7f3e492c4a&sub_menu_code=085d46b8a6604228b371e0706ac4af7d)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash snippets and JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses under a local linkfox session data directory; large responses print summaries unless --inline is used.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
