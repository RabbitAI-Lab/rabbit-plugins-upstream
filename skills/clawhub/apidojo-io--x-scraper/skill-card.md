## Description:

Guides agents through fetching X/Twitter posts by search query, profile, hashtag, keyword, conversation thread, date range, or list using Apify's X scraping actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation agents use this skill to construct Apify API calls and client-library snippets for collecting X/Twitter posts from targeted searches, profiles, hashtags, conversations, date ranges, and lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and target accounts are sent to Apify under the user's API token.

Mitigation: Avoid sensitive searches unless Apify's handling, retention, and billing terms are acceptable; prefer scoped or rotatable API tokens.

Risk: The skill depends on a paid Apify plan and may return demo, limited, or rejected results on an unsupported plan.

Mitigation: Confirm paid-plan access before relying on results and stop when responses indicate demo mode, free-plan limits, or ten or fewer returned items.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/x-scraper)
- [Apify account setup](https://apify.com/?fpr=yhdrb)
- [Apify pricing](https://apify.com/pricing?fpr=yhdrb)
- [Apify API token settings](https://console.apify.com/account/integrations)
- [Apify actor sync dataset endpoint](https://api.apify.com/v2/acts/nfp1fpt5gUlBwPcor/run-sync-get-dataset-items?timeout=120)
- [Apify actor run endpoint](https://api.apify.com/v2/acts/nfp1fpt5gUlBwPcor/runs?waitForFinish=60)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, Python, JavaScript, TypeScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Apify request payloads and examples; Apify returns tweet objects as JSON dataset items.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter states 0.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
