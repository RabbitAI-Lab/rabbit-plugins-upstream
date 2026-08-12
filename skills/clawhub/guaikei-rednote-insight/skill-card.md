## Description:

Searches public Xiaohongshu/Rednote notes by keyword and retrieves note details, comments, and creator posts as structured data for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and analysts use this skill to search public Xiaohongshu/Rednote content, inspect note and comment data, monitor creator posts, and prepare downstream trend, competitor, KOL, and topic analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu URLs, and the GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use a token obtained through a trusted channel, avoid sensitive business research inputs in shared environments, and confirm that external data transfer is acceptable for the use case.

Risk: Skill results are saved automatically to a local logs directory.

Mitigation: Protect the workspace and periodically delete or archive logs when results contain sensitive research or campaign information.

Risk: The skill depends on a third-party API and public Xiaohongshu data availability.

Mitigation: Do not use it for private or login-gated content, and handle empty, rate-limited, timeout, or error responses before drawing conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-insight)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance, Text]

**Output Format:** [Structured JSON from CLI tools, with concise text or Markdown summaries when useful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes result logs locally under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
