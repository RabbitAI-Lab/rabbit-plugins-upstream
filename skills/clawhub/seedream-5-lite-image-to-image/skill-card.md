## Description:

Uses Seedream 5.0 Lite through AI Hive to redraw authorized reference images with region-based controls for locked, modified, and rebuildable areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, designers, and developers use this skill to make controlled image-to-image edits from authorized reference images, including sketch rendering, local object replacement, aspect-ratio expansion, style conversion, and commercial image iteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are uploaded to AI Hive for generation.

Mitigation: Use only images you are authorized to upload and review privacy, rights, brands, people, and evidentiary sensitivity before submission.

Risk: Generated edits can materially alter people, brands, artworks, news, or evidence-relevant imagery.

Mitigation: Obtain authorization, clearly label substantial edits, and compare locked regions against the original before use.

Risk: The AI Hive API key may be stored locally.

Mitigation: Use environment variables or the init flow's 0600 config file permissions; rotate keys if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-image-to-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands; generated image files are saved locally by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least one user-selected reference image and an AI Hive API key; generated results default to ~/Downloads/AiHive.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
