## Description:

Search Indeed job postings, fetch full posting details with original ATS links, and read employer profiles and employee reviews through Scavio's structured JSON API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting, talent intelligence, and labor-market research users can ask an agent to search Indeed postings, inspect a specific posting, and review employer profile or employee-review data. Developers can use the skill to produce structured API calls and JSON-oriented workflows around Scavio's Indeed endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job queries, locations, job IDs, Indeed URLs, and employer targets are sent to Scavio with the user's API key.

Mitigation: Avoid confidential recruiting targets or personally sensitive searches unless the disclosure is necessary for the task.

Risk: Each endpoint call consumes Scavio credits, including empty responses and billed lookup failures described by the skill.

Mitigation: Cap search and review loops, state expected credit use before running repeated requests, and re-derive job IDs or company slugs from prior results before retrying.

Risk: Indeed filter behavior can produce misleading or broader paid searches when unsupported radius or posting-age values are used.

Mitigation: Use only the documented closed filter values and tell the user when a requested value is rounded to a supported option.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/indeed-jobs-api)
- [Scavio Indeed Search documentation](https://scavio.dev/docs/indeed-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [Scavio API](https://api.scavio.dev)
- [Publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON, API calls]

**Output Format:** [Markdown guidance with code examples and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns guidance for four Scavio Indeed endpoints; each endpoint request consumes credits.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
