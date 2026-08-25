## Description:

Fetches public Douyin search results, creator posts, video comments, and trending-feed data through Node.js CLI commands for downstream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to collect public Douyin data for content research, competitor analysis, sentiment review, and trend monitoring. It is not intended for video editing, publishing, private-data access, or downloading content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad auto-triggering can run the skill for generic short-video or competitor-research prompts where Douyin is not clearly intended.

Mitigation: Require explicit Douyin/public-data intent before execution and ask for confirmation when the platform is ambiguous.

Risk: The skill sends Douyin keywords, URLs, requested limits, and GUAIKEI_API_TOKEN-authenticated requests to guaikei.com.

Mitigation: Use only non-sensitive public keywords and URLs, keep the token in the environment, and rotate the token if it may have been exposed.

Risk: Fetched results are saved locally in logs by default.

Mitigation: Review or clear generated logs after runs, and avoid using the skill for searches that should not be retained locally.

Risk: The authoritative security scan marked the release suspicious because of under-scoped behavior including runtime contact messages and download-capable output fields.

Mitigation: Review the skill before installation, monitor stderr/stdout during test runs, and restrict use to public Douyin analysis workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-fetch-trending-feed)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Input and output JSON schemas](assets/)
- [Guaikei token and support site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands; CLI commands return structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16.14.0 and GUAIKEI_API_TOKEN; successful CLI runs also save fetched results under logs/ by default.]

## Skill Version(s):

1.0.0 (source: package.json, release metadata, skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
