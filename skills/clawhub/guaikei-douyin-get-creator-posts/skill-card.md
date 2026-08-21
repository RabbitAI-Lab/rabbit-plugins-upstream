## Description:

Runs Node.js command-line tools that retrieve public Douyin search results, creator posts, comments, and hot-list data as JSON through the Guaikei API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and marketing teams use this skill to gather public Douyin content, creator-post, comment, and hot-list data for content research, competitor analysis, market monitoring, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin search terms, profile or video URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when that data sharing is acceptable; keep the token private and rotate it if exposed.

Risk: Command results can include comments, usernames, profile identifiers, and other public Douyin data saved to local logs.

Mitigation: Review the logs directory after use and delete files containing data that should not be retained or shared.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-get-creator-posts)
- [Complete option reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [JSON schemas](artifact/assets/)
- [Guaikei API token and help site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; command stdout is structured JSON with status, request metadata, and result arrays.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands write logs under the skill's logs directory and use exit code 3 for missing or invalid GUAIKEI_API_TOKEN.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
