## Description:

Searches Google's public careers site (careers.google.com) via the Crawlora API and pulls single job postings by id, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and recruiting researchers use this skill to search public Google Careers postings by role or location, retrieve a specific posting by numeric id, and track posting changes over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to an overridden API host.

Mitigation: Do not set CRAWLORA_API_BASE unless the destination is fully trusted; use a Crawlora key that can be rotated and scoped.

Risk: The helper is broader than the Google Jobs lookup use case.

Mitigation: Prefer limiting use to the documented GET endpoints /google-jobs/search and /google-jobs/job.

## Reference(s):

- [Google Jobs endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/google-jobs-research)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Google Careers posting data from Crawlora endpoints.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
