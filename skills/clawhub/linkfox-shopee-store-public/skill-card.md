## Description:

Provides agent guidance and Python scripts for calling six Shopee Open Platform Public APIs through LinkFox's developer proxy, including authorized shop and merchant listing, OAuth token exchange and refresh, resend-code token retrieval, and Shopee IP range lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and e-commerce operators use this skill to call Shopee Public module endpoints from an agent workflow for partner shop or merchant discovery, token exchange and refresh, resend-code token retrieval, and Shopee IP allowlist lookup. It also guides users through LinkFox API key setup, dependency checks, and billing/authentication remediation when gateway calls fail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Shopee and LinkFox tokens, phone-login onboarding, billing orders, and locally stored API responses.

Mitigation: Use it only in workspaces where local response storage is acceptable, avoid pasting real tokens into chat or logs, and review saved response files according to workspace data-handling policy.

Risk: Custom LinkFox gateway or login URL environment variables can redirect API, login, or token traffic.

Mitigation: Keep the default LinkFox endpoints unless the replacement destination is fully trusted and intentionally configured.

Risk: Onboarding and billing helpers may initiate account setup, plan selection, payment order creation, or order-status checks.

Mitigation: Prefer self-service account setup at the LinkFox site when possible and have the user review plan, payment method, and order details before continuing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-public)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Public module API reference](artifact/references/api.md)
- [Onboarding and auth guidance](artifact/references/onboarding.md)
- [Shopee get_shops_by_partner documentation](https://open.shopee.com/documents/v2/v2.public.get_shops_by_partner?module=104&type=1)
- [Shopee get_access_token documentation](https://open.shopee.com/documents/v2/v2.public.get_access_token?module=104&type=1)
- [Shopee refresh_access_token documentation](https://open.shopee.com/documents/v2/v2.public.refresh_access_token?module=104&type=1)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with Python shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session directory; small responses print as JSON, large responses print summaries unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
