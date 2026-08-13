## Description:

Search Indeed job postings, pull one posting in full with its original ATS link, and read employer profiles and employee reviews. 4 endpoints, 2 credits each, structured JSON for recruiting and labour-market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and talent-intelligence analysts use this skill to query Indeed postings, inspect individual jobs, and review employer profiles and employee reviews through Scavio's structured API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job-search, employer-review, and recruiting queries are sent to Scavio as a third-party service.

Mitigation: Avoid sending confidential recruiting plans, sensitive employer investigations, or personally identifying job-search details unless those query values are intended to be shared with Scavio and its upstream data path.

Risk: Indeed filter behavior can silently ignore unsupported radius or posting-age values while still charging credits.

Mitigation: Use only the documented closed filter values, round unsupported user values before making requests, and state any rounding to the user.

Risk: Search pages, review pages, missing jobs, and missing company slugs can each consume credits.

Mitigation: Cap loops, state expected spend before multi-page calls, and re-derive job keys or company slugs from search results instead of retrying billed failures.

## Reference(s):

- [Scavio Indeed Search Documentation](https://scavio.dev/docs/indeed-search)
- [Scavio Rate Limits Documentation](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-indeed)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API Calls, Configuration]

**Output Format:** [Markdown with JSON, Python, JavaScript, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide agents to call Scavio endpoints that return structured JSON for Indeed jobs, employers, and reviews.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
