## Description:

Routes Xiaohongshu links and keywords to public content search, note detail retrieval, comment retrieval, or creator post retrieval for Xiaohongshu content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, analysts, and agent operators use this skill to retrieve public Xiaohongshu search results, note details, comments, and creator posts for topic research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, links, and fetched public data are sent to guaikei.com.

Mitigation: Use only public, authorized inputs and confirm the user accepts third-party API processing before running commands.

Risk: JSON results may be written to local logs.

Mitigation: Clear local logs when results are no longer needed, especially for sensitive research or client work.

Risk: GUAIKEI_API_TOKEN is required for API access.

Mitigation: Keep the token private in environment variables or secret storage and do not paste it into prompts, logs, or shared files.

Risk: The skill is not intended for private, login-only, or legally restricted content.

Mitigation: Decline those requests and limit use to public Xiaohongshu data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-creator-posts)
- [Guaikei API token and support](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; command results may be saved under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
