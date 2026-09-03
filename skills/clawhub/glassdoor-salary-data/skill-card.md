## Description:

Resolve a company name to a Glassdoor employer id, then pull the employer profile with ratings and CEO approval, up to three full reviews, and salary percentiles by job title.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide agents through Scavio Glassdoor lookups for employer profiles, employee review summaries, workplace ratings, and salary percentiles by job title.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Scavio API key and can spend Scavio credits when an agent makes Glassdoor lookup calls.

Mitigation: Store SCAVIO_API_KEY in a secret manager or scoped environment, monitor credit usage, and have the agent confirm costly or repeated lookup workflows before running them.

Risk: Returned reviews and salary estimates are third-party data, and reviews may contain employee-authored workplace details.

Mitigation: Summarize review content, avoid attempts to identify reviewers, and label salary values as Glassdoor estimates with their currency and pay period.

Risk: Glassdoor calls can be slow or intermittently fail while still consuming credits.

Mitigation: Use the documented 180-second timeout, retry sparingly, and reuse profile-provided review and salary URLs to avoid unnecessary repeated resolution calls.

## Reference(s):

- [Scavio Glassdoor Companies Documentation](https://scavio.dev/docs/glassdoor-companies)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/glassdoor-salary-data)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline code examples and JSON response schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Glassdoor review responses are capped at three reviews, and salary results paginate at 10 job titles per page.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
