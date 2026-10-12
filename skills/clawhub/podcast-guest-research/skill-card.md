## Description:

Find podcasts suited to a proposed guest using Crawlora's podcast catalog, live show and episode data, and public show websites to build sourced shortlists and tailored pitch angles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Podcast publicists, guest bookers, and creators use this skill to identify relevant shows, check recent episodes, and develop evidence-backed guest pitch angles without assuming booking availability or audience size.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries, public URLs submitted for scraping, and the API key are sent to Crawlora.

Mitigation: Use only if comfortable sharing those inputs with Crawlora, and keep the key in the environment as instructed.

Risk: Scraping private or authenticated pages could expose sensitive information.

Mitigation: Scrape public pages only; avoid private or authenticated URLs.

Risk: Incomplete catalogs or episode metadata may overstate a show's fit, audience, or availability.

Mitigation: Verify show identity and recent episodes, cite checked sources, and preserve unknowns about audience and bookings.

## Reference(s):

- [Podcast guest research endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub release](https://clawhub.ai/crawlora-org/skills/podcast-guest-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sourced show shortlist with recent episode evidence, proposed pitch angles, verified public contact channels when available, and caveats.]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
