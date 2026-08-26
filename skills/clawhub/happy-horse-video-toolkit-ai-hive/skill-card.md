## Description:

Use this skill when a creator or commercial team needs to turn Happy Horse, AI video, reference-based video, or video-editing requests into T2V/I2V/R2V mode recommendations, prompts, executable AI-HIVE tasks, and delivery checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketing teams, ecommerce operators, and developers use this skill to plan, generate, track, download, and check short-form commercial video assets with AI-HIVE. It supports production briefs, shot scripts, prompts, shell commands, media uploads, task polling, downloaded outputs, and deterministic ffmpeg edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store and use an AI-HIVE API key.

Mitigation: Use a personal authorized key only, avoid shared environments, keep local configuration private, and do not commit or paste real API keys into logs or prompts.

Risk: The skill can upload user-provided media and submit potentially billable generation tasks.

Mitigation: Confirm media rights, final prompt parameters, routing mode, model choice, and budget before generation; run a small sample before batch work.

Risk: Reference-based workflows can produce content too similar to protected source material or imply unauthorized endorsement.

Mitigation: Reuse only abstract structure, timing, and evidence patterns; replace protected dialogue, characters, logos, watermarks, music, and specific shot composition.

Risk: Commercial video outputs can contain inaccurate product, performance, price, market, or platform claims.

Mitigation: Require factual sources for claims, mark company-provided data where applicable, and avoid guarantees about traffic, sales, ranking, approval, or return on investment.

## Reference(s):

- [Happy Horse 视频工具箱 AI-HIVE entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/happy-horse-video-toolkit-ai-hive)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON task records, local media files, and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create blueprint JSON, upload authorized media, submit potentially billable AI-HIVE generation tasks, poll task status, and download generated files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
