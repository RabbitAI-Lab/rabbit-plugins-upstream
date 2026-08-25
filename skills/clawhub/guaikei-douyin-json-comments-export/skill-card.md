## Description:

Uses token-backed command-line tools to retrieve Douyin public search results, creator posts, video comments, and real-time hot-list data as JSON for content planning, competitor analysis, and traffic research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to collect public Douyin data for marketing selection, content planning, competitor monitoring, comment analysis, and hot-topic tracking. It is not intended for private account analytics, publishing, editing, watermark removal, or follower-growth operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin URLs, search keywords, request limits, and GUAIKEI_API_TOKEN to the third-party guaikei.com API.

Mitigation: Install only when that data sharing is acceptable, keep the token in an environment variable, and rotate or revoke the token if exposure is suspected.

Risk: Fetched comments, account data, and research terms are saved locally in the skill's logs directory by default.

Mitigation: Restrict access to generated logs, delete them when no longer needed, and avoid collecting sensitive research terms unless approved.

Risk: Broad auto-trigger wording may run the skill for loosely related Douyin prompts.

Mitigation: Use explicit Douyin-related prompts and confirm the intended search, post, comment, or hot-list action before running commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-json-comments-export)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Usage documentation](readme.md)
- [Complete CLI options](references/options.md)
- [Changelog](references/changelog.md)
- [JSON Schemas](assets/*.schema.json)
- [Guaikei token documentation](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files, Configuration, Guidance]

**Output Format:** [Pure JSON on stdout, logs on stderr, and JSON log files saved under logs/ by default]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16.14 and GUAIKEI_API_TOKEN; each retrieval is limited to 10000 records.]

## Skill Version(s):

1.0.0 (source: package.json, references/changelog.md, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
