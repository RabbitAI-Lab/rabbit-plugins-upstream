## Description:

Helps procurement and bidding teams search tender notices, analyze companies and markets, and track project opportunities, with Zhejiang as the default search region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, and bidding teams use the skill to find tender and award notices, research companies and competitors, and analyze purchasing trends and project opportunities. Zhejiang is the default search area unless the user specifies another region.

### Deployment Geography for Use:

China (Zhejiang is the default search region, not a geographic restriction)

## Known Risks and Mitigations:

Risk: Searches and account requests use the vendor's remote APIs.

Mitigation: Review what information will be sent to the vendor before use.

Risk: Trial-account registration can send device-derived features, including a hashed MAC address.

Mitigation: Ask for informed consent before registration; provide an existing API key instead to avoid automatic onboarding.

Risk: Automatic onboarding writes an API key to a local plaintext configuration file.

Mitigation: Prefer supplying ZLBX_API_KEY through the host's secret mechanism rather than auto-registering.

Risk: Auto-login recharge links can grant access to an account.

Mitigation: Treat generated recharge links as sensitive and avoid sharing or logging them.

Risk: Conflicting region defaults in the documentation can change the scope of an unspecified-region search.

Mitigation: Specify the intended region explicitly and state the actual search scope in the answer.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-zhejiang)
- [Vendor service](https://ai.zhiliaobiaoxun.com/?ch=s152)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account onboarding reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Shell commands, Configuration guidance]

**Output Format:** [Markdown responses with search results, analysis, and occasional setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search filters and region should be stated; some data requests use account credits.]

## Skill Version(s):

1.0.3 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
