## Description:

Turns a browser game or three.js/WebGL scene into a frame-accurate trailer with directed shots, sound, an MP4 cut, and checks for common visual and audio issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to capture a browser game or WebGL scene as a directed, beat-synced trailer for sharing or promotion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports a filesystem containment weakness that could expose files in sibling directories.

Mitigation: Review the reported weakness and run the skill with access limited to the project files it needs.

Risk: The scan was partial: 11 of 17 components were fully inspected, and the install command is unpinned.

Mitigation: Review the remaining components and install a specific release version.

## Reference(s):

- [Director JSON format](references/director-format.md)
- [Virtual clock and frame-accurate capture](references/virtual-clock.md)
- [Sound, editing, and deliverables](references/sound-and-cut.md)
- [Example trailer](https://s3.varg.ai/files/4325c578-378d-4c43-ae53-3cc3218df1ea/file_b715771f882f.mp4)

## Skill Output:

**Output Type(s):** [Video files, Audio files, Configuration files, Shell commands]

**Output Format:** [MP4 video, WAV or MP3 audio, JSON director configuration, and captured image sequences]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 1920x1080 at 30 fps; 60 fps and other capture sizes can be configured.]

## Skill Version(s):

1.0.3 (source: server-resolved release version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
