## Description:

Helps agents create or edit Nano Banana 2 seeding images with realistic usage context, observable details, disclosure space, and safeguards against presenting synthetic content as real user experience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing creators, social commerce teams, and agents use this skill to draft image-generation or image-editing workflows for product seeding content on social platforms. It emphasizes authorized reference assets, observable product details, platform disclosure space, and review before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to AI Hive for generation or editing.

Mitigation: Use only content that is approved for external processing and avoid uploading sensitive, private, or unauthorized assets.

Risk: Generated product seeding images may be mistaken for real user experience or undisclosed advertising.

Mitigation: Keep disclosure space in the image plan, label AI-generated or sponsored content as appropriate, and review platform advertising rules before publishing.

Risk: API keys may be stored locally or passed on the command line.

Mitigation: Prefer environment or least-privilege local configuration, keep the config file private, and rotate keys if they are exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-seeding-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with bash commands, JSON configuration, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed Nano Banana 2 public model through AI Hive; generated results are saved locally unless download is disabled.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
