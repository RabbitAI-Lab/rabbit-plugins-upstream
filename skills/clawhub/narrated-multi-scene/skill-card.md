## Description:

Use when someone wants a multi-part story with voiceover - episodic B-roll, chaptered promo, or several linked video scenes without on-camera dialogue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to coordinate a gated workflow for multi-scene narrated videos: plan scenes, generate and review stills and voiceover, create clips, and assemble the final film with ffmpeg.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned npx install examples can introduce supply-chain drift.

Mitigation: Install only from a trusted PrunaAI source and prefer pinned or reviewed installers when available.

Risk: The workflow may upload media, voiceover, and generated assets to external media-generation services.

Mitigation: Confirm rights, privacy expectations, and suitability of inputs before upload.

Risk: Narration-led video clips can truncate if an audio line exceeds the stated service limit.

Mitigation: Run the documented ffprobe duration gate and shorten, split, or regenerate narration before video generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/narrated-multi-scene)
- [Pruna AI publisher profile](https://clawhub.ai/user/pruna-ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with tables, JSON request examples, and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes gated review checkpoints for plan, stills, clips, and audio duration checks before video generation.]

## Skill Version(s):

1.0.13 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
