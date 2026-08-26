## Description:

Search global companies by name, industry, product, and website URL, and gather firmographic data for supplier research, target-market research, and overseas lead generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sales teams, exporters, supplier researchers, and B2B lead-generation specialists use this skill to search global company records, discover target accounts, and enrich firmographic data from the UpKuaJing Open Platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores the UpKuaJing service API key in a plaintext home-directory file.

Mitigation: Use a dedicated API key, restrict local file permissions on ~/.upkuajing/.env, and rotate the key if it may have been exposed.

Risk: Company searches and account actions may incur fees or create top-up payment links.

Mitigation: Confirm expected costs and user approval before paid searches, large result requests, or top-up workflows.

Risk: Error reports can include request context or response details.

Mitigation: Send error reports only after user confirmation and avoid including sensitive request or response data.

Risk: The skill performs a daily version-check network call and writes local version cache data.

Mitigation: Review this behavior before installation in restricted environments and monitor local ~/.upkuajing cache files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/global-company-search)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html)
- [Global Company List API](artifact/references/global-company-list-api.md)
- [Skill Error Report API](artifact/references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands and JSON or JSONL script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company search results are saved to task result files; API calls require UPKUAJING_API_KEY and may incur fees.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
