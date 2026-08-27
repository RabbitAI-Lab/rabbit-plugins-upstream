## Description:

Collects public Douyin keyword search results, account posts, video comments, and real-time trending lists as structured JSON for content research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, and researchers use this skill to gather public Douyin search, post, comment, and hot-list data for short-video planning, competitor monitoring, public-opinion analysis, and trend discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run for generic short-video research requests and collect Douyin public data even when the user does not explicitly name Douyin.

Mitigation: Use it only when Douyin data collection is intended, and confirm the platform and scope before running broad research workflows.

Risk: Collected search, post, and comment results may be saved locally under the skill's logs directory.

Mitigation: Delete or protect logs that contain user-generated comments, account metadata, or business research.

Risk: The skill requires a GUAIKEI_API_TOKEN for API access.

Mitigation: Keep the token in the environment, avoid sharing it, and verify it is not written to logs or output.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-keyword-index-ranker)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [JSON schemas](assets/*.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON on stdout with optional JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs Douyin search, post, comment, and hot-list records; local logs may include collected user-generated comments, account metadata, or business research.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog, constants.js)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
