## Description:

Researches Fiverr gigs and sellers via the Crawlora API by searching gigs, retrieving gig details with packages and pricing tiers, and looking up seller profiles as normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and external users use this skill to research Fiverr gigs, compare service pricing and packages, and review public seller profile details before making marketplace decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fiverr queries and the Crawlora API key are sent to a third-party Crawlora API.

Mitigation: Use a dedicated Crawlora API key, avoid sensitive search terms, and confirm the third-party API fits the user's compliance requirements before use.

Risk: Marketplace research can reflect incomplete, stale, or commercially biased public listing data.

Mitigation: Treat returned Fiverr data as research input and verify important pricing, package, and seller details before making purchasing decisions.

## Reference(s):

- [fiverr-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/fiverr-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell command examples and JSON API output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API calls and returns normalized public Fiverr gig and seller data.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
