## Description:

Find podcasts suited to a proposed guest using Crawlora's podcast catalog, live show and episode data, and public show websites for guest-appearance shortlists, recent-topic research, and tailored pitch angles supported by actual episodes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, podcast researchers, founders, marketers, and agents use this skill to identify podcasts that fit a proposed guest, gather recent episode evidence, and draft grounded pitch angles. It is intended for sourced shortlists and research notes, not automated outreach decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends podcast research queries, show URLs, and scrape requests to Crawlora.

Mitigation: Use an approved Crawlora key in the environment, avoid submitting confidential research subjects unless authorized, and review requests before running them.

Risk: Podcast metadata, rankings, episode counts, and search results can be incomplete or poor proxies for audience size, activity, or booking likelihood.

Mitigation: Verify show identity, recent publication dates, host or creator details, and booking channels before relying on a shortlist or pitch angle.

Risk: Public contact research can lead to inappropriate outreach if treated as a sending instruction.

Mitigation: Keep researched contacts separate from draft pitch copy and send outreach only after human review and explicit approval.

## Reference(s):

- [Podcast Guest Research endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/podcast-guest-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown research shortlist with sourced notes and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include show and host names, canonical links and IDs, fit rationale, recent episode dates, pitch angles, verified submission channels, and caveats.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
