## Description:

Researches Upwork job postings and freelancer profiles through the Crawlora API and returns normalized JSON for job searches, job details, and freelancer profile lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and hiring teams use this skill to search public Upwork job listings, inspect individual job postings, estimate freelance market rates, and review public freelancer profile signals before outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged helper can call arbitrary Crawlora API paths and methods beyond the documented Upwork endpoints, which may send data to unrelated Crawlora endpoints or consume API credits.

Mitigation: Review commands before execution and restrict use to the documented /upwork/search, /upwork/job/{id}, and /upwork/freelancer/{id} endpoints unless broader Crawlora access is explicitly intended.

Risk: Crawlora API credentials are required for use.

Mitigation: Provide the key only through CRAWLORA_API_KEY, avoid placing it in commands or files, and rotate it if it is exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/upwork-research)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; the helper prints raw JSON from Crawlora API calls.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
