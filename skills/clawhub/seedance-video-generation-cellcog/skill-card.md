## Description:

AI video generation powered by CellCog via Seedance 2.5. Complete multi-minute videos from a single prompt: scripting, voice synthesis, lipsync, scoring, editing, with locked character consistency via 50 reference files. Full productions, not just clips, via ByteDance's Seedance model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to ask an agent to create marketing videos, explainers, cinematic content, and spokesperson videos through CellCog's Seedance video-generation workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video prompts and attached image, video, or audio references are sent to CellCog and its model providers.

Mitigation: Use only with material approved for external processing, and avoid confidential, regulated, or copyrighted internal content unless organizational policy and CellCog's terms allow it.

## Reference(s):

- [CellCog homepage](https://cellcog.ai)
- [ClawHub skill page](https://clawhub.ai/cellcog/skills/seedance-video-generation-cellcog)
- [CellCog publisher profile](https://clawhub.ai/user/cellcog)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, text, files]

**Output Format:** [Markdown guidance with Python code blocks and shell commands; generated video assets are returned by the CellCog service, typically as MP4 output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, the cellcog dependency, and CELLCOG_API_KEY. Recommended video-generation settings are chat_mode="agent" and chat_tier="max".]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
