## Description:

Use when the user asks to generate an image, draw, edit an image, use reference images, make a video, or do text-to-image or text-to-video. Also use when the request names Codex, Grok, Grok Imagine, Gemini, nano banana, Antigravity, Jimeng, Dreamina, Muse, Lovart, gpt-image, or a pay-per-image API. Jimeng and Grok can make video. An optional pay-per-image API line (OpenAI or Gemini API) takes over when every subscription is out. Jimeng can edit from up to 10 reference images, and Gemini from up to 3. Not for crop, resize, convert, or other ordinary local image processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ekko237](https://clawhub.ai/user/ekko237)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use the skill to generate and edit images, create videos, and route jobs across supported image-generation services, including optional pay-per-image APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports risky command scope, sandbox escalation, and file deletion behavior, with only partial inspection of the artifact.

Mitigation: Review the reported command scope, sandbox retry, deletion behavior, required access, and scan coverage before installing.

Risk: ClawScan reports spending-limit weaknesses, and optional pay-per-image generation can incur costs.

Mitigation: Review paid API configuration, spending limits, and expected usage before enabling pay-per-image generation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/ekko237/skills/imagegen-swarm)
- [Codex image-generation notes](references/codex.md)
- [Lovart integration notes](references/lovart.md)
- [Lovart upstream skill reference](https://github.com/lovartai/lovart-skill)

## Skill Output:

**Output Type(s):** [Image files, Video files, JSON reports, Shell commands]

**Output Format:** [PNG images, MP4 videos, JSON batch reports, and terminal status lines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Jobs can specify prompts, aspect ratios, reference images, video generation, and an image-generation engine.]

## Skill Version(s):

1.2.3 (source: SKILL.md frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
