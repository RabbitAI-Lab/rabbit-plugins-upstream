## Description:

AI video generation powered by CellCog via Seedance 2.5. Complete multi-minute videos from a single prompt: scripting, voice synthesis, lipsync, scoring, editing, with locked character consistency via 50 reference files. Full productions, not just clips, via ByteDance's Seedance model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and marketing teams use this skill to ask an agent to generate CellCog video productions from prompts, including marketing, explainer, cinematic, and spokesperson videos. It provides guidance and invocation examples for sending video-generation requests through the CellCog client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached images, videos, or audio are sent to CellCog and underlying providers for generation.

Mitigation: Use only material you are authorized to send, and avoid confidential, regulated, or rights-restricted content unless approved for that service path.

Risk: Generated videos can be large and may involve provider-side output handling or storage.

Mitigation: Check CellCog output locations, retention, and storage behavior before using the skill for production or sensitive work.

## Reference(s):

- [Seedance Video Generation on ClawHub](https://clawhub.ai/cellcog/skills/seedance-video-generation-cellcog)
- [CellCog](https://cellcog.ai)
- [CellCog Publisher Profile](https://clawhub.ai/user/cellcog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls, files]

**Output Format:** [Markdown guidance with Python code snippets, shell commands, configuration requirements, and generated MP4 video outputs through CellCog]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and CELLCOG_API_KEY; video requests may use prompt text and optional image, video, or audio references.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
