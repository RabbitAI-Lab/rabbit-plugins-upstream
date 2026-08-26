## Description:

Collects structured JSON from public Douyin search results, creator posts, video comments, and hot lists for content research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to collect public Douyin data for short-video topic research, competitor monitoring, comment analysis, and trend tracking. It is not intended for publishing videos, editing media, downloading assets, or collecting private platform data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-trigger on broad or vague research requests.

Mitigation: Confirm that the user intends Douyin public-data collection before running commands.

Risk: Raw search, post, and comment results may be saved locally under the skill logs directory.

Mitigation: Run in a private workspace and remove logs that are no longer needed.

Risk: The skill requires GUAIKEI_API_TOKEN.

Mitigation: Treat the token as a secret and provide it only through the environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-deep-dive-collector)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Input and output JSON schemas](assets/*.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands]

**Output Format:** [Structured JSON on stdout with optional JSON log files under logs/.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; command arguments select search, creator-post, comment, or hot-list collection.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
