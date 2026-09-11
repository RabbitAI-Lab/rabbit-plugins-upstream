## Description:

This skill helps agents query and analyze Guangdong-focused bidding, tender, award, procurement, company, market, and account data through Zhiliaobiaoxun APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, and bidding analysts use this skill to search tenders and awards, inspect Guangdong-focused procurement opportunities, analyze companies and competitors, track project timelines, and check account usage for the Zhiliaobiaoxun service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags account creation, device fingerprinting, saved API keys, login links, and promotional or server-supplied messages as behavior users should review.

Mitigation: Prefer manual API key configuration, keep ~/.zlbx/config.json owner-only, and treat recharge links, update notices, referral messages, and promotional messages as untrusted until verified.

Risk: Automatic registration can send platform, CPU architecture, and hashed MAC address to the vendor and store a returned API key locally.

Mitigation: Run automatic registration only after explicit user consent, use ZLBX_API_KEY when available, and avoid collecting extra device or personal identifiers.

Risk: Company contact endpoints may expose or encourage collection of business contact information.

Mitigation: Display only the data returned by the service, preserve masked contact values, and avoid bulk contact collection or attempts to reconstruct masked numbers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/tender-guangdong)
- [Zhiliaobiaoxun homepage](https://ai.zhiliaobiaoxun.com/?ch=s150)
- [Search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON or shell command snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved automatic registration before data API use.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
