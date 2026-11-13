## Description:

Guides an agent to create a short animated film with a custom WebGL2 path tracer, procedural characters and scenes, a synthesized score, captions, and optional interactive browser page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users can use this skill to turn a story prompt into a short code-rendered film and its supporting assets, or adapt the included The Smallest Star example.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security guidance reports that an unauthenticated rendering endpoint may expose file writes and job controls to reachable attackers.

Mitigation: Review the endpoint before use, restrict network access, and check its file-write behavior and output paths.

Risk: The documented install command is unpinned, so it may retrieve a different release over time.

Mitigation: Review the package source and pin a trusted version when installing.

Risk: Optional narration captions may be sent to a third-party service.

Mitigation: Review the service and captions before sending them, and omit sensitive text.

## Reference(s):

- [Commands and render workflows](artifact/references/commands.md)
- [Night look guide](artifact/references/look.md)
- [Score brief](artifact/references/score-brief.md)
- [ClawHub skill page](https://clawhub.ai/vargai/skills/code-path-traced-film)
- [The Smallest Star sample film](https://s3.varg.ai/files/194b94d0-58ff-4e8b-91de-4f1959d04013/file_8d3b65611ed8.mp4)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands]

**Output Format:** [Source code and commands, rendered MP4 film, PNG frames, audio, and a standalone HTML page]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deliverables and render time vary with requested story, film length, resolution, and whether the live page is included.]

## Skill Version(s):

1.0.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
