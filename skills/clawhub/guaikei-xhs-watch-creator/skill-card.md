## Description:

Retrieves public Xiaohongshu search results, note details, creator posts, and comment data through command-line workflows for content, trend, competitor, KOL, and audience-feedback analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External content creators, marketers, data analysts, MCN teams, and agencies use this skill to retrieve public Xiaohongshu notes, creator activity, and comments for trend tracking, competitor monitoring, KOL screening, and audience-feedback analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a guaikei.com API token and sends Xiaohongshu keywords or URLs to that third-party service.

Mitigation: Install only when that data transfer is acceptable, use authorized public targets, and avoid private, confidential, or sensitive inputs.

Risk: Returned public comments, profile, and note data may be saved in local log files.

Mitigation: Apply an appropriate retention policy and periodically delete logs when retained social-media data is no longer needed.

Risk: The skill depends on third-party API availability and may return empty or error status objects.

Mitigation: Treat status fields as authoritative, retry or broaden inputs when appropriate, and do not infer or fabricate missing Xiaohongshu data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-watch-creator)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [guaikei.com API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [JSON status objects on stdout, optional local JSON log files, and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and a public Xiaohongshu keyword, note URL, or creator profile URL; command limits support up to 10000 requested items.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
