## Description:

Searches and pulls postings from Meta's public careers site (metacareers.com) via the Crawlora API - full catalog listing, filtered search by team/technology/location/employment-type, and single-posting detail - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and analysts use this skill to search Meta public job openings, enumerate the current catalog, track new or modified requisitions, and retrieve details for a specific posting id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send a user's Crawlora API key and credits to arbitrary Crawlora paths, methods, request bodies, or an environment-selected API base.

Mitigation: Review before installing, keep CRAWLORA_API_BASE controlled, avoid untrusted command arguments, and prefer restricting use to the three documented GET Meta Jobs endpoints.

Risk: The skill requires a Crawlora API key, so misuse may expose credentials or consume account credits.

Mitigation: Store the key only in CRAWLORA_API_KEY, do not commit or pass it in query parameters, and run the helper only in trusted environments.

## Reference(s):

- [Meta Jobs endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/meta-jobs-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on Crawlora API availability, valid CRAWLORA_API_KEY credentials, endpoint parameters, and Meta public careers data.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
