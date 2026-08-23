## Description:

Retrieves public Xiaohongshu data for keyword search, note details, comments, and creator post history so agents can prepare growth, competitor, and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketing teams, operators, and analysts use this skill to collect public Xiaohongshu search results, note details, comments, and creator post lists for topic discovery, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keywords, Xiaohongshu links, requested limits, and GUAIKEI_API_TOKEN are sent to the third-party guaikei.com API.

Mitigation: Use the skill only for public data, confirm the API data-sharing boundary before execution, and keep the token in environment configuration rather than prompts or shared files.

Risk: Fetched results are saved locally under logs, which may retain public content and analysis inputs on shared or synced machines.

Mitigation: Delete local logs when they are no longer needed and avoid running the skill in directories that are broadly shared or automatically synchronized.

Risk: The skill is not intended for private, hidden, or login-only Xiaohongshu content.

Mitigation: Validate that user requests are limited to public Xiaohongshu data and decline or redirect requests for private or restricted content.

## Reference(s):

- [Skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-public-data-for-growth)
- [Guaikei API and token portal](https://www.guaikei.com)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Structured JSON command output with terminal status text and locally saved JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; results are fetched through guaikei.com and saved under logs.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
