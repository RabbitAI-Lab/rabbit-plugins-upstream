## Description:

Helps agents call LinkFox-forwarded Temu Global returns, refunds, and after-sales APIs for querying after-sales records, return orders, return addresses, labels, carriers, and related refund workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to work with Temu Global returns and refunds through the LinkFox gateway, including after-sales list/detail lookup, return logistics, return labels, carriers, and token-guided access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may contact LinkFox and Temu services while handling Temu seller tokens.

Mitigation: Install only where those network contacts are acceptable, prefer pre-provisioned credentials, and use short-lived or scoped tokens where possible.

Risk: The skill can store full API responses locally, which may include seller, order, return, refund, or logistics data.

Mitigation: Run it in a dedicated workspace and review retained response files before sharing or archiving the workspace.

Risk: The bundled generic proxy, token-printing, account onboarding, billing, and payment/order helpers expand the actions available beyond simple returns and refunds lookup.

Mitigation: Avoid generic proxy, token-printing, and payment/order scripts unless the user explicitly requests that specific action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-returns-refunds-global)
- [API Reference](references/api.md)
- [Partner Global Returns & Refunds Catalog](references/partner-global-catalog.md)
- [Access Token Guide](references/access-token.md)
- [Onboarding and Billing Guide](references/onboarding.md)
- [Temu Partner Global Documentation](https://partner-global.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON API parameters, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full API responses under the current workspace and may print either full JSON or a summarized response depending on response size.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
