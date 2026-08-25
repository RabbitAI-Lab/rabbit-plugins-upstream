## Description:

Retrieves structured public Douyin data for keyword search, creator post collection, video comment analysis, and real-time hot-list tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and content analysts use this skill to collect public Douyin records for content research, competitor account analysis, comment insight, and trend tracking. It is intended for Douyin public data workflows and does not support publishing, editing, downloading, private account data, or other short-video platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad automatic triggering can route generic short-video research prompts into Douyin collection.

Mitigation: Use explicit Douyin-only prompts and confirm intent before running commands for ambiguous research requests.

Risk: Collected public social-media records are automatically retained in local JSON logs.

Mitigation: Periodically delete logs that contain comments, profile URLs, user identifiers, or other sensitive research outputs.

Risk: Requests send Douyin keywords, profile or video URLs, requested limits, and token-backed calls to guaikei.com.

Mitigation: Install only when that data flow is acceptable for the workspace and keep GUAIKEI_API_TOKEN scoped and protected.

Risk: Runtime contact or marketing output may appear despite the skill documentation's neutral-error guidance.

Mitigation: Review error output before sharing it with end users and remove promotional or contact details from user-facing responses.

## Reference(s):

- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Input and Output JSON Schemas](assets/)
- [Guaikei Token and Help Site](https://www.guaikei.com)
- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-public-records)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that produce JSON on stdout and local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=16.14 and GUAIKEI_API_TOKEN; individual commands can return up to 10000 public records.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
