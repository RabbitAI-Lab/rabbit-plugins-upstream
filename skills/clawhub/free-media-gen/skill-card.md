## Description:

Free Media Gen（免费生图生视频） helps agents generate images and videos through configured third-party media APIs such as Agnes, SenseNova, and SiliconFlow Kolors while bypassing WorkBuddy Hunyuan ImageGen.

This skill is ready for commercial/non-commercial use.

## Publisher:

[igenomed](https://clawhub.ai/user/igenomed)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to discover configured free media-generation backends, generate images or videos from prompts, and optionally audit model availability before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads API keys from WorkBuddy models.json and sends prompts, generation parameters, and media-generation requests to third-party providers.

Mitigation: Use dedicated or scoped API keys where possible and avoid sensitive prompts unless those providers are approved for the content.

Risk: Third-party free quotas and pricing may change, so a model described as free may later require paid access or fail quota checks.

Mitigation: Review provider pricing before use and run the skill's model audit when availability or pricing is uncertain.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/igenomed/skills/free-media-gen)
- [WorkBuddy homepage](https://www.workbuddy.cn)
- [Known free media model catalog](references/model_catalog.md)
- [Free media model platform reference](references/platforms.md)
- [Portable path resolver](references/resolve_paths.py)
- [Agnes](https://agnes-ai.cn)
- [SenseNova](https://www.sensenova.cn)
- [SiliconFlow](https://cloud.siliconflow.cn)
- [Google AI Studio](https://aistudio.google.com)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON script results, and local image, video, or audit report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved to workspace output folders; the skill reads configured WorkBuddy model keys and sends prompts and generation parameters to selected third-party providers.]

## Skill Version(s):

1.0.0 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
