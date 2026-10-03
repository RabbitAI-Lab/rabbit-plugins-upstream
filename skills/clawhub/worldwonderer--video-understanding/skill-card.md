## Description:

Analyzes videos into scene, speech, visual, silence, and timeline indexes plus a briefing for downstream agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Developers and content creators use this skill to understand and index source video before summarization or creative planning. It produces evidence-linked scene observations and a briefing rather than narration or narration scores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source media, extracted audio and images, transcripts, and context may be sent to external model endpoints.

Mitigation: Use only approved providers and avoid confidential media unless provider and environment are approved.

Risk: Configurable external endpoints can receive an API key as well as media and transcripts.

Mitigation: Leave endpoint overrides unset or configure only trusted provider URLs, and use a dedicated work directory.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/video-understanding)
- [Output data schema](references/data-schema.md)
- [Background research guide](references/research-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Timestamped JSON analysis and Markdown briefing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scene descriptions, coarse speech windows, silence intervals, fused timeline, and optional visual storyboards; does not generate narration.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
