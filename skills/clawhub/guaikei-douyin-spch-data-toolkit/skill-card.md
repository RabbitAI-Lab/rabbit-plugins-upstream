## Description:

Queries public Douyin data for hot lists, keyword search, creator posts, and video comments, then returns structured JSON without publishing, editing, downloading, or accessing other platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, analysts, and developers use this skill to retrieve public Douyin search results, trending topics, creator posts, and comments for content research, competitor monitoring, sentiment review, and follow-on reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, URLs, requested public data, and the API token are sent to guaikei.com.

Mitigation: Install and run only when third-party API sharing is acceptable, and avoid confidential monitoring targets unless that sharing is approved.

Risk: Search, post, and comment results may be saved under the skill's logs directory.

Mitigation: Review local log retention before use and delete or protect logs that contain sensitive research targets or business context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-spch-data-toolkit)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei API token and support site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Node.js CLI commands; executed commands return structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command output is JSON on stdout with logs and status messages on stderr.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
