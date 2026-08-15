## Description:

Searches and pulls postings from Meta's public careers site through the Crawlora API, including full catalog listing, filtered search by team, technology, location, employment type, and single-posting detail, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and recruiting analysts use this skill to search Meta public job openings, enumerate the open requisition catalog, track changes over time, or retrieve one posting by id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can make authenticated requests to arbitrary Crawlora paths and methods beyond the Meta jobs endpoints documented for this skill.

Mitigation: Review before installing, keep prompts limited to /meta-jobs/list, /meta-jobs/search, and /meta-jobs/job, and do not treat scripts/crawlora.sh as a general Crawlora API client unless that broader behavior is trusted.

Risk: The skill requires a Crawlora API key for authenticated requests.

Mitigation: Keep the key scoped and uncommitted, provide it only through CRAWLORA_API_KEY, and avoid placing it in prompts, query strings, or repository files.

## Reference(s):

- [Meta Jobs endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/meta-jobs-research)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [json, shell commands, guidance]

**Output Format:** [JSON responses with Markdown usage guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a Crawlora API key in CRAWLORA_API_KEY and documents three Meta Jobs GET endpoints.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
