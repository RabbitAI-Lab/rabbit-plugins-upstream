## Description:

Find podcasts suited to a proposed guest using Crawlora's podcast catalog, live show and episode data, and public show websites for guest-appearance shortlists, recent-topic research, and tailored pitch angles supported by actual episodes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to identify podcast guest opportunities, assess editorial fit from recent episodes and public show pages, and produce sourced shortlists with pitch angles and caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Podcast research queries, public URLs to scrape, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when that data transfer is acceptable, keep the API key in the environment, and avoid submitting secrets or private internal URLs.

Risk: Returned contact details, show metadata, rankings, ratings, and episode counts can be incomplete or misleading for outreach decisions.

Mitigation: Review contact information before use, verify booking channels on official show pages, preserve caveats, and avoid treating metadata as audience size or booking likelihood.

Risk: Episode descriptions and scraped pages may not prove that an episode was listened to or that a topic reflects full editorial intent.

Mitigation: Tie pitch angles to specific checked evidence, use short excerpts, and distinguish descriptions or notes from full transcripts.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with sourced shortlist details and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include show and host names, canonical links and IDs, fit rationale, recent episode evidence with dates, proposed pitch angles, verified submission channels, and caveats.]

## Skill Version(s):

1.0.10 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
