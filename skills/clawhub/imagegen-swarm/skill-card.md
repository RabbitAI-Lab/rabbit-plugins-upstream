## Description:

Use when the user asks to generate an image, draw, edit an image, use reference images, make a video, or do text-to-image or text-to-video. Also use when the request names Codex, Grok, Grok Imagine, Gemini, nano banana, Antigravity, Jimeng, Dreamina, Muse, or Lovart. Jimeng and Grok can make video. Jimeng can edit from up to 10 reference images, and Gemini from up to 3. Not for crop, resize, convert, or other ordinary local image processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ekko237](https://clawhub.ai/user/ekko237)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can generate images, edit images with references, and create supported videos through the skill's image-generation workflows. It can also distribute batches of image jobs across available engines and return generated files with run results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports an unsafe remote installer and notes that several scripts were only partly inspected.

Mitigation: Wait for a verifiable installation method and review the scripts before installing or running the skill.

Risk: The security assessment reports broad or weakly constrained operations and calls out approval and command restrictions for review.

Mitigation: Review the approval and command restrictions and narrow them before execution.

Risk: Prompts and reference images may pass through the multi-provider workflow.

Mitigation: Check which services will receive the content and avoid sending sensitive prompts or images unless that routing is acceptable.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/ekko237/skills/imagegen-swarm)
- [Codex engine notes](artifact/references/codex.md)
- [Lovart engine notes](artifact/references/lovart.md)
- [Lovart skill repository](https://github.com/lovartai/lovart-skill)
- [Jimeng CLI installer](https://jimeng.jianying.com/cli)

## Skill Output:

**Output Type(s):** [Image files, Video files, JSON run summaries, Shell commands, Configuration guidance]

**Output Format:** [PNG images, MP4 videos, and JSON status or batch-result data, with Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation requests can include prompts, aspect ratios, reference images, engine selection, and video options; supported limits vary by engine.]

## Skill Version(s):

1.1.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
