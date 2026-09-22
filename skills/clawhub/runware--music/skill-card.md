## Description:

Generate music from a text description, including vocal songs, instrumental beds, jingles, intros, background tracks, and cover or restyle variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runware](https://clawhub.ai/user/runware)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide an agent through music-generation requests, including model selection, style and lyric collection, JSON request construction, asynchronous polling, and audio result review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes music-creation requests to external audio-generation providers, and cover or restyle workflows can send source audio to the provider.

Mitigation: Use the skill only when external provider processing is acceptable, and avoid submitting sensitive or unlicensed source audio.

Risk: Prompts or source material could request imitation of identifiable artists or use copyrighted material without rights.

Mitigation: Describe genres and production traits rather than named performers or songs, and use original lyrics or material the user has rights to use.

## Reference(s):

- [Music worked recipes](references/examples.md)
- [Music on ClawHub](https://clawhub.ai/runware/skills/music)

## Skill Output:

**Output Type(s):** [guidance, json, configuration]

**Output Format:** [Markdown guidance with JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides asynchronous audio-generation workflows that return task identifiers, audio UUIDs, and audio URLs.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
