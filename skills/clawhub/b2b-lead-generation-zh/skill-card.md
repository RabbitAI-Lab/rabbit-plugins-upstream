## Description:

B2B lead generation skill that combines customs trade intelligence, global company due diligence, and LinkedIn professional-network data to help agents analyze markets, inspect companies, identify decision makers, and support cross-border buyer or supplier discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External B2B sales, export, sourcing, and procurement users can use this skill to size product markets by HS code, review company trade activity, find buyers or suppliers, and enrich company or person records with employee, shareholder, UBO, colleague, alumni, work-history, and education context. Agents use it to route user intent to UpKuaJing API-backed scripts, return concise findings, and guide paid lookups with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid API calls can spend account balance during lead searches, enrichment, account actions, and paginated lookups.

Mitigation: Require clear user confirmation before paid calls, use the pricing endpoint or published pricing page for current costs, and disclose multi-page query counts before execution.

Risk: The skill uses an UpKuaJing API key that may be stored in a local plaintext environment file.

Mitigation: Limit file access to the local user, prefer secured environment injection where available, avoid sharing logs or screenshots containing credentials, and rotate the key if exposure is suspected.

Risk: Lead searches and enrichment can send company identifiers, person identifiers, and search intent to UpKuaJing and can return personal contact or professional-history records.

Mitigation: Apply privacy, anti-spam, retention, and access-control rules before storing, exporting, or using returned person and contact data.

Risk: Error reports may include request identifiers and contextual details about failed calls.

Mitigation: Ask for user confirmation before submitting error reports and keep report context limited to diagnostic information needed for support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/b2b-lead-generation-zh)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing developer platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Customs analysis area API reference](references/customs-analysis-area-api.md)
- [Customs analysis HS code detail API reference](references/customs-analysis-hscode-detail-api.md)
- [Customs analysis HS code search API reference](references/customs-analysis-hscode-search-api.md)
- [Customs analysis overview API reference](references/customs-analysis-overview-api.md)
- [Customs analysis trade percent API reference](references/customs-analysis-trade-percent-api.md)
- [Customs analysis trends API reference](references/customs-analysis-trends-api.md)
- [Customs company stats API reference](references/customs-company-stats-api.md)
- [Customs company partner stats API reference](references/customs-company-partner-stats-api.md)
- [Customs company product list API reference](references/customs-company-product-list-api.md)
- [Customs company port list API reference](references/customs-company-port-list-api.md)
- [Customs overview summary API reference](references/customs-overview-summary-api.md)
- [Customs overview top N API reference](references/customs-overview-top-n-api.md)
- [Customs overview US import API reference](references/customs-overview-us-import-api.md)
- [Global company list API reference](references/global-company-list-api.md)
- [Global company person list API reference](references/global-company-person-list-api.md)
- [Company employee list API reference](references/company-employee-list-api.md)
- [Company shareholder list API reference](references/company-shareholder-list-api.md)
- [LinkedIn company list API reference](references/linkedin-company-list-api.md)
- [LinkedIn person list API reference](references/linkedin-person-list-api.md)
- [LinkedIn company employee list API reference](references/linkedin-company-employee-list-api.md)
- [LinkedIn person colleague list API reference](references/linkedin-person-colleague-list-api.md)
- [LinkedIn person alumni list API reference](references/linkedin-person-alumni-list-api.md)
- [LinkedIn person experience list API reference](references/linkedin-person-experience-list-api.md)
- [LinkedIn person education list API reference](references/linkedin-person-education-list-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown and JSON-oriented command output from API-backed Python scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search scripts may create task_data files, use cursor or task_id continuation, and require an UPKUAJING_API_KEY.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
