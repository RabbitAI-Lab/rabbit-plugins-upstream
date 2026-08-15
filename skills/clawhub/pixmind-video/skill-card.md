## Description:

Generate AI videos via Pixmind API (text-to-video and image-to-video).

This skill is ready for commercial/non-commercial use.

## Publisher:

[fuyunzhishang](https://clawhub.ai/user/fuyunzhishang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate text-to-video or image-to-video content through the Pixmind API and poll generation tasks for final video and cover URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PixMind API keys, prompts, and reference image URLs are sent to PixMind API services and may incur usage costs.

Mitigation: Use a scoped or revocable PixMind API key where possible, avoid submitting sensitive prompts or private image URLs, and monitor API usage.

Risk: Video generation depends on model-specific constraints and task polling, so unsupported model, resolution, aspect ratio, or duration choices can fail.

Mitigation: Use the model table and documented defaults in the skill, confirm prompt, duration, and model before generation, and poll task status until completion or failure.

## Reference(s):

- [Pixmind](https://www.pixmind.io)
- [Pixmind API Platform Dashboard](https://www.pixmind.io/api-platform/dashboard/keys)
- [ClawHub Skill Page](https://clawhub.ai/fuyunzhishang/skills/pixmind-video)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PIXMIND_API_KEY and sends prompts, reference image URLs, and task requests to PixMind API services.]

## Skill Version(s):

2.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
