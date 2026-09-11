## Description:

Researches Fiverr gigs and sellers via the Crawlora API by searching gigs, retrieving gig details, and looking up seller profiles as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find Fiverr gigs, compare pricing and package details, and review seller profile information before making freelance marketplace decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Fiverr search terms, seller names, gig slugs, and the user's Crawlora API key to Crawlora.

Mitigation: Keep the API key in the environment as documented and avoid using the helper for private or unrelated data.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Guidance]

**Output Format:** [JSON responses with optional Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and returns public Fiverr gig and seller data from Crawlora endpoints.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
