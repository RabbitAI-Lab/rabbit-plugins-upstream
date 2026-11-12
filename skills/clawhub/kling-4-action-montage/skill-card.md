## Description:

Guides an agent to create a Kling 4 action montage from three or four key frames, with prompting and clip-selection guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to plan and generate a short action, dance, trick, or chase montage from reference stills, then select and trim usable moments from the generated take.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference-image URLs may be sent to VARG and other generation providers.

Mitigation: Avoid sensitive images or private references unless you are comfortable sharing them; review the providers' privacy implications before use.

Risk: The installation example uses an unpinned CLI package.

Mitigation: Verify the CLI package and pin its version before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/kling-4-action-montage)
- [VARG how-to](https://varg.ai/how-to)
- [Kling 4 Halloween film example](https://www.youtube.com/watch?v=WzXKggH-0Io)
- [Test montage example](https://s3.varg.ai/files/72c55813-c0fa-4cf2-9f64-ec4f7ed0e7ae/file_0665c41e46ff.mp4)

## Skill Output:

**Output Type(s):** [Video, Shell commands, Guidance]

**Output Format:** [Generated video file with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A generated take is typically cut into selected short clips; some generated moments may be unusable.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
