## Description:

列出视频号账号可访问的直播回放记录，包括标题、时间、时长和封面，并可获取指定回放的详细资料与互动数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and operators use this skill to retrieve WeChat Channel live replay records, inspect replay details, and export interaction metrics for livestream review or competitor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a We-Media API key and sends replay query requests to a third-party API service.

Mitigation: Use it only when the provider is trusted with the API key and the returned replay data.

Risk: Local file upload behavior can send files referenced through --file, videoUrl, or audioUrl to temporary platform storage.

Mitigation: Do not provide local file paths or local media URLs unless that upload behavior is explicitly approved.

Risk: Configuration, cached responses, and exported replay data may remain on disk after use.

Mitigation: Clear config.json, output files, and scripts/.cache when the data is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-channel-live-replay)
- [We-Media API service](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated Markdown, JSON, or Excel output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a We-Media API key; paid calls require user confirmation before execution; Excel export requires openpyxl.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
