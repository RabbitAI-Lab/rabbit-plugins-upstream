## Description:

Researches job postings, hiring signals, and freelance gigs through the Crawlora API across job boards, company career sites, ATS boards, Upwork, and Fiverr, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, researchers, and agents use this skill to search jobs, inspect company hiring activity, identify ATS boards, compare hiring signals, and research freelance gigs or sellers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script is a general Crawlora API proxy and can call endpoints outside the job-market research scope.

Mitigation: Review each requested path before execution or restrict use to the job-market endpoints documented in artifact/reference/endpoints.md.

Risk: Job, company, and freelance search terms are sent to Crawlora.

Mitigation: Avoid sensitive or confidential queries unless the user accepts sending them to Crawlora.

Risk: The skill depends on a Crawlora API key and external API availability.

Mitigation: Keep CRAWLORA_API_KEY in the environment only, do not hardcode it, and handle authentication or service failures explicitly.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/job-market-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; most search and board-list responses may require pagination.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
