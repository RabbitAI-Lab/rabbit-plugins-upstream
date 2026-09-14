## Description:

Researches job postings, hiring signals, and freelance gigs via the Crawlora API across major career sites, ATS boards, Upwork, and Fiverr, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, analysts, and agents use this skill to search public job postings, inspect company ATS boards, assess hiring signals, and research freelance gigs through normalized Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends job, company, and freelance search terms to Crawlora using the user's API key.

Mitigation: Use the skill only for searches appropriate to share with Crawlora, keep CRAWLORA_API_KEY in the environment, and do not hardcode or commit the key.

Risk: Release evidence flags extra authenticated routes and POST behavior that are not clearly scoped to the stated job-market purpose.

Mitigation: Review the route catalog before installation and prefer a version that removes unneeded POST support and non-job-market routes.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/job-market-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses are normalized JSON and may be paginated.]

## Skill Version(s):

1.0.16 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
