## Description:

Converts reference images or text descriptions into platform-ready video direction, prompts, shot plans, motion settings, and optional generation or post-production steps for short videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yeshenyue12345](https://clawhub.ai/user/yeshenyue12345)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and developers use this skill to turn images or text concepts into video-generation prompts, platform routing choices, storyboard tables, and optional local media assembly commands for short social, product, poster, and cinematic clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run local Python media scripts that write or overwrite requested audio and video output files.

Mitigation: Review output paths before execution and run the scripts in a managed working directory.

Risk: Voice-line generation uses online edge-tts and may send provided text to an external TTS service.

Mitigation: Avoid sending sensitive, confidential, or private text to TTS and confirm network use before voice generation.

Risk: Generated media prompts and edits can alter identity, labels, logos, or factual meaning if used carelessly.

Mitigation: Keep protected visual anchors static where needed, review generated outputs before publication, and avoid misleading transformations.

## Reference(s):

- [Platform routing and syntax adaptation](references/platform-routing.md)
- [Image-to-video prompt patterns](references/prompt-patterns.md)
- [ClawHub skill page](https://clawhub.ai/yeshenyue12345/skills/multi-platform-video-director)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown with prompt blocks, parameter tables, JSON tool-call examples, shell commands, and local media file outputs when helper scripts are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce platform-specific prompts, negative prompts or fidelity constraints, shot lists, video-generation settings, local WAV/MP3/MP4 outputs, subtitle-burned videos, muxed audio, or stitched multi-shot videos.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
