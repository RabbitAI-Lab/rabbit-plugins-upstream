## Description:

Use when someone wants an original AI song with vocals: sung lyrics, a style prompt track, or source audio for a music video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to guide an agent through generating original songs with vocals from lyrics and an optional style prompt through Replicate's MiniMax music-2.5 model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends lyrics and prompts to an external provider through Replicate.

Mitigation: Avoid submitting private or sensitive lyrics, prompts, or source material, and review MiniMax and Replicate handling policies before use.

Risk: The skill depends on Replicate credentials and may trigger paid external API calls.

Mitigation: Use a Replicate token with appropriate account limits and confirm required inputs before making prediction requests.

Risk: The skill asks agents to install related Pruna dependency skills before generation.

Mitigation: Verify the Pruna dependency skills before installation and allow only dependencies needed for the intended workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/music-2-5)
- [MiniMax privacy policy](https://www.minimax.io/platform/protocol/privacy-policy)
- [Replicate MiniMax music-2.5 prediction endpoint](https://api.replicate.com/v1/models/minimax/music-2.5/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline bash, curl, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides credential setup, required lyrics input, optional music settings, Replicate prediction polling, and generated audio download.]

## Skill Version(s):

1.0.10 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
