## Description:

AI视频剪辑工具箱｜AI-HIVE helps editors, operators, and merchants turn short-video editing requests into reviewable production plans, local ffmpeg commands, AI-HIVE generation steps, task records, and delivery checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, e-commerce operators, and merchants use this skill to plan, inspect, resize, trim, mute, normalize, concatenate, and augment short-form commercial videos. The skill favors reviewable local edits first and uses AI-HIVE generation only after confirming prompts, routing mode, cost-sensitive settings, and source-media authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation can incur cost when image or video jobs are submitted.

Mitigation: Show the final prompt, generation mode, routing mode, model choice, and price snapshot before submitting paid or batch tasks.

Risk: Uploaded media may include copyrighted, trademarked, private, or otherwise unauthorized material.

Mitigation: Use only media the user has rights to use, and provide abstract structure guidance when authorization is unclear.

Risk: API keys can be exposed through logs, screenshots, command history, or repositories.

Mitigation: Use placeholders in examples, prefer environment variables or the local config file, keep the config file permission-restricted, and do not echo real keys.

Risk: Commercial video outputs may contain unsupported product claims, fake testimonials, platform-rule evasion, or misleading performance promises.

Mitigation: Require source-backed factual claims, avoid impersonation or fake endorsements, and keep human review before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/video-editing-toolkit-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON records and inline bash or Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local file paths, ffmpeg command lines, AI-HIVE routing choices, pricing snapshots, taskId values, task status, downloaded output locations, and acceptance-check results.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
