## Description:

This skill helps Chinese short-video creators, brand producers, and subtitle editing teams analyze viral captions and copy, produce differentiated scripts and prompts, and optionally run AI-HIVE media-generation or local ffmpeg helper workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketing teams, and production editors use this skill to turn Chinese short-video caption and copy requests into reviewable breakdowns, differentiated remake plans, shot-by-shot scripts, prompts, runnable AI-HIVE commands, and quality checklists. It is intended for authorized marketing, ecommerce, social media, short-drama, and product-promotion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE media generation can involve paid API calls and asynchronous downloads.

Mitigation: Confirm prompts, routing mode, model parameters, and budget before submitting generation tasks; start with a small sample for batch work.

Risk: The workflow handles API keys, media uploads, downloads, and local ffmpeg file operations.

Mitigation: Use environment variables or local config for credentials, avoid sharing keys in chat or logs, review commands before running them, and upload only media the user is authorized to use.

Risk: Caption and copy analysis can produce misleading claims, overly similar remakes, or unauthorized use of protected material if source facts and rights are not checked.

Mitigation: Require factual product or brand support, confirm reference-material authorization, avoid copying protected dialogue or visual identity, and keep distinct scripts, scenes, characters, and CTAs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/viral-video-caption-copy-analyzer-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured sections, inline shell commands, optional Python-generated JSON files, and task records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include captions, copy rewrites, CTA variants, shot lists, prompts, AI-HIVE routing choices, price snapshots, task IDs, status records, download locations, and ffmpeg command output paths.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
