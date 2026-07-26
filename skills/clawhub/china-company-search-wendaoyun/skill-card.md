## Description: <br>
WenDaoYun company information lookup skill for querying Chinese enterprise basic information, operations, finance, public opinion, and risk indicators through the WenDaoYun API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rose-develop](https://clawhub.ai/user/rose-develop) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search for Chinese companies, confirm the intended company, and retrieve WenDaoYun records for legal, operating, financial, public-opinion, customer, supplier, employment, and risk-review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Company names, identifiers, and detailed lookup requests are sent to WenDaoYun. <br>
Mitigation: Use the skill only when WenDaoYun is an acceptable service for the lookup, and avoid sending unnecessary sensitive context. <br>
Risk: A leaked API key could allow unauthorized WenDaoYun usage. <br>
Mitigation: Keep WENDAOYUN_API_KEY private, configure it through the environment, and revoke or rotate the key if exposure is suspected. <br>
Risk: Detailed legal, risk, customer, supplier, or employment queries may be run against the wrong company. <br>
Mitigation: Review the search results and confirm the exact company before requesting detailed endpoints. <br>
Risk: API calls may consume paid quota or daily allowance. <br>
Mitigation: Review WenDaoYun costs, quotas, and remaining allowance before running detailed or repeated lookups. <br>


## Reference(s): <br>
- [WenDaoYun Open Platform](https://open.wintaocloud.com/home) <br>
- [WenDaoYun API Base Endpoint](https://h5.wintaocloud.com/prod-api/api/invoke) <br>
- [Skill Source](artifact/SKILL.md) <br>
- [fuzzy-search-org - Company Fuzzy Search](artifact/references/fuzzy-search-org.md) <br>
- [get-risk - Enterprise Risk Information](artifact/references/get-risk.md) <br>
- [get-punishments - Administrative Penalties](artifact/references/get-punishments.md) <br>
- [get-execute-info - Enforcement Information](artifact/references/get-execute-info.md) <br>
- [get-dishonest-debtors - Dishonest Debtor Information](artifact/references/get-dishonest-debtors.md) <br>
- [get-customer - Customer Query Information](artifact/references/get-customer.md) <br>
- [get-supplier - Supplier Query](artifact/references/get-supplier.md) <br>
- [get-employment-info - Enterprise Recruitment Information](artifact/references/get-employment-info.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/rose-develop/skills/china-company-search-wendaoyun) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API result summaries and inline shell configuration commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided WENDAOYUN_API_KEY and company confirmation before detailed lookups.] <br>

## Skill Version(s): <br>
1.2.29 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
