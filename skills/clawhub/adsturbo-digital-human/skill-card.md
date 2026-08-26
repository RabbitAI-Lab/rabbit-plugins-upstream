## Description:

Turn a script into a talking avatar by choosing a platform digital human, cloning a custom avatar from a photo and voice sample, or lip-syncing a portrait to an audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent operators use this skill to generate digital-human voiceover videos, create reusable custom personas, or produce one-off lip-sync videos from authorized portrait and audio assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can clone or animate faces and voices, which may be misused without consent.

Mitigation: Use only portraits, voices, and scripts that the operator owns or has explicit permission to use.

Risk: Uploaded media and generated assets may be sent to AdsTurbo and exposed through public URLs.

Mitigation: Avoid sensitive personal media unless the operator has reviewed the provider's retention, deletion, and access terms.

Risk: Custom personas can persist after creation and may be difficult to distinguish from authorized assets later.

Mitigation: Track persona identifiers carefully and confirm deletion targets before using persona-delete.

Risk: Resubmitting timed-out asynchronous jobs may create duplicate work and charges.

Mitigation: Resume polling with the existing workspace_id instead of submitting the same request again.

## Reference(s):

- [Digital Human](references/digital_human.md)
- [Upload](references/upload.md)
- [Work Status](references/work.md)
- [AdsTurbo website](https://www.adsturbo.ai)
- [AdsTurbo API base URL](https://adsturbo.ai/klian/novartapi)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Text]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ADSTURBO_API_KEY; local portrait, audio, and video assets must be converted to public URLs before generation.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
