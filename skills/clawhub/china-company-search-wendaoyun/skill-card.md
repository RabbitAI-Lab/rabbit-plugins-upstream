## Description:

This skill helps agents query WenDaoYun for Chinese company basic information, operating information, financial information, public opinion information, and risk indicators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rose-develop](https://clawhub.ai/user/rose-develop)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts can use this skill to search for a Chinese company, confirm the intended entity, and retrieve WenDaoYun company records such as legal, operational, financial, customs, employment, customer, supplier, and risk information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The WenDaoYun API key is sensitive and may authorize API usage if exposed.

Mitigation: Store WENDAOYUN_API_KEY in the environment or a secrets manager, do not paste it into chat or logs, and rotate it through WenDaoYun if it is exposed.

Risk: Company names, identifiers, and search keywords are sent to WenDaoYun when the skill performs lookups.

Mitigation: Use the skill only when sending those query terms to WenDaoYun is acceptable for the user's workflow and data-handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rose-develop/skills/china-company-search-wendaoyun)
- [WenDaoYun API portal](https://open.wendaoyun.com/home)
- [WenDaoYun API invoke base URL](https://h5.wintaocloud.com/prod-api/api/invoke)
- [Enterprise fuzzy search reference](references/fuzzy-search-org.md)
- [Enterprise risk information reference](references/get-risk.md)
- [Enterprise risk index reference](references/get-risk-index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration guidance]

**Output Format:** [Markdown text with API request guidance and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires WENDAOYUN_API_KEY for live WenDaoYun API queries.]

## Skill Version(s):

1.2.31 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
