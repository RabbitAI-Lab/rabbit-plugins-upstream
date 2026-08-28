## Description:

Searches LinkedIn-derived person records through Upkuajing APIs using filters such as name, company, title, industry, location, and contact availability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, and B2B lead builders use this skill to find LinkedIn-derived people records and continue larger searches through saved task results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid API calls can incur costs during LinkedIn-derived person searches.

Mitigation: Confirm costs and user intent before searches, especially when query_count requires multiple API calls; use the price endpoint or pricing page for current pricing.

Risk: The Upkuajing API key is a secret stored in the environment or ~/.upkuajing/.env.

Mitigation: Protect the file and environment variable, avoid sharing the key, and rotate it if exposure is suspected.

Risk: Search results can include contact-related person data saved in task_data files.

Mitigation: Limit searches to legitimate recruiting, sales, or lead-generation needs and delete task_data results when no longer needed.

Risk: Error reports may include request context that could contain sensitive details.

Mitigation: Review report content before submission and avoid sending unnecessary sensitive details.

## Reference(s):

- [LinkedIn person list API reference](references/linkedin-person-list-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)
- [Upkuajing homepage](https://www.upkuajing.com)
- [Upkuajing developer portal](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files]

**Output Format:** [JSON responses and JSONL task result files, with human-facing guidance before paid operations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are saved under task_data with task metadata for pagination and continuation.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
