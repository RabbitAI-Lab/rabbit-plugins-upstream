## Description:

Analyzes a finished video’s editing pace, loudness, narrative structure, and audio roles to produce a reusable production reference without source-specific names or dialogue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Video editors and production teams use this on demand to turn a finished video into measured, reusable guidance for a future production, while keeping source-specific observations local.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local breakdowns and frame sheets can expose source-video facts and imagery.

Mitigation: Keep the working directory local and review the exported production_reference.json before sharing it.

Risk: Automatic cut detection and coarse audio timing may miss edits or misstate pacing.

Mitigation: Review candidate cuts against the frame sheets and check agent labels before reusing the reference.

## Reference(s):

- [Video Reference skill release](https://clawhub.ai/worldwonderer/skills/video-reference)
- [Production reference schema and examples](references/reference-schema.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files]

**Output Format:** [JSON (production_reference.json)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reusable methods and measured video metrics; source-specific facts and frame sheets remain local.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
