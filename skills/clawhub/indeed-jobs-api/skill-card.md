## Description:

Search Indeed job postings, pull one posting in full with its original ATS link, and read employer profiles and employee reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and labour-market analysts use this skill to retrieve structured Indeed job postings, full job details, employer profiles, and employee reviews through Scavio APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and sends job-search terms, locations, job IDs, and company identifiers to Scavio.

Mitigation: Use a scoped environment variable for SCAVIO_API_KEY, avoid committing credentials, and only submit search or company data intended for Scavio processing.

Risk: Indeed endpoints consume credits, including empty results, paginated searches, review pages, and billed 404 responses.

Mitigation: Cap loops and pagination, state expected credit spend before broad searches, and re-derive job keys or company slugs from search results before retrying.

Risk: Unsupported radius or max_age_days values can be ignored by Indeed while still returning a billable response.

Mitigation: Use only the documented closed sets for radius and max_age_days, and disclose any rounding before making a request.

Risk: Salary filters may use Indeed estimates, and employee reviews are self-reported.

Mitigation: Label estimated salaries as estimates, check salary_source before presenting figures, and attribute reviews and aggregate sentiment to employee reports.

Risk: Server-resolved import provenance is unavailable for this release.

Mitigation: Review the packaged artifact and recorded file hash before deployment instead of inferring repository provenance from the skill text.

## Reference(s):

- [Scavio Indeed API documentation](https://scavio.dev/docs/indeed-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=indeed-jobs-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=indeed-jobs-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/indeed-jobs-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell and SDK examples plus structured JSON API response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns Scavio API response envelopes with data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
