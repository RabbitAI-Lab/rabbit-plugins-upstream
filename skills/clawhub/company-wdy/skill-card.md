## Description:

WenDaoYun company information lookup skill that helps agents search companies and query basic, operational, financial, public-opinion, and risk indicators through the WenDaoYun API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rose-develop](https://clawhub.ai/user/rose-develop)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search for a company, confirm the intended entity, and retrieve business, legal-risk, finance, public-notice, and regulatory records from WenDaoYun. It is useful when an agent needs structured company intelligence while preserving user confirmation before detailed lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a user-provided WenDaoYun API key stored in WENDAOYUN_API_KEY.

Mitigation: Treat the key as sensitive, store it only in the environment, and rotate it if exposed.

Risk: Two route-table entries are marked pending and lack reference files, so those lookups may not work.

Mitigation: Use implemented routes with matching reference files until the pending route documentation is added.

Risk: Company searches can return similarly named entities.

Mitigation: Require the user to confirm the selected company before calling detailed information endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rose-develop/skills/company-wdy)
- [rose-develop ClawHub profile](https://clawhub.ai/user/rose-develop)
- [WenDaoYun Open Platform](https://open.wendaoyun.com/home)
- [Skill workflow and route table](artifact/SKILL.md)
- [Company fuzzy search reference](artifact/references/fuzzy-search-org.md)
- [Company risk reference](artifact/references/get-risk.md)
- [Administrative punishment reference](artifact/references/get-punishments.md)
- [Judgment document reference](artifact/references/get-judge-doc.md)
- [Enforcement information reference](artifact/references/get-execute-info.md)
- [Import and export credit reference](artifact/references/get-import-export-credit.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration guidance]

**Output Format:** [Markdown text with API request guidance, environment-variable setup commands, and summarized query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires WENDAOYUN_API_KEY and uses read-only GET requests against WenDaoYun endpoints.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
