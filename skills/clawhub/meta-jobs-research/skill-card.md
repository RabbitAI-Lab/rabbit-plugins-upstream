## Description:

Searches and pulls postings from Meta's public careers site (metacareers.com) via the Crawlora API - full catalog listing, filtered search by team/technology/location/employment-type, and single-posting detail - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and recruiting analysts use this skill to search Meta's public job openings, enumerate the open requisition catalog, track newly modified roles, or retrieve a single posting by job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meta jobs search queries and requests are sent to Crawlora, and a custom CRAWLORA_API_BASE can redirect the helper script to another destination.

Mitigation: Install only if that data flow is acceptable; keep CRAWLORA_API_BASE unset unless intentionally using a trusted alternative endpoint.

Risk: CRAWLORA_API_KEY is required to call the API and could be exposed if hardcoded or committed.

Mitigation: Store the key in an environment variable or secret store and never place it in source files, query parameters, or committed examples.

## Reference(s):

- [Meta Jobs endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/meta-jobs-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; returns public Meta Careers job data through Crawlora endpoints.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
