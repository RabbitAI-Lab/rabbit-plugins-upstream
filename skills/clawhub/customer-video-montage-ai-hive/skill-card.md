## Description:

This skill helps e-commerce, community, and user-content teams turn authorized customer review videos into montage plans, runnable AI-HIVE commands, and deliverable short-video assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce brands, community operators, and marketing teams use this skill to convert authorized customer-review footage, product facts, channel constraints, and music permissions into auditable montage workflows, scripts, prompts, local video-processing commands, AI-HIVE generation tasks, and acceptance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses or stores an AI-HIVE API key.

Mitigation: Keep API keys out of logs and repositories, prefer environment variables or a permissions-restricted config file, and rotate any exposed key.

Risk: Customer footage, music, logos, claims, or likenesses may be uploaded to AI-HIVE or object storage without sufficient rights.

Mitigation: Verify authorization and usage rights before upload, remove sensitive order or user data unless approved, and mark unsupported claims as requiring human verification.

Risk: Generation jobs can incur costs after parameters are approved.

Mitigation: Show the final prompt, model, routing mode, and pricing snapshot before submission, and use small samples before batch generation.

Risk: Broad brand-ad trigger phrases could invoke the workflow for unrelated or unsuitable content.

Mitigation: Confirm the user intends authorized customer-review or marketing montage work before using AI-HIVE generation or media upload steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/customer-video-montage-ai-hive)
- [AI-HIVE chat and API access entry](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON briefs, Python command examples, shell commands, task records, and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE routing choices, pricing snapshots, task IDs, downloaded file paths, ffmpeg outputs, and review checkpoints.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
