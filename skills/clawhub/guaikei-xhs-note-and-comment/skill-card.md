## Description:

Fetches public Xiaohongshu (XHS/Rednote) search results, note details, comments, and creator post lists for downstream content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, marketers, content operators, and developers use this skill to gather public Xiaohongshu note, comment, and creator-post data for content research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or URLs and the GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use it only when that data sharing is acceptable and provide a scoped token through the GUAIKEI_API_TOKEN environment variable.

Risk: Fetched comments and creator data may include personal information even when sourced from public pages.

Mitigation: Handle returned data according to privacy and retention requirements before analysis, sharing, or reporting.

Risk: Command results are saved under the local logs directory.

Mitigation: Periodically clear local logs when retained copies of fetched data are not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-note-and-comment)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON data, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; executed commands return structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; fetched results are logged locally.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact package/changelog report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
