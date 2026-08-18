## Description:

xhs-strategy-scan helps agents retrieve public Xiaohongshu notes, note details, comments, and creator post lists for trend research, competitor analysis, KOL screening, and content planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, brand marketers, market analysts, and agent developers use this skill to collect public Xiaohongshu data for topic discovery, competitor monitoring, comment analysis, trend tracking, and report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided Xiaohongshu keywords, note or profile URLs, and GUAIKEI_API_TOKEN are sent to www.guaikei.com.

Mitigation: Install only if this data transfer is acceptable; keep the token in an environment variable, avoid sensitive queries, and rotate the token if it may have been exposed.

Risk: Returned Xiaohongshu data and saved logs can expose sensitive marketing research, URLs, comments, or profile data.

Mitigation: Review and clean the logs directory when results are sensitive, and use collected public data only in line with Xiaohongshu and applicable policy requirements.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/engheng-art/skills/xhs-strategy-scan)
- [GUAIKEI API and token portal](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; command results may be saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
