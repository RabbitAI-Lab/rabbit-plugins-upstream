## Description:

Collects public Xiaohongshu note, comment, engagement, and creator-post data through guaikei.com APIs for KOL screening, trend research, competitor monitoring, and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, content operators, and analysts use this skill to search Xiaohongshu public content, inspect note details and comments, monitor creator posts, and prepare structured data for reports or follow-on analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note URLs, profile URLs, and the API token are sent to a third-party API.

Mitigation: Use the skill only when that data transfer is approved for the user's workflow and configure GUAIKEI_API_TOKEN through the environment rather than pasting it into prompts or shared files.

Risk: Returned comments and profile-linked public content can still be privacy-relevant.

Mitigation: Limit use to authorized public-data analysis, avoid private or hidden content requests, and follow applicable platform, legal, and organizational data-handling rules.

Risk: Task results are saved in a local logs directory, which may retain research targets and collected data.

Mitigation: Delete or sanitize local logs when results should not be retained or shared.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-xiaohongshu-data-collector)
- [Guaikei Website](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON emitted by Node.js CLI commands, with task results also saved as local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and a GUAIKEI_API_TOKEN environment variable for API access.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
