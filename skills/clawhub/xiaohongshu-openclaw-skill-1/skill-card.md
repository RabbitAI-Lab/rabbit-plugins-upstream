## Description:

Provides structured retrieval of public Xiaohongshu data for keyword research, note details, comments, creator post monitoring, and downstream content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, data analysts, and agent developers use this skill to gather public Xiaohongshu data for content planning, competitor monitoring, KOL screening, and comment insight workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords or URLs are sent to the Guaikei third-party API.

Mitigation: Avoid submitting sensitive campaign plans, private links, secrets, or data that should not be shared with the API provider.

Risk: Successful public-platform results are saved locally under logs/.

Mitigation: Review local result files for sensitive or retained data and delete them when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xiaohongshu-openclaw-skill-1)
- [Guaikei API service](https://www.guaikei.com)
- [Changelog](references/changelog.md)
- [Options reference](references/options.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files, Guidance]

**Output Format:** [Structured JSON responses from Node.js command-line tools, with local JSON result files for successful runs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful results are saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
