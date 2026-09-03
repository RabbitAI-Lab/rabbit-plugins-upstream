## Description:

Discovers TikTok Shop sellers and product listings in a specific niche using apidojo's TikTok scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, product researchers, affiliate marketers, and TikTok Shop entrants use this skill to map sellers, promoted products, competitors, and market saturation signals within a TikTok Shop niche.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-chosen TikTok research inputs are sent to Apify and may reveal sensitive research interests if keywords or custom mapping code include private information.

Mitigation: Use your own Apify token, keep private information out of keywords and customMapFunction, and review helper scripts before running them.

Risk: Large or unbounded scraper runs can increase cost and produce more data than intended.

Mitigation: Set maxItems before running the actor and choose focused niche keywords or start URLs.

Risk: TikTok Shop market signals can be noisy, incomplete, or skewed by viral posts.

Mitigation: Filter non-shop posts, de-duplicate products, and prefer median activity across recent posts instead of relying on a single high-view post.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/discovering-tiktok-shop-sellers-by-niche)
- [API Dojo publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify TikTok scraper REST endpoint](https://api.apify.com/v2/acts/apidojo~tiktok-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with tables, optional CSV or JSON result files, and inline shell or API commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes seller handles, product names, prices when available, estimated sales signals, seller classifications, competition level, and potential niche gaps.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact/SKILL.md metadata lists 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
