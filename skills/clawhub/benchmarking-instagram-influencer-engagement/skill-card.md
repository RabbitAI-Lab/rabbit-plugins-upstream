## Description:

Benchmarks and compares Instagram influencer engagement rates using apidojo's Instagram scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, influencer agencies, and campaign analysts use this skill to compare Instagram accounts, benchmark engagement by follower tier, and flag suspicious or low-quality engagement before paid partnerships.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instagram handles, request metadata, and scraper activity are sent to Apify/Apidojo.

Mitigation: Use only appropriate public account targets and review Apify/Apidojo billing and data-handling terms before running the scraper.

Risk: APIFY_TOKEN exposure could allow unauthorized actor runs or account charges.

Mitigation: Store APIFY_TOKEN as a secret environment variable and avoid pasting it into prompts, command history, logs, or files.

Risk: Engagement conclusions can be unreliable for private accounts, low post counts, or incomplete scraper results.

Mitigation: Skip inaccessible private profiles, flag accounts with fewer than 10 recent posts, and present anomaly findings as review signals rather than definitive fraud determinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/benchmarking-instagram-influencer-engagement)
- [Apify actor: apidojo/instagram-scraper](https://apify.com/apidojo/instagram-scraper)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, API Calls]

**Output Format:** [Markdown report with comparison tables, account-level findings, and optional JSON or CSV scrape outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires APIFY_TOKEN; analyzes up to 10 Instagram accounts and defaults to 30 recent posts when not specified.]

## Skill Version(s):

1.0.0 (source: evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
