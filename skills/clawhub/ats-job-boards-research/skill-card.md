## Description:

Fetches public job openings and posting details from company ATS-hosted career pages through the Crawlora API, returning normalized JSON for supported platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and market researchers use this skill to retrieve live public ATS job boards, inspect individual postings, and build hiring-velocity snapshots when they know or can resolve a company's ATS platform and board slug.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the configured Crawlora API key to a non-default API base if CRAWLORA_API_BASE is changed.

Mitigation: Use the default Crawlora API base and review any environment override before running the helper.

Risk: A Crawlora API key with paid quota could be exposed through logs, shell history, or committed files.

Mitigation: Keep CRAWLORA_API_KEY in the environment only, avoid logging it, and do not commit it.

Risk: Sensitive personal or proprietary data could be passed through the helper.

Mitigation: Use the skill for public job postings and board identifiers, and avoid submitting sensitive data.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/ats-job-boards-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; works with public ATS postings and board identifiers.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
