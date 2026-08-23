## Description:

Generates controlled Nano Banana Pro images from multiple reference images by assigning each reference a clear role for identity, product facts, composition, material, color, background, lighting, or style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and developers use this skill to combine people, products, layouts, materials, and brand style references into a controlled AI Hive image generation request. It helps agents produce role-specific prompts, upload ordered reference images, submit Nano Banana Pro generation tasks, and retrieve task results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key and supports persistent local credential configuration.

Mitigation: Use a scoped key where possible, prefer environment-based configuration for short-lived use, and review local config permissions before installation.

Risk: Reference images selected by the user are uploaded to AI Hive for generation.

Mitigation: Do not pass sensitive, private, or unauthorized local files as references; review each input path before running generate.

Risk: The bundled helper includes broader generic AI Hive capabilities than the multi-reference image workflow advertises.

Mitigation: Use the documented init, generate, and task commands for this skill and review any other helper subcommands before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-multi-reference-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access portal](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples; executed helper commands submit AI Hive tasks and may download generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key via CLI, AI_HIVE_API_KEY, or local config; selected reference files are uploaded to AI Hive for generation.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
