## Description:

Retrieves structured public Xiaohongshu search, note-detail, creator-post, and comment data for content research, KOL screening, and interaction-quality analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Marketing, content, and research teams use this skill to gather public Xiaohongshu notes, comments, and creator posts so an agent can summarize trends, compare competitor content, and prepare KOL or campaign analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the GUAIKEI API token, Xiaohongshu keywords, target URLs, and requested limits to guaikei.com.

Mitigation: Use the skill only when that third-party sharing is acceptable, and run it only against public, authorized targets.

Risk: Returned comments and profile data may contain personal or sensitive business information.

Mitigation: Use explicit result limits and handle returned data according to applicable privacy and business data rules.

Risk: Successful runs can save fetched results locally as JSON logs.

Mitigation: Protect or delete generated logs when they contain sensitive business or personal data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-comment-grabber)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Structured JSON command results with status, request metadata, skill metadata, and results; guidance may include Markdown with inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful command runs may save JSON result logs locally under the skill's logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
