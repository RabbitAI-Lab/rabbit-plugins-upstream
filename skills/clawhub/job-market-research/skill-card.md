## Description:

Researches job postings, hiring signals, and freelance gigs via the Crawlora API across job boards, employer career sites, ATS boards, Upwork, and Fiverr, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search public job postings, inspect company hiring activity, resolve ATS boards, aggregate hiring signals, and research freelance gigs through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the Crawlora API key and job or freelance search parameters to Crawlora.

Mitigation: Use only an intended Crawlora API key and avoid sensitive personal or confidential business information in search terms unless sharing it with Crawlora is acceptable.

Risk: Job, ATS, and freelance marketplace results are external public data and may be incomplete, stale, or subject to source terms.

Mitigation: Validate important hiring or market conclusions against the source postings and respect the applicable terms for each data source.

Risk: The helper performs API calls through a shell script and requires local environment setup.

Mitigation: Set CRAWLORA_API_KEY in the environment, keep it out of files and command arguments, and review generated shell commands before execution.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora account and API key](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/job-market-research)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses GET requests against documented Crawlora routes.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
