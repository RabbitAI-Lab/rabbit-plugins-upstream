## Description:

Provides Node.js commands for collecting Xiaohongshu public data, including note comments, note details, creator posts, and keyword search results for downstream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, marketers, content teams, and data analysts use this skill to retrieve public Xiaohongshu comments and related public note, search, and creator-post data for trend research, competitive monitoring, KOL review, and report generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is named and summarized as a comment-only helper but includes broader Xiaohongshu search, note-detail, and creator-post collection commands.

Mitigation: Use comment-cli.js for comment-only workflows and invoke search, detail, or post commands only when broader public-data collection is explicitly intended and permitted.

Risk: URLs, keywords, limits, and GUAIKEI_API_TOKEN are sent to guaikei.com for API-backed data retrieval.

Mitigation: Confirm third-party data-sharing approval before use, avoid submitting sensitive URLs or keywords, and protect the API token as a credential.

Risk: Returned public-data results are automatically saved under logs/ by the command-line tools.

Mitigation: Review log contents after use and apply retention, access control, or deletion practices appropriate for the collected data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-comment-data)
- [Guaikei Service Website](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful command results may be written automatically under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
