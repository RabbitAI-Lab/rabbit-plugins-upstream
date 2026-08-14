## Description:

This skill helps agents retrieve public Xiaohongshu note search results, note details, comments, and creator posts through Guaikei API-backed Node.js commands, returning structured JSON for content research and marketing analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketing teams, analysts, and agent developers use this skill to gather public Xiaohongshu data for topic research, competitor monitoring, KOL screening, comment analysis, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, URLs, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use it only when third-party API processing is acceptable, and avoid submitting private, confidential, or unauthorized URLs.

Risk: Generated logs can retain research data, including URLs with xsec_token values, comments, and profile metadata.

Mitigation: Treat log files as retained research records; restrict access, avoid sharing them broadly, and delete them when no longer needed.

Risk: The skill is limited to public Xiaohongshu data and may return empty or failed results for deleted, private, hidden, or unavailable content.

Mitigation: Check each command's status field, report empty or failed results honestly, and do not infer missing data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-data-assistant)
- [Guaikei API site](https://www.guaikei.com)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown, Files]

**Output Format:** [Markdown guidance with Node.js shell commands and structured JSON command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; fetched results are printed to stdout and saved under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
