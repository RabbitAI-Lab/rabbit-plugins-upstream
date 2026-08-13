## Description:

Retrieves structured public Xiaohongshu content data for keyword search, note detail and comments, and creator post monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketing teams, analysts, and agent developers use this skill to collect public Xiaohongshu search results, note details, comments, and creator posts for content research, competitor monitoring, trend analysis, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release headline emphasizes single-note lookup, while the package also supports broad search and creator-post collection.

Mitigation: Review the selected workflow before use and invoke only the specific script needed for the user's stated task.

Risk: Keywords, Xiaohongshu URLs, limits, and GUAIKEI_API_TOKEN are sent to a third-party API service.

Mitigation: Use the skill only when third-party API use is acceptable, avoid sensitive inputs, and confirm token handling requirements before deployment.

Risk: Fetched Xiaohongshu results may persist on disk in local logs.

Mitigation: Inspect and clean the logs directory according to the user's retention and privacy requirements.

Risk: The skill is intended for public Xiaohongshu data and does not support private, hidden, or login-gated content.

Mitigation: Reject requests for non-public data and limit collection to public Xiaohongshu content.

## Reference(s):

- [Complete option reference](artifact/references/options.md)
- [Release changelog](artifact/references/changelog.md)
- [Guaikei API service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON results from the invoked CLI tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; fetched results may be stored locally in logs.]

## Skill Version(s):

1.0.0 (source: server release metadata, artifact metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
