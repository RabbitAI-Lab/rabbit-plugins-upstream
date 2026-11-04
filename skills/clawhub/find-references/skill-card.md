## Description:

Finds and evaluates human-made visual and audio references to guide AI-generated or code-made creative work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Developers, designers, and creative teams use it to research and shortlist verified visual and audio references before making AI-generated or code-made image, video, and music projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional Discogs container setup could expose unrelated project secrets to a third-party container.

Mitigation: Use the built-in keyless search path; skip that setup command, or use only service-specific secrets with a reviewed, digest-pinned image.

Risk: External searches or judging may receive confidential brief details or private images.

Mitigation: Keep confidential material out of provider requests unless use with those providers is approved.

Risk: Media processing can consume local resources and create files in the project area.

Mitigation: Use a separate output folder and constrain media-processing resources.

## Reference(s):

- [ClawHub release](https://clawhub.ai/vargai/skills/find-references)
- [Project homepage](https://github.com/vargHQ/skills/tree/main/find-references)

## Skill Output:

**Output Type(s):** [Markdown, JSON, HTML, Analysis]

**Output Format:** [Markdown reference boards and notes, JSON search data, and an HTML candidate board]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source links, provenance notes, measurements, and provisional recommendations for a person to review.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
