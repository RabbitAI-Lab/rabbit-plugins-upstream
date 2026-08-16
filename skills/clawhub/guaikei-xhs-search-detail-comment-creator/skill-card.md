## Description:

Provides Xiaohongshu public-data lookups for content planning, including keyword search, note details, comments, and creator post collections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketers, analysts, and agents use this skill to retrieve Xiaohongshu public data for topic research, competitor monitoring, comment analysis, and creator post review. It supplies data for downstream analysis rather than logging in, publishing, interacting with Xiaohongshu, or drafting content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords or links, including link query tokens, are sent to guaikei.com using GUAIKEI_API_TOKEN.

Mitigation: Use only approved public-data queries and avoid submitting sensitive links, tokens, or research topics.

Risk: Fetched comments, URLs, and research topics may remain on disk in generated log files.

Mitigation: Review or delete the generated logs directory when the fetched data should not persist locally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-search-detail-comment-creator)
- [Guaikei API access](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI results are structured JSON and saved as JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; fetched results are written under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
