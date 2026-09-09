## Description:

Discovers pre-launch startups and products on Twitter using apidojo's Twitter Search scraper and returns startup handles, product descriptions, waitlist or launch signals, stage classifications, and niches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, venture investors, accelerator scouts, and competitive intelligence teams use this skill to discover early-stage startups, beta products, stealth companies, and waitlist signals on Twitter/X. It helps configure and run the Apify tweet scraper, then classify and score results for startup research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitter/X search terms and related Apify usage metadata may be sent to Apify during scraping workflows.

Mitigation: Use the skill only for intended startup-research requests, keep APIFY_TOKEN scoped and private, and confirm that sending the selected queries to Apify is acceptable.

Risk: Saved CSV or JSON outputs may contain retained research data from Twitter/X results.

Mitigation: Store exported files only in locations approved for this research data and remove unnecessary retained outputs.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/apidojo-io/skills/discovering-pre-launch-startups-on-twitter)
- [API Dojo publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify actor REST run endpoint](https://api.apify.com/v2/acts/apidojo~tweet-scraper/runs?token=$APIFY_TOKEN)
- [Apify run dataset items endpoint](https://api.apify.com/v2/actor-runs/$RUN_ID/dataset/items?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with tables and inline shell/API commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save research results as CSV or JSON when the run_actor.js workflow is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
