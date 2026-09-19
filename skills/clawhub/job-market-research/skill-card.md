## Description:

Researches job postings, hiring signals, and freelance gigs via the Crawlora API, including company career sites, ATS boards, Upwork, and Fiverr, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and recruiting teams use this skill to search public job postings, inspect current company hiring, resolve ATS boards, summarize hiring signals, and research freelance gigs or sellers through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, company slugs, gig identifiers, and freelancer identifiers are sent to Crawlora as a third-party provider.

Mitigation: Use the skill only when sharing that lookup data with Crawlora is acceptable for the task.

Risk: The Crawlora API key could be exposed if copied into commands, files, or version control.

Mitigation: Keep CRAWLORA_API_KEY in the environment and do not hardcode, pass, or commit the key.

Risk: Broader Tes resource and school-directory endpoints may exceed the intended job-market research use case.

Mitigation: Use those endpoints only when they directly match the requested research scope.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/job-market-research)
- [Crawlora Website](https://crawlora.net)
- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API requests require CRAWLORA_API_KEY and use the documented Crawlora GET endpoints.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
