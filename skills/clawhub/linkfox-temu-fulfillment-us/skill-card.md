## Description:

Temu 美国站电商履行/发货 API skill，帮助代理调用 Buy-Shipping 购标面单、合作仓履约、卖家自发货、物流跟踪和 Scan Form 等 27 个已接入接口。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers, operators, and agents use this skill to prepare and manage US fulfillment workflows, including shipping label purchase, warehouse fulfillment, self-fulfilled shipment confirmation, pickup reservations, scan forms, document retrieval, and tracking.

### Deployment Geography for Use:

United States (Temu US site)

## Known Risks and Mitigations:

Risk: The skill handles LinkFox and Temu credentials, including optional local Temu access token storage.

Mitigation: Use trusted credential channels, avoid sharing production tokens in shell commands or chats, and secure or delete the local Temu token store when it is no longer needed.

Risk: The skill can initiate fulfillment actions such as shipment creation, shipment confirmation, fulfillment cancellation, payment-related onboarding, and file downloads.

Mitigation: Require explicit human confirmation before actions that purchase labels, change shipment state, cancel fulfillment, or download documents.

Risk: Gateway or login URL overrides could route sensitive fulfillment traffic away from trusted LinkFox endpoints.

Mitigation: Use only trusted LinkFox endpoints and avoid overriding gateway-related environment variables unless the endpoint has been reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-fulfillment-us)
- [Skill definition](artifact/SKILL.md)
- [API reference](artifact/references/api.md)
- [Partner US fulfillment catalog](artifact/references/partner-us-catalog.md)
- [Fulfillment API index](artifact/references/apis/README.md)
- [Access token guide](artifact/references/access-token.md)
- [Onboarding and billing guidance](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are written under a linkfox date/session data directory; small responses print in full and large responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
