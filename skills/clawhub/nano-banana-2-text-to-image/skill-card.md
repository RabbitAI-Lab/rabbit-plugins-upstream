## Description:

Nano Banana 2 文生图 helps agents turn text prompts into image concepts through AI Hive, supporting product scenes, social visuals, educational illustrations, environment concepts, and batch creative variants without using reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, designers, and developers use this skill to generate and iterate text-only image concepts for commerce, social media, education, environment design, product scenes, and creative variants through AI Hive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and the AI Hive API key are used with AI Hive.

Mitigation: Use an API key with appropriate account limits and avoid placing sensitive information in prompts.

Risk: Generated images are saved locally.

Mitigation: Choose an appropriate output directory and handle generated files according to the user's data handling requirements.

Risk: Generated concept images could be mistaken for real products, buildings, or documentary photos.

Mitigation: Label generated images as concepts and do not present them as already-produced products, real buildings, or documentary photographs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-text-to-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash command examples; CLI output includes task JSON and downloaded PNG files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI_HIVE_API_KEY or local ~/.ai-hive/config.json; prompts are sent to the fixed AI Hive API and generated images are saved locally.]

## Skill Version(s):

1.0.1 (source: evidence.release.version and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
