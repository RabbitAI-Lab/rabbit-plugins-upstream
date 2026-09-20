## Description:

Researches Fiverr gigs and sellers via the Crawlora API, returning normalized JSON for gig search, gig detail, pricing and package comparison, and seller profile lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search Fiverr gigs, compare package pricing and delivery details, and review public seller profile information before recommending or selecting freelance services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Fiverr lookup terms, seller names, gig slugs, and the Crawlora API key to Crawlora.

Mitigation: Keep the API key in CRAWLORA_API_KEY, avoid sensitive queries, and install only when that data sharing is acceptable.

## Reference(s):

- [fiverr-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/fiverr-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends Fiverr search terms, seller usernames, and gig slugs to Crawlora.]

## Skill Version(s):

1.0.16 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
