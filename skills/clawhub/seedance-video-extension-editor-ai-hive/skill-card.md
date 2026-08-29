## Description:

Seedance 视频编辑与延长｜AI-HIVE helps editors, ad post-production teams, and ecommerce content teams turn video editing or extension requests into reviewable plans, AI-HIVE generation parameters, local editing commands, task records, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, ad post-production teams, and ecommerce marketers use this skill to plan Seedance video editing or extension work, separate deterministic ffmpeg edits from generative AI-HIVE tasks, and produce auditable commands, prompts, task records, and quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid AI-HIVE generation could be submitted with unintended prompts, routing, or budget impact.

Mitigation: Review final prompts, parameters, routing mode, and price snapshot before submitting generation tasks; use a small sample before batch work.

Risk: Uploaded media or requested edits may involve content the user is not authorized to use.

Mitigation: Confirm media rights before upload or generation, and limit unsupported reference material to abstract structure guidance.

Risk: API keys may be exposed through logs, screenshots, shell history, or repositories.

Mitigation: Use environment variables or the local AI-HIVE config file, keep config permissions restricted, and avoid echoing or committing real API keys.

Risk: Changing AI_HIVE_BASE_URL or --base-url can send credentials and media to an untrusted endpoint.

Mitigation: Use the default AI-HIVE endpoint unless the alternate endpoint is explicitly trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-video-extension-editor-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON artifacts and bash/Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include AI-HIVE routing choices, price snapshots, task IDs, local file paths, and acceptance checks.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
