## Description:

Helps an agent run Guaikei-backed Douyin public-data searches for keywords, creator posts, video comments, and hot-list topics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect and analyze public Douyin search results, creator posts, comments, and real-time hot-list data for content research, competitor monitoring, sentiment review, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad or ambiguous natural-language requests may trigger high-volume Douyin collection.

Mitigation: Confirm ambiguous requests before running a command and choose the narrowest keyword, URL, time window, and limit that satisfy the user's task.

Risk: Search terms, account or video URLs, and retrieval limits are sent to Guaikei's API.

Mitigation: Use the skill only when that third-party API exchange is intended, and use a dedicated token with the minimum needed access.

Risk: Scraped results can include public account, post, and comment data and are saved locally in the skill's logs directory by default.

Mitigation: Collect only necessary public data, avoid unnecessary comment or account collection, and delete local log files when the task is complete.

## Reference(s):

- [README](readme.md)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Command JSON Schemas](assets/*.schema.json)
- [Guaikei API token and support site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON data]

**Output Format:** [Markdown guidance with Node.js shell commands; CLI runs emit structured JSON to stdout and may write JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and Node.js 16.14 or newer; retrieval commands accept limits up to 10000 records.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
