## Description:

Searches public Xiaohongshu posts, note details, comments, and blogger posts so agents can gather structured data for content research, competitor analysis, KOL screening, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, content creators, and analysts use this skill to query public Xiaohongshu content through command-line scripts and return structured results for summaries, comparisons, reports, and follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, profile links, note links, and GUAIKEI_API_TOKEN are sent to the third-party guaikei.com API.

Mitigation: Use only approved tokens and inputs that are acceptable for third-party processing; confirm organizational data-sharing policy before use.

Risk: Generated logs can retain sensitive research topics, competitor targets, comments, or other returned public-data results locally.

Mitigation: Review the logs/ directory after use and delete files that should not be retained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-blogger-posts)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [json, text, shell commands, configuration, guidance]

**Output Format:** [Structured JSON on stdout with status logs on stderr; successful results may also be saved as JSON files under logs/.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; calls the third-party guaikei.com API; command limits range up to 10000 results depending on route.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
