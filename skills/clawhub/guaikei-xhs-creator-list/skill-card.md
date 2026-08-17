## Description:

Provides structured public Xiaohongshu data for post search, note details, comment analysis, and creator monitoring to support content planning, competitor monitoring, KOL screening, and trend research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketing teams, analysts, and MCN operators use this skill to retrieve public Xiaohongshu data for topic research, competitor monitoring, KOL evaluation, comment analysis, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note URLs, profile URLs, and the GUAIKEI_API_TOKEN are sent to guaikei.com when commands run.

Mitigation: Use the skill only when that external data transfer is acceptable, and protect or rotate the API token according to the publisher's guidance.

Risk: Returned research results are saved locally and may include sensitive campaign, competitor, or personal comment information.

Mitigation: Store logs in an approved location, restrict access, and delete retained outputs when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-creator-list)
- [Guaikei API website](https://www.guaikei.com)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files]

**Output Format:** [Markdown guidance with bash command examples; CLI commands return JSON and save local log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; supports public Xiaohongshu data only.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
