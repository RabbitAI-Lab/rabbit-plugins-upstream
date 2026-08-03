## Description: <br>
Media-use helps agents resolve, generate, transform, caption, grade, and reuse media assets for HyperFrames projects through documented commands and provider workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents building HyperFrames media projects use this skill to find, generate, edit, and reuse media such as background music, sound effects, images, icons, logos, voiceover, captions, color grades, LUTs, and transformed clips. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can contact cloud media providers through existing signed-in accounts. <br>
Mitigation: Use --local-only for sensitive media and install the skill only where cloud-provider access is acceptable. <br>
Risk: Telemetry may send account-linked usage events. <br>
Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 before use when telemetry is not wanted. <br>
Risk: Persistent project and global media memory can retain reusable media data across projects. <br>
Mitigation: Review project .media files and ~/.media before sharing, committing, or reusing a project. <br>
Risk: Optional local generation tools may be installed or run by workflows. <br>
Mitigation: Review provider setup and local generator requirements before enabling optional generators. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/media-use) <br>
- [Resolve workflow](artifact/references/resolve.md) <br>
- [Setup and providers](artifact/references/setup-providers.md) <br>
- [Audio workflow](artifact/references/audio.md) <br>
- [Media treatments](artifact/references/media-treatments.md) <br>
- [Media operations](artifact/references/operations.md) <br>
- [User memory](artifact/references/memory.md) <br>
- [Ownership, telemetry, and privacy](artifact/references/meta.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with inline shell commands, JSON snippets, and local file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or reference persistent project .media files and global ~/.media cache entries when the user runs the documented commands.] <br>

## Skill Version(s): <br>
1.0.36 (source: server release evidence, created 2026-07-29T22:27:58Z) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
