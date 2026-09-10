## Description:

Fetches public Kuaishou video search results, creator posts, and video comments through Guaikei and returns structured JSON for content research, competitor monitoring, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, content operators, and analysts use this skill to collect public Kuaishou search, creator-post, and comment data for topic research, KOL screening, competitor monitoring, and sentiment review. The skill requires a GUAIKEI_API_TOKEN and a keyword, profile URL, user ID, video URL, or video ID depending on the requested task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile or video URLs, and GUAIKEI_API_TOKEN are sent to the guaikei.com API.

Mitigation: Confirm that the user or organization approves this third-party API use before running the skill, and provide the token only through the expected environment variable.

Risk: Successful task results are retained locally under logs/ by default, which may expose sensitive research, comments, or competitor monitoring outputs.

Mitigation: Review, protect, or delete generated logs after use when the collected data or research intent is sensitive.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-visible-content-fetcher)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API access and support](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results include status, error_code, request metadata, runtime metadata, and results; successful runs are saved under logs/ by default.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, and changelog; artifact SKILL.md metadata reports 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
