## Description:

Searches Xiaohongshu public notes by keyword and retrieves note details, comments, and creator post lists for content research, competitor monitoring, and market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, content creators, content operations teams, and data analysts use this skill to collect structured public Xiaohongshu data for topic research, post/comment analysis, competitor monitoring, creator review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu note/profile URLs, and returned public-content data are sent to guaikei.com using GUAIKEI_API_TOKEN.

Mitigation: Use only approved public-data queries and confirm that the third-party API service and data handling are acceptable for the intended workspace before use.

Risk: Generated logs can contain keywords, returned public-content data, and URLs with xsec_token values.

Mitigation: Store logs only in approved locations, restrict access on shared machines, and clean or redact the logs directory when results no longer need to be retained.

Risk: The skill depends on a third-party API token, so invalid, missing, or overexposed tokens can interrupt operation or leak service access.

Mitigation: Keep GUAIKEI_API_TOKEN in environment configuration, avoid pasting it into prompts or logs, and rotate it if exposure is suspected.

## Reference(s):

- [Options and Usage Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei API Service](https://www.guaikei.com)
- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/xhs-keyword-search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, json, files]

**Output Format:** [Markdown guidance with shell commands; CLI execution returns structured JSON and saves JSON result logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; result logs may include Xiaohongshu URLs, xsec_token query values, keywords, and returned public-content data.]

## Skill Version(s):

1.0.0 (source: package.json, artifact metadata, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
