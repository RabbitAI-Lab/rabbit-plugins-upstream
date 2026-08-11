## Description:

Retrieves structured public Xiaohongshu/RedNote data for keyword search, note details, creator post lists, and note comments through Guaikei command-line tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, researchers, and analysts use this skill to collect public Xiaohongshu content, creator posts, engagement metadata, and comments for content planning, competitive monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords or links, including xsec_token URL parameters, are sent to guaikei.com with the configured GUAIKEI_API_TOKEN.

Mitigation: Use the skill only when third-party API disclosure is acceptable, avoid unnecessary sensitive query terms, and scope requests to the minimum data needed.

Risk: Fetched public comments, profile data, and engagement results may be saved locally under the logs directory.

Mitigation: Periodically delete local logs when retained datasets are no longer needed.

Risk: Returned Xiaohongshu comments and profile data are public but user-generated and may be incomplete, stale, or unsuitable for automated decisions.

Mitigation: Review outputs before using them in reports, marketing decisions, or downstream analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-public-data-guaikei)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Node.js command examples and structured JSON command results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; command results may be written to the local logs directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
