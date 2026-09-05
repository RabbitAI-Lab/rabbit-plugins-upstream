## Description:

Use when a MIDI file needs rendering as a piano roll image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flobo3](https://clawhub.ai/user/flobo3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, musicians, and agents assisting them use this skill to render MIDI files into vertical or horizontal piano-roll PNGs for reading, teaching, sharing, and inspecting song structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local Python scripts and third-party packages run on user-provided MIDI files.

Mitigation: Install only the disclosed mido and Pillow packages and run the scripts in a local environment appropriate for untrusted files.

Risk: The output path is user-controlled and can write a PNG wherever the running user has permission.

Mitigation: Review output paths before execution and direct generated images to an intended project or temporary directory.

Risk: Automatic key, chord, and track-selection heuristics can produce incorrect musical labels.

Mitigation: Review generated labels before publication and use the documented --mel, --acc, --start, and --bars options when auto-detection is unsuitable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flobo3/skills/midi-pianoroll-render)
- [Artifact skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated PNG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces vertical or horizontal piano-roll PNGs from local MIDI input files.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
