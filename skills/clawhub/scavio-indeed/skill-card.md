## Description:

Search Indeed job postings, pull one posting in full with its original ATS link, and read employer profiles and employee reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and market-research agents use this skill to search Indeed job postings, inspect a selected posting, and retrieve employer profiles or employee reviews through Scavio's structured API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scavio API calls consume credits and transmit job-search or company-research queries to Scavio.

Mitigation: State expected credit spend before loops, cap pagination, and keep SCAVIO_API_KEY in environment variables or a secret store.

Risk: Unsupported Indeed filters may be ignored while still producing billable responses.

Mitigation: Use only documented radius and max_age_days values and tell users when values are rounded.

Risk: Salary estimates and employee reviews can be mistaken for employer-verified facts.

Mitigation: Attribute estimated salary data to Indeed and describe reviews as self-reported employee feedback.

## Reference(s):

- [Scavio Indeed Search Documentation](https://scavio.dev/docs/indeed-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON, Python, JavaScript, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio Indeed endpoints return structured JSON and consume credits per request.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
