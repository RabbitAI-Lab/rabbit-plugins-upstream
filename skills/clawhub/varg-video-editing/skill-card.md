## Description:

Routes editing tasks for existing footage to suitable services and gives guidance for reliable cuts, captions, reframing, dubbing, enhancement, quality checks, and handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors use this skill to choose a service for editing existing footage and plan a reliable workflow for cuts, captions, reframing, dubbing, enhancement, quality checks, or handoff to an editor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags an unpinned installation command.

Mitigation: Verify the installer source and pin installation to a trusted version or commit before use.

Risk: The guidance uses public URLs to share uploaded footage with hosted services.

Mitigation: Avoid putting sensitive footage at public URLs; confirm the external processing and access are authorized before sharing.

## Reference(s):

- [Service selection guide](references/services.md)
- [Agentic editing practices](references/practices.md)
- [FFmpeg documentation](https://ffmpeg.org/documentation.html)
- [Online editing services guide](https://skills.varg.ai/browse/skills/edit-services/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown recommendations and an edit plan, with example commands where relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory workflow; does not render a finished video by itself.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
