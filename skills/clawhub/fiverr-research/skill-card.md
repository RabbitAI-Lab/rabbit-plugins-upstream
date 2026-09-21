## Description:

Researches Fiverr gigs and sellers through the Crawlora API, including keyword gig search, gig package and pricing details, and seller profile lookup, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and sourcing teams use this skill to find Fiverr gigs, compare public pricing and packages, and review seller profile signals before shortlisting freelance services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fiverr search terms, seller usernames, gig slugs, and the Crawlora API key are sent to Crawlora's API.

Mitigation: Use a dedicated Crawlora key stored only in the environment, and avoid sensitive or private research queries.

Risk: The skill uses public Fiverr gig and seller data that may be incomplete, stale, or subject to Fiverr's terms.

Mitigation: Treat results as research inputs, respect Fiverr's terms, and verify seller or gig details directly before making decisions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/fiverr-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and queries public Fiverr gig and seller endpoints through Crawlora.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
