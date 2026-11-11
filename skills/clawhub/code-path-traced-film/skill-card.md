## Description:

Create a short animated film with a custom WebGL2 path tracer, procedural scenes and characters, a synthesized score, captions, and an encoded video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative coding agents use this skill to plan and produce short animated films from a story brief, including the renderer, scene, soundtrack, captions, and final video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious and reports an unauthenticated rendering endpoint that may overwrite files outside its output folder, alongside other security and privacy concerns.

Mitigation: Review the endpoint’s file-writing and access controls, and constrain its filesystem permissions and output location before use.

Risk: The security review is partial: 15 of 20 components were fully inspected and five were partially inspected.

Mitigation: Review the remaining components and complete the scan before installing or running the skill.

Risk: The security guidance calls out installer package pinning and whether narration sends private text to an external service.

Mitigation: Check and pin installer packages, and confirm the narration provider’s data handling before sending private text.

## Reference(s):

- [Skill page on ClawHub](https://clawhub.ai/vargai/skills/code-path-traced-film)
- [The Smallest Star starter film](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_8d3b65611ed8.mp4)
- [Skill guide on varg.ai](https://varg.ai/how-to/skills/code-path-traced-film)
- [Commands reference](artifact/references/commands.md)
- [Night look reference](artifact/references/look.md)
- [Score brief](artifact/references/score-brief.md)
- [Starter film source overview](artifact/scripts/smallest-star/README.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Files]

**Output Format:** [Source code and rendered media files, including PNG frames, an MP4 film, audio, and a standalone HTML live page.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the requested delivery; the starter workflow can produce a film, a live page, or both.]

## Skill Version(s):

1.0.0 (source: release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
