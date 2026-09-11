## Description:

Free Media Gen provides a WorkBuddy/OpenClaw entry point for free text-to-image and text-to-video generation through third-party providers including Agnes, SenseNova, and SiliconFlow Kolors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[igenomed](https://clawhub.ai/user/igenomed)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to route media-generation prompts to configured free third-party image and video APIs, list available models, and optionally audit model availability. It is designed for WorkBuddy/OpenClaw environments that already store provider API keys in a compatible models.json registry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, request metadata, and generated media requests are sent to third-party providers using API keys from the user's WorkBuddy models.json.

Mitigation: Avoid sensitive or regulated prompts and review the configured provider endpoints before use.

Risk: Stored API keys and skill configuration can affect where requests are sent and which credentials are used.

Mitigation: Restrict who can edit models.json and the skill config, and rotate provider keys through the provider consoles as needed.

Risk: The audit option may consume provider quota and update local files.

Mitigation: Run audits intentionally, review generated audit reports, and use the no-live audit mode when live generation is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/igenomed/skills/free-media-gen)
- [WorkBuddy homepage](https://www.workbuddy.cn)
- [Known free media model catalog](artifact/references/model_catalog.md)
- [Media platform reference](artifact/references/platforms.md)
- [Agnes](https://agnes-ai.cn)
- [SenseNova](https://www.sensenova.cn)
- [SiliconFlow Cloud](https://cloud.siliconflow.cn)
- [SiliconFlow pricing](https://www.siliconflow.cn/pricing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance, shell commands, JSON status objects, generated image/video files, and Markdown audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is saved to the resolved workspace output directories; the optional audit flow can update the skill config and write a dated Markdown report.]

## Skill Version(s):

1.1.0 (source: server release metadata, SKILL.md frontmatter, README changelog, and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
