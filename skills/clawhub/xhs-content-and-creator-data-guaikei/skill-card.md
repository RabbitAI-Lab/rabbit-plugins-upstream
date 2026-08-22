## Description:

Searches public Xiaohongshu notes, note details, comments, and creator posts through guaikei, returning structured JSON for content research, competitor analysis, KOL screening, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, content creators, data analysts, and operations teams use this skill to collect public Xiaohongshu content and creator data for topic discovery, competitor monitoring, comment analysis, KOL screening, and trend reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User keywords, Xiaohongshu note URLs, profile URLs, and request metadata are sent to guaikei.

Mitigation: Confirm the data-sharing posture before use and avoid confidential research terms or sensitive/tokenized links.

Risk: Returned public data may be saved in local JSON logs.

Mitigation: Protect or periodically delete the logs directory when outputs contain business research or personal data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-content-and-creator-data-guaikei)
- [Guaikei official site](https://www.guaikei.com)
- [Options and calling guide](references/options.md)
- [Skill changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with shell commands; executed scripts return JSON and may write JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; returned data is limited to public Xiaohongshu content.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
