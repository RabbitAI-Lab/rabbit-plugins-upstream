## Description:

Media Use helps agents resolve, generate, operate on, and reuse HyperFrames media assets such as BGM, SFX, images, icons, logos, voiceover, captions, color grades, LUTs, cuts, and transformations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media-producing agents use this skill to resolve, generate, operate on, and reuse project media assets such as music, sound effects, images, icons, logos, voiceover, captions, color grades, LUTs, cuts, and transformations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call external provider CLIs/APIs and read configured provider credentials.

Mitigation: Review credential placement, prefer explicit provider credentials, and use local-only provider paths when external calls are not acceptable.

Risk: The skill can persist media, preferences, and reusable memory across projects.

Mitigation: Review cache and memory locations before use with sensitive media, and clear or isolate project caches when needed.

Risk: The skill can install or run sizeable local Python and model dependencies.

Mitigation: Review dependency installation steps and run them in isolated environments appropriate for the host.

Risk: The skill can send coarse usage telemetry unless opted out.

Mitigation: Set DO_NOT_TRACK=1 or HYPERFRAMES_NO_TELEMETRY=1 when telemetry is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/media-use)
- [Setup and providers](artifact/references/setup-providers.md)
- [Resolve command, flags, reuse, adopt, inventory](artifact/references/resolve.md)
- [Audio engine](artifact/references/audio.md)
- [Media operations](artifact/references/operations.md)
- [Media treatments](artifact/references/media-treatments.md)
- [Color grading and LUTs](artifact/references/grading.md)
- [User memory](artifact/references/memory.md)
- [Ownership, telemetry, and privacy](artifact/references/meta.md)
- [HeyGen CLI release instructions](https://developers.heygen.com/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, file paths, and local media asset outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce frozen local media files, paste-ready blocks, and ledger records for resolved assets.]

## Skill Version(s):

1.0.55 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
