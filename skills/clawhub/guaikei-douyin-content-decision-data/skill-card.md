## Description:

Provides structured JSON data from Douyin public sources for keyword search, creator post collection, video comment retrieval, and real-time trending-list queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and content teams use this skill to collect Douyin public data for content research, competitor analysis, sentiment review, topic exploration, and trend monitoring. It is not intended for publishing, editing, downloading videos, follower-growth consulting, private data access, or non-Douyin platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party GUAIKEI API token is required for Douyin public-data queries.

Mitigation: Provide the token only through GUAIKEI_API_TOKEN, avoid sharing it in prompts or outputs, and rotate it if it may have been exposed.

Risk: Successful searches, creator-post fetches, and comment fetches may be saved locally in the skill's logs directory.

Mitigation: Review or delete generated logs after use, especially when queries or returned public data are sensitive to the team.

Risk: Broad automatic triggers can route ambiguous short-video research requests to Douyin.

Mitigation: Use explicit Douyin-scoped prompts and confirm the intended platform when the user asks for general social or short-video research.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-content-decision-data)
- [Readme](readme.md)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [GUAIKEI Token and Support Site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON output conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill's command-line tools emit JSON to stdout, write logs to stderr, and save successful search, creator-post, and comment results under logs/.]

## Skill Version(s):

1.0.0 (source: package.json, references/changelog.md, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
