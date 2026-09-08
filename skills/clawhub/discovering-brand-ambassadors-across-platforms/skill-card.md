## Description:

Discovers potential brand ambassadors across Instagram, TikTok, and Twitter using apidojo scrapers, returning platform handles, reach estimates, brand affinity signals, engagement metrics, and tier classification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Brand partnership teams, DTC brands, and ambassador program managers use this skill to discover and triage creators for multi-channel ambassador outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires an APIFY_TOKEN and uses Apify-hosted scraping actors.

Mitigation: Use a scoped token where possible, keep it out of shared outputs, and run the skill only in environments approved for Apify usage.

Risk: The release presents cross-platform discovery, but the documented execution path is primarily Instagram-focused.

Mitigation: Treat TikTok and Twitter coverage as unverified unless the publisher adds concrete collection steps or the operator validates those platforms separately.

Risk: The cross-platform reach score is internally inconsistent and may misrank creators.

Mitigation: Review per-platform metrics separately before using the ranking for outreach or partnership decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apidojo-io/skills/discovering-brand-ambassadors-across-platforms)
- [Apify Actor Run API](https://api.apify.com/v2/acts/apidojo~instagram-scraper/runs?token=$APIFY_TOKEN)
- [Apify Actor Dataset Items API](https://api.apify.com/v2/actor-runs/$RUN_ID/dataset/items?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, configuration, guidance]

**Output Format:** [Markdown with tables and inline shell/API command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save scraped results as CSV or JSON when the helper script is available.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact metadata version is 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
