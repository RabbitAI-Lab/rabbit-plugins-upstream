## Description:

Finds YouTube micro-influencers and niche creators using apidojo's YouTube scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing, sponsorship, podcast, and affiliate teams use this skill to discover YouTube channels in a niche, filter for micro-influencer subscriber ranges, score engagement, and produce a ranked outreach list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends requested search inputs to Apify and requires an APIFY_TOKEN.

Mitigation: Install only if comfortable using Apify for YouTube scraping, protect APIFY_TOKEN, and avoid exposing secrets in shared commands or outputs.

Risk: Contact information and exported outreach lists may contain personal or business contact data.

Mitigation: Use contact information only where lawful and appropriate, follow privacy and anti-spam rules, and keep exported lists out of public repositories or shared folders.

Risk: YouTube channel metrics and contact details can be stale or incomplete.

Mitigation: Verify top channel picks and contact details manually before sponsorship or partnership outreach.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-youtube-micro-influencers)
- [Apify YouTube Scraper actor](https://apify.com/apidojo/youtube-scraper)
- [Apify actor run API endpoint](https://api.apify.com/v2/acts/apidojo~youtube-scraper/runs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Markdown, Files]

**Output Format:** [Markdown with inline bash commands and optional CSV or JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranked channel table with subscriber counts, engagement ratios, contact details when available, URLs, and outreach notes.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
