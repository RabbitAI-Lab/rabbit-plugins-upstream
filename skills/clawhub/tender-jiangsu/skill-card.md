## Description:

Helps agents search and analyze tender notices, project timelines, suppliers, company records, and bid pricing, with Jiangsu as the default search region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and bidding teams use this skill to find tender opportunities, review project and company histories, compare suppliers, and analyze bidding trends. Jiangsu is the default search region, but users can specify another region.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trial registration may send a hashed MAC-derived device identifier to the provider and create an account.

Mitigation: Request informed consent before registration; configure ZLBX_API_KEY manually to avoid the automatic registration flow.

Risk: Automatic registration saves an API key in a local configuration file.

Mitigation: Protect the local key and avoid sharing it in reports or logs; use an environment variable if local key creation is unwanted.

Risk: Provider responses may include business contact information.

Mitigation: Share contact details only as needed for the user's authorized procurement task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-jiangsu)
- [Provider website](https://ai.zhiliaobiaoxun.com/?ch=s151)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Registration and API key guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown with tender results and analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API-backed results; requires ZLBX_API_KEY or an account registration flow.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
