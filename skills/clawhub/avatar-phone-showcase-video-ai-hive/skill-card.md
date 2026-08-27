## Description:

Creates Chinese AI-HIVE production workflows for avatar phone showcase videos, including briefs, scripts, prompts, runnable commands, generation task records, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External App, e-commerce, education, and internet product marketing teams use this skill to turn authorized people references, real interface screenshots, product facts, platform constraints, duration, and CTA into avatar-led phone showcase video plans and deliverables. Developers and operators can also use the bundled scripts to prepare production briefs, submit AI-HIVE video jobs, poll tasks, download outputs, and run deterministic local video checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may submit potentially billable AI-HIVE generation jobs.

Mitigation: Review the prompt, routing mode, model choice, and pricing snapshot before execution; use a small sample before batch generation.

Risk: The workflow can upload selected media and use an AI-HIVE API key.

Mitigation: Use only authorized reference materials, keep API keys out of logs and screenshots, and prefer environment variables or a local config file with restricted permissions.

Risk: Generated marketing content can misstate product facts, screenshots, prices, performance, or endorsements.

Mitigation: Use real interface screenshots, mark unverifiable claims as needing review, and do not present generated content as official endorsement or user testimony without authorization.

Risk: Reference-driven video work can become too similar to protected or unauthorized source material.

Mitigation: Retain only abstract structure from references unless rights are confirmed, and rewrite people, scenes, dialogue, camera direction, music, logos, and visual style.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/avatar-phone-showcase-video-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands, JSON task records, and generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE routing mode, model selection, pricing snapshot, taskId, status, download locations, and video acceptance checks.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
