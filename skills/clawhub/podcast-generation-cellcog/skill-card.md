## Description:

AI podcast generation and production powered by CellCog, producing episode scripts, show notes, interview prep, audiograms, and full multi-voice podcast episodes with music, mastering, MP3 output, and chapter markers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, podcast teams, and developers use this skill to ask an agent to plan, script, prepare, produce, document, and promote podcast episodes through CellCog.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Podcast prompts, guest details, scripts, and show branding information may be sent to CellCog when the skill uses CELLCOG_API_KEY.

Mitigation: Review data handling requirements before use and avoid sending confidential or regulated material unless the CellCog service is approved for that data.

Risk: The artifact is a guide and does not include the underlying CellCog SDK implementation.

Mitigation: Verify CellCog dependency installation, setup materials, and API key configuration before relying on the skill in a production workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cellcog/skills/podcast-generation-cellcog)
- [CellCog homepage](https://cellcog.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with Python snippets and generated podcast assets such as MP3 audio and JSON chapter markers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, the cellcog dependency, and CELLCOG_API_KEY; uses the CellCog external service for content and audio generation.]

## Skill Version(s):

1.0.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
