## Description:

This skill helps ad buyers, creative directors, agencies, and growth teams decompose authorized winning ads into transferable variables, original scripts, prompts, runnable AI-HIVE commands, and review checklists without copying protected expression.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External advertising, ecommerce, marketing, short-video, and social content teams use this skill to analyze authorized reference ads, extract hooks, personas, scenes, proof points, rhythm, CTA variables, and create original test plans. When media generation is needed, it guides confirmed AI-HIVE OpenAPI calls, uploads authorized references, records routing and task details, and downloads generated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and media files may be sent to AI-HIVE during generation workflows.

Mitigation: Use only authorized reference materials and avoid submitting sensitive or unapproved media.

Risk: AI-HIVE API keys may be exposed if stored in shared environments, logs, screenshots, or repositories.

Mitigation: Use environment variables or a private local config with restricted permissions, and keep placeholder keys in examples.

Risk: Image or video generation may incur charges after task submission.

Mitigation: Review the final prompt, routing mode, model choice, and pricing snapshot before submitting generation jobs.

Risk: Advertising analysis or generated content may include unsupported product claims, copied expression, or misleading performance promises.

Mitigation: Verify product facts, rights, platform constraints, and originality before publication; treat winning-ad history as input data, not a future performance guarantee.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/winning-ad-variable-decomposer-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with command examples, JSON briefs or task records, and generated media file paths when downloads complete.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE routing mode, model and pricing snapshot, taskId, status, and local download paths after user confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
