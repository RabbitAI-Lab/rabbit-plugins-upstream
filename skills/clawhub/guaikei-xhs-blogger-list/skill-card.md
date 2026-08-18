## Description:

Fetches recent public Xiaohongshu notes by keyword and supports note detail, creator post monitoring, and comment retrieval for trend and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, brand marketers, market researchers, and data analysts use this skill to collect public Xiaohongshu content, creator posts, and comments for topic research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or URLs and the configured Guaikei API token to guaikei.com.

Mitigation: Use only when data sharing with Guaikei is acceptable, and provide tokens through managed environment variables rather than user-visible prompts.

Risk: Fetched public data can be saved in local JSON logs.

Mitigation: Review local log retention and access controls before running the skill on sensitive research topics.

Risk: The release has scope-labeling issues because the skill name emphasizes blogger lists while the artifact also supports keyword search, note details, and comments.

Mitigation: Review the documented command routes and enable only the capabilities appropriate for the agent workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-blogger-list)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, guidance]

**Output Format:** [Command guidance and structured JSON results from the Xiaohongshu CLI scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; fetched results may be saved in local logs.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
