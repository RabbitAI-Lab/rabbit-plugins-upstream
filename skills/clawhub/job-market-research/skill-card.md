## Description:

Researches job postings, hiring signals, and freelance gigs via the Crawlora API across major job boards, company career sites, ATS boards, Upwork, and Fiverr, returning normalized JSON for job-market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, recruiters, and agents use this skill to search public job postings, inspect company ATS boards, summarize hiring velocity, and research freelance-market signals through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and caller-supplied query data can be sent through the Crawlora helper, including to an overridden API destination.

Mitigation: Use the skill only in trusted environments, keep CRAWLORA_API_KEY tightly scoped, avoid setting CRAWLORA_API_BASE unless the destination is validated, and review generated commands before execution.

Risk: Private documents, secrets, or broad conversation context could be exposed if they are passed into Crawlora API requests.

Mitigation: Send only the minimum public search terms needed for the task and exclude secrets, private documents, and unrelated conversation context.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/job-market-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and may return paginated public job, hiring-signal, and freelance-market data.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
