## Description:

Query paginated trade-area data for a company, including country and region breakdowns with trade counts, amounts, quantities, weights, and percentages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market-analysis agents use this skill to retrieve paginated company trade-area breakdowns from UpKuaJing customs data for import-export research, country-level market presence analysis, and regional drill-downs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store or read an UpKuaJing API key from a plaintext home-directory .env file.

Mitigation: Use a scoped API key where possible, restrict local file access, rotate the key if exposed, and remove the file when the skill is no longer needed.

Risk: Company area queries and account top-up flows can incur fees or initiate billing-related actions.

Mitigation: Require explicit user confirmation before each fee-incurring query or top-up action and verify current pricing through the documented pricing command or pricing page.

Risk: Error reports may send troubleshooting context, request details, or response data to UpKuaJing.

Mitigation: Report errors only after user confirmation and avoid including secrets, private business details, or unnecessary raw response data in the report context.

Risk: API requests also contact UpKuaJing for version checks and may create a local version cache.

Mitigation: Review outbound network behavior before installation and run the skill in an environment where UpKuaJing network access and local cache writes are acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-company-area-list)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Company Area List API Reference](references/customs-company-area-list-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses may include paginated records, fee information, account balance, and request identifiers.]

## Skill Version(s):

1.0.1 (source: server evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
