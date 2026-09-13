## Description:

Searches Indeed job postings and retrieves location suggestions and individual job details through the Crawlora API, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search public Indeed postings by role and location, resolve valid Indeed location strings, paginate recent searches, and retrieve detailed postings by job key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags that the bundled helper can send undocumented request bodies beyond the stated GET-only job endpoints.

Mitigation: Use only the documented Indeed endpoints and parameters, prefer GET requests for normal use, and review proposed commands before execution.

Risk: The skill uses a Crawlora API key and may be used with private job-search context or credentials.

Mitigation: Keep CRAWLORA_API_KEY in the environment only, do not commit or expose it, and avoid sharing sensitive job-search context unless necessary.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/indeed-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented Indeed job search, location suggestion, and job detail endpoints.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
