## Description:

AI UGC广告生成器｜AI-HIVE helps ecommerce merchants, media buyers, brand content teams, and UGC ad creators turn product facts and authorized assets into UGC ad concepts, realistic scripts, storyboards, key-frame prompts, generation tasks, and acceptance checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce and advertising teams use this skill to plan UGC-style commercial content from verified product facts, authorized media, platform constraints, and budget preferences. It can produce reviewable campaign structure, scripts, prompts, AI-HIVE image or video task commands, task records, and acceptance criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE API credentials may be stored locally or supplied through the environment.

Mitigation: Use a dedicated API key, keep config files permission-restricted, prefer environment variables for temporary use, and do not paste or log real keys.

Risk: Reference images or videos are uploaded to an external generation service.

Mitigation: Upload only media the user is authorized to use, avoid sensitive private footage, and confirm platform and consent constraints before generation.

Risk: Image or video generation can create billable API tasks.

Mitigation: Show final prompts, routing mode, model choices, and expected task parameters before submission; run a small sample before batch generation.

Risk: UGC-style advertising can mislead audiences if testimonials, product effects, or performance claims are invented.

Mitigation: Ground claims in supplied evidence, mark unknown facts for review, avoid fake consumer identities, and disclose synthetic people according to platform rules.

Risk: Local ffmpeg edits can overwrite generated outputs or produce platform-specific crops that omit important content.

Mitigation: Preserve original files, choose explicit output paths, and review aspect-ratio conversions before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ugc-ad-generator-ai-hive)
- [AI-HIVE application](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON file outputs and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI-HIVE image or video generation tasks after user confirmation; deterministic video inspection and edits use local ffmpeg commands.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
