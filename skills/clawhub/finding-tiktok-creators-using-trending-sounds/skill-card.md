## Description:

Finds TikTok creators using trending sounds or viral audio tracks with apidojo's TikTok Music Scraper on Apify, returning creator and post metrics for discovery and ranking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External music labels, brand trend spotters, and influencer marketing teams use this skill to find creators using a specific TikTok sound, compare creator reach and engagement, and prioritize outreach candidates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Apify with an APIFY_TOKEN and sends TikTok sound-page URLs to that service.

Mitigation: Confirm Apify use is approved, protect the APIFY_TOKEN, and review Apify and TikTok terms before running the scraper.

Risk: The optional custom mapping input can include secrets or private data if supplied carelessly.

Mitigation: Do not place secrets, private data, or unnecessary personal data in custom mapping functions.

Risk: TikTok sounds can be removed, region-specific, duplicated across posts, or too large to process without limits.

Mitigation: Use maxItems caps, deduplicate by creator username, sort by engagement, and verify empty or regional results before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-tiktok-creators-using-trending-sounds)
- [API Dojo publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify actor run endpoint](https://api.apify.com/v2/acts/apidojo~tiktok-music-scraper/runs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, files, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON or CSV result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can guide output as a quick table, CSV file, or JSON file and includes scoring and tier labels for creators.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
