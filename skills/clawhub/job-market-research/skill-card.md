## Description:

Researches job postings, hiring signals, and freelance gigs via the Crawlora API, covering major employer career sites, ATS boards, Upwork, and Fiverr, and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to search job postings, inspect company hiring activity, identify ATS boards, gather hiring signals, and research freelance gigs through Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job, company, freelancer, and marketplace search terms are sent to Crawlora with the user's API key.

Mitigation: Use the skill only when that third-party API use is acceptable, and avoid sending secrets, confidential plans, private candidate data, or sensitive company research terms.

Risk: The skill makes expected external requests to Crawlora.

Mitigation: Review requests before execution and keep CRAWLORA_API_KEY in the environment rather than hardcoding or committing it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora API key and account setup](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/job-market-research)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and raw JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and sends requests to the Crawlora API.]

## Skill Version(s):

1.0.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
