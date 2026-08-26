## Description:

Pull bulk Google Maps business data with radius-based filters, gather merchant contact information, analyze market density, and find distributors or overseas buyers for offline business expansion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, distribution, brand operations, and regional growth teams use this skill to find merchant leads by region, radius, industry, keyword, and contact availability. Agents can use it to prepare location-based prospect lists, resume large searches, and guide account setup, pricing checks, and top-up flows for the UpKuaJing Open Platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores UPKUAJING_API_KEY in a local plaintext .env file when configured that way.

Mitigation: Use a dedicated API key with limited exposure, protect the local account directory, and rotate the key if the machine or file may have been exposed.

Risk: Merchant search calls and account top-up flows can involve paid UpKuaJing API usage.

Mitigation: Check current pricing and obtain explicit confirmation before paid searches, large query counts, or top-up actions.

Risk: Search results are written to local task files and may contain business contact or location data.

Mitigation: Store result files only where authorized users can access them and remove task data when it is no longer needed.

Risk: User-confirmed error reports can send troubleshooting context to the UpKuaJing platform.

Mitigation: Send reports only after user approval and avoid including secrets or unnecessary personal data in the report context.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/upkuajing-map-merchants-search)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html)
- [Merchants Search API Reference](references/merchants-search-api.md)
- [Country List API Reference](references/country-list-api.md)
- [Province List API Reference](references/province-list-api.md)
- [City List API Reference](references/city-list-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands; scripts return JSON and write JSONL task result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; merchant searches may incur paid API calls and can write task metadata and result files locally.]

## Skill Version(s):

1.0.6 (source: server release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
