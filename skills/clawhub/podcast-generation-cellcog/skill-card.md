## Description:

AI podcast generation and production powered by CellCog, including multi-voice episodes, scripts, show notes, interview prep, audiograms, finished MP3 files, and chapter markers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, podcast teams, and agent users use this skill to plan, script, produce, document, and promote podcast episodes through CellCog.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Podcast prompts and source materials may be submitted to an external CellCog production service.

Mitigation: Do not submit secrets, regulated data, unpublished confidential plans, or sensitive guest information unless CellCog's privacy and retention terms are acceptable for the use case.

Risk: The skill requires CELLCOG_API_KEY for service access.

Mitigation: Store the API key in the agent environment or secret manager and avoid including it in prompts, scripts, logs, or generated podcast materials.

Risk: Generated scripts, show notes, audiograms, and audio may include factual, attribution, or brand-safety issues before publication.

Mitigation: Review and edit generated materials before publishing, especially guest facts, quotes, sponsorship language, and claims made in final audio.

## Reference(s):

- [CellCog Homepage](https://cellcog.ai)
- [ClawHub Skill Page](https://clawhub.ai/cellcog/skills/podcast-generation-cellcog)
- [CellCog Publisher Profile](https://clawhub.ai/user/cellcog)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance, files]

**Output Format:** [Markdown guidance with Python examples and generated podcast artifacts such as scripts, show notes, MP3 files, and chapter JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and CELLCOG_API_KEY; full audio production depends on the external CellCog service.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
