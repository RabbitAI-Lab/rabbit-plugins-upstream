## Description:

Retrieves structured public Xiaohongshu data for keyword search, note details, note comments, and creator post lists so agents can prepare downstream summaries, comparisons, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, content operators, data analysts, and agent developers use this skill to collect public Xiaohongshu note, comment, and creator-post data for content research, competitor monitoring, KOL evaluation, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, and collected public content are sent through the Guaikei API.

Mitigation: Use only for data you are authorized to process and avoid sensitive tracking targets or content you do not want handled by the third-party API.

Risk: GUAIKEI_API_TOKEN is a paid or private credential and the scanner notes token handling in URL query strings.

Mitigation: Store the token in the environment, restrict access to runtime logs and shell history, rotate it if exposure is suspected, and avoid sharing command transcripts that may include request details.

Risk: Fetched social-media results are automatically retained in local log files.

Mitigation: Review and delete local logs after use when they contain sensitive campaign, creator, or competitive research data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-kol-evaluation-data)
- [Guaikei API access](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with executable Node.js commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results may also be saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
