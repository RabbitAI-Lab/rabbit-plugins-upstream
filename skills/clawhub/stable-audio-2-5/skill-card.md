## Description:

Use when someone wants light instrumental background music, such as an ambient bed under dialogue or underscore for reels and explainers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to craft Replicate Stable Audio 2.5 prompts and API calls for light instrumental background beds, then download and mix generated MP3 output under narration or video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote prerequisite install commands can add or update skills from a remote repository.

Mitigation: Review each npx skills add command and installed skill content before running generation workflows.

Risk: Secrets or sensitive private content may be exposed if included in prompts sent to Replicate.

Mitigation: Do not place secrets or sensitive private content in audio prompts.

Risk: Missing local media tools can block the mix step.

Mitigation: Confirm ffmpeg and ffprobe are installed on PATH before planning a mixed audio deliverable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/stable-audio-2-5)
- [Replicate Stable Audio 2.5 prediction API](https://api.replicate.com/v1/models/stability-ai/stable-audio-2.5/predictions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of REPLICATE_API_TOKEN, Replicate prediction polling, MP3 download, and optional ffmpeg-based mixing.]

## Skill Version(s):

1.0.11 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
