## Description:

This skill helps agents call LinkFox-gatewayed Temu US Returns & Refunds APIs for after-sales orders, return logistics, return labels, carrier lookup, return addresses, and refund workflow data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Temu US sellers, ecommerce operators, and developers use this skill to retrieve and process after-sales return and refund information through LinkFox scripts and API guidance. It is intended for operational workflows that need Temu store credentials, order-shipping access tokens, and Partner US Returns & Refunds endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags broad proxy, credential-management, billing, and local data-retention capabilities as suspicious enough to require review before installation.

Mitigation: Install only when the LinkFox publisher is trusted and the broader Temu gateway toolkit is needed; prefer dedicated us_returns_refunds scripts for routine returns and refunds tasks.

Risk: The skill handles LinkFox API keys and Temu access tokens, including local token storage.

Mitigation: Store tokens only on trusted machines, avoid raw token output and unmasked token listing, and rotate or remove saved tokens when they are no longer needed.

Risk: Gateway override environment variables can redirect requests away from the default LinkFox gateway.

Mitigation: Do not set gateway override variables unless the destination is controlled and expected for the task.

Risk: Scripts retain full API responses locally, which may include operational order, after-sales, or return data.

Mitigation: Review saved response files for sensitivity and clear local linkfox response directories when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-returns-refunds-us)
- [API reference](artifact/references/api.md)
- [Partner US Returns & Refunds catalog](artifact/references/partner-us-catalog.md)
- [Access token authorization guide](artifact/references/access-token.md)
- [Onboarding and account guidance](artifact/references/onboarding.md)
- [Temu Partner US documentation entry](https://partner-us.temu.com/documentation?menu_code=d3d2812d87034d35adb016972349fcb0)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON request examples, shell commands, and saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full LinkFox responses under a local linkfox session data directory and print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
