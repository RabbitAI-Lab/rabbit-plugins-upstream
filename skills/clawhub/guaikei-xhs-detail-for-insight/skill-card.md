## Description:

This skill helps agents retrieve public Xiaohongshu/Rednote search results, note details, comments, and creator posts through guaikei.com for downstream content, competitor, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, content creators, analysts, and agent workflows use this skill to collect public Xiaohongshu data for topic research, competitor monitoring, note review, comment analysis, and creator post monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, links, and related request data are sent to guaikei.com.

Mitigation: Use only public, non-sensitive inputs and confirm the user is authorized to process the requested public data.

Risk: Successful results are saved locally in logs.

Mitigation: Delete or restrict access to log files when retained public-data results are no longer needed.

Risk: The skill requires an API token and may fail with 401 or 403 errors when the token is missing or invalid.

Mitigation: Provide GUAIKEI_API_TOKEN through the environment and avoid exposing the token in prompts, logs, or committed files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-detail-for-insight)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API access and documentation](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Structured JSON from Node.js CLI commands, with guidance for selecting search, detail, comment, or creator-post workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful command results are also saved under local logs.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
