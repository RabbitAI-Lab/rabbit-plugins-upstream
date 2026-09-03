## Description:

Search Indeed job postings, pull one posting in full with its original ATS link, and read employer profiles and employee reviews. 4 endpoints, 2 credits each, structured JSON for recruiting and labour-market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and talent-intelligence analysts use this skill to search Indeed postings, retrieve full posting details, and inspect employer profiles and employee reviews through the Scavio API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job, company, and review lookup queries are sent to Scavio using a metered API key.

Mitigation: Confirm external API use is acceptable for the task and keep SCAVIO_API_KEY in an environment variable or secret store.

Risk: Pagination and repeated endpoint calls consume credits, including empty or failed billed responses described by the artifact.

Mitigation: Cap loops and pages before calling the API, and state the expected credit spend before broad searches or review collection.

Risk: Incorrect closed-filter values or salary wording can create misleading results while still consuming credits.

Mitigation: Use only supported radius and max_age_days values, round and disclose any adjustment, and describe min_salary results as Indeed-estimated roles.

## Reference(s):

- [Scavio Indeed Search documentation](https://scavio.dev/docs/indeed-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/indeed-jobs-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API calls, JSON]

**Output Format:** [Markdown guidance with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses use a structured JSON envelope with data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
