## Description:

Helps agents decide when to prototype a video shot, build measured 3D previs scenes, check frames, and prepare handoffs to video models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Developers, filmmakers, and video creators use it to decide whether a prototype will help, block shots in Three.js or Blender, and prepare checked previews or storyboards for video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private files beside a scene may be exposed during use.

Mitigation: Work in a directory containing only project files approved for the workflow.

Risk: Reference media and judging materials may be sent to external services.

Mitigation: Use only media approved for external processing and check the destination service before sending it.

Risk: The security review is incomplete, with two files only partially inspected.

Mitigation: Review those files and verify the installer version before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/vargai/skills/code-to-video-previz)
- [Scene staging format](references/staging-format.md)
- [Blender setup and workflow](references/blender.md)
- [Video model handoff guidance](references/handoff.md)
- [Reference video workflow](references/reference-video.md)

## Skill Output:

**Output Type(s):** [Configuration, Code, Shell commands, Guidance]

**Output Format:** [Staging JSON, JavaScript or Python code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include rendered stills, storyboards, or guide clips; a person should assess pacing and visual quality.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
