## Description:

Extract a SaaS-style storyboard with local reference frames, timestamps, scripts, scene descriptions, and recreation prompts from one local video or remote URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fuyunzhishang](https://clawhub.ai/user/fuyunzhishang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze one local video or HTTP(S) video URL with Pixmind, then produce a structured storyboard with reference frames, shot details, scripts, scene descriptions, and recreation prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pixmind receives the chosen video file or URL for analysis.

Mitigation: Use only videos approved for Pixmind processing and configure PIXMIND_API_KEY through the environment or client provider settings.

Risk: The skill may cache and execute downloaded Node.js or FFmpeg binaries when local tools are missing.

Mitigation: Preinstall Node.js and FFmpeg from trusted sources, or set explicit local paths before running the skill.

Risk: New submissions consume Pixmind credits based on video duration.

Mitigation: Confirm the 100 credits per started minute charge before approving a new paid analysis.

## Reference(s):

- [Pixmind Video to Prompt ClawHub Page](https://clawhub.ai/fuyunzhishang/skills/pixmind-video-to-prompt)
- [fuyunzhishang Publisher Profile](https://clawhub.ai/user/fuyunzhishang)
- [Node.js Downloads](https://nodejs.org/en/download)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands]

**Output Format:** [JSON result with storyboard data, local JPEG attachments, and a Markdown-compatible seven-column storyboard table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PIXMIND_API_KEY; new submissions require explicit user approval for Pixmind credit usage; local screenshots and result.json are saved under the configured output directory.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
