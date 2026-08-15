## Description:

Researches job postings, hiring signals, and freelance gigs via the Crawlora API - Indeed, Google/Amazon/Apple/Meta/Tesla careers sites, any company's ATS board (Greenhouse, Lever, Workday, SmartRecruiters, Ashby, and more), plus Upwork and Fiverr - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, and developers use this skill to search job postings, resolve company ATS boards, summarize hiring signals, and research freelance gigs from public job and marketplace sources through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key and request data to arbitrary API paths or to a base URL overridden with CRAWLORA_API_BASE.

Mitigation: Keep CRAWLORA_API_BASE unset or set only to https://api.crawlora.net/api/v1, and review requested paths before execution.

Risk: Queries and POST bodies may contain sensitive private text that would be sent to the external Crawlora API.

Mitigation: Use a key limited to Crawlora and avoid placing sensitive private content in query parameters or request bodies.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/job-market-research)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; most search and board-list endpoints support pagination.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
