## Description:

Researches public US legal opinions, courts, and judicial people through CourtListener via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External legal researchers, developers, and agents use this skill to search public US legal opinions, browse courts, and look up public judicial-person records as research leads before verifying legal conclusions against primary sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key with arbitrary methods, paths, request bodies, and an overridden API base.

Mitigation: Review before installing, avoid untrusted CRAWLORA_API_BASE values, and prefer a version that hardcodes the documented CourtListener GET endpoints and validates parameters.

## Reference(s):

- [CourtListener endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API service](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/courtlistener-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key and returns public CourtListener search, court, and judicial-person data for verification against primary sources.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
