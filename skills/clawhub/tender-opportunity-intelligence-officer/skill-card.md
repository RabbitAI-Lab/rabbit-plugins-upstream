## Description:

Assists agents with Chinese tender opportunity intelligence, including expiring projects, renewal opportunities, competitor activity, supplier discovery, purchaser analysis, and market monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to find tender opportunities, monitor expiring or proposed projects, analyze competitors, identify likely suppliers or purchasers, and summarize market signals from the provider's bidding APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles provider API credentials, may use a local API-key configuration file, and includes an onboarding flow that can create an account from device-derived features.

Mitigation: Prefer setting ZLBX_API_KEY through a trusted secret mechanism, require explicit user consent before auto-registration, and review local credential storage before deployment.

Risk: The skill can output auto-login recharge links and uses a third-party tender-intelligence API for account and billing state.

Mitigation: Inspect any recharge or auto-login URL before use and confirm that the organization accepts the provider's account, billing, and credential-handling flow.

Risk: The skill may process company, contact, tender, and supplier data returned by the provider API.

Mitigation: Use the contact data exactly as returned by the provider, do not attempt to reconstruct masked contact details, and avoid bulk contact export without authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/tender-opportunity-intelligence-officer)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration flow reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON request examples, API-call guidance, and shell command snippets when onboarding is required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on ZLBX_API_KEY and provider API responses; account and contact details are presented according to provider-side access controls.]

## Skill Version(s):

1.0.3 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
