## Description:

Use when someone wants light instrumental background music - an ambient bed under dialogue or underscore for reels and explainers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to guide an agent through generating light instrumental background music with Replicate's stability-ai/stable-audio-2.5 model, including prompt intake, API calling, polling, download, and basic mix guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill asks users to install multiple unpinned follow-on skills that can change agent behavior later.

Mitigation: Review the referenced PrunaAI skill sources before installation and prefer pinned versions or reviewed commits where available.

Risk: The skill sends generation prompts to Replicate and requires a Replicate API token.

Mitigation: Only provide REPLICATE_API_TOKEN in environments where sending prompts to Replicate is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/stable-audio-2-5)
- [Replicate Stable Audio 2.5 prediction API](https://api.replicate.com/v1/models/stability-ai/stable-audio-2.5/predictions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON/curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Replicate API token and ffmpeg/ffprobe for the mix step.]

## Skill Version(s):

1.0.13 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
