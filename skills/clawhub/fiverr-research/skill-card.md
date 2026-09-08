## Description:

Researches Fiverr gigs and sellers via the Crawlora API to search gigs by keyword, retrieve gig details, and look up seller profiles as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Fiverr gigs, compare pricing and package details, and assess seller profiles using public Fiverr data returned through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can send the user's API key with arbitrary Crawlora requests if used outside the documented Fiverr endpoints.

Mitigation: Keep CRAWLORA_API_BASE on the official Crawlora API origin and constrain usage to the documented Fiverr GET endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/fiverr-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Fiverr search results are paginated.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
