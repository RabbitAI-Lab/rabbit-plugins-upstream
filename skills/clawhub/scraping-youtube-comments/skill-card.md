## Description:

Scrapes comments from YouTube videos using apidojo's YouTube scraper on Apify and returns commenter names, comment text, likes, reply counts, and timestamps for analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, product teams, and content researchers use this skill to collect YouTube comment datasets for sentiment research, audience feedback review, and offline analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented input scope may allow broader YouTube scraping than a single video's comments.

Mitigation: Limit runs to the intended video URLs, set conservative collection limits, and review Apify actor input before execution.

Risk: Examples place APIFY_TOKEN in URL query strings, which can expose credentials through logs or shell history.

Mitigation: Use a limited Apify token, pass credentials through environment or approved secret handling, and avoid sharing command history or logs containing tokens.

Risk: YouTube comment collection sends target URLs and collected data through Apify infrastructure.

Mitigation: Avoid sensitive research targets unless the user accepts Apify processing, and review applicable platform and data-use obligations before collection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-youtube-comments)
- [Apify actor: apidojo/youtube-scraper](https://apify.com/apidojo/youtube-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summary and table, with optional CSV or JSON dataset export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns comment IDs, author display names, text, like counts, reply counts, timestamps, reply status, and parent IDs when available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
