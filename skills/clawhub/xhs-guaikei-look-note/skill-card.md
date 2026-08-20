## Description:

Retrieves public Xiaohongshu content, note details, comments, and creator post lists through GUAIKEI so agents can support trend research, competitor monitoring, KOL screening, and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, analysts, and agent developers use this skill to query public Xiaohongshu keywords, inspect public notes and comments, and monitor public creator profiles for content planning, competitor research, trend analysis, and KOL evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, and retrieved public data are sent to the third-party GUAIKEI API service with the user's API token.

Mitigation: Use the skill only when third-party API processing is acceptable for the user's workflow, and avoid submitting confidential or sensitive analysis targets.

Risk: The required GUAIKEI_API_TOKEN can enable API access if exposed in chat transcripts, repositories, shell history, or logs.

Mitigation: Store the token in an environment variable or secret manager, avoid pasting it into prompts or source files, and rotate it if exposure is suspected.

Risk: The skill is scoped to public Xiaohongshu data and can return empty or error responses for private, deleted, login-required, or unavailable content.

Mitigation: Do not infer missing data; verify links and report empty or error responses clearly before drawing conclusions.

Risk: Successful command runs can save fetched public posts or comments to local JSON logs, which may retain sensitive business research context.

Mitigation: Periodically review and clean the logs directory, especially when research targets, comments, or competitor analyses are sensitive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/xhs-guaikei-look-note)
- [GUAIKEI API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful command runs may also write JSON result logs under the skill's logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
