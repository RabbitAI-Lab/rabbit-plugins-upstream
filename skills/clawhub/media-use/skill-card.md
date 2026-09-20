## Description:

media-use helps agents resolve, generate, transform, caption, grade, and reuse media assets for HyperFrames projects through local scripts, HeyGen-enabled providers, and documented media workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to select, create, register, and adjust media assets for HyperFrames compositions, including background music, sound effects, images, icons, logos, voiceover, captions, transcription, color treatments, and cut or reframe operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call external provider CLIs and use existing HeyGen or Codex authentication.

Mitigation: Run setup checks first, confirm agent-initiated paid or metered calls, and use local-only provider options when network providers are not appropriate.

Risk: The skill keeps reusable media, prompts, preferences, recipes, and misses in project and cross-project media stores.

Mitigation: Avoid sensitive client work unless cross-project reuse is acceptable, and review project .media and personal ~/.media contents before sharing or committing assets.

Risk: Telemetry can be linked to a signed-in HeyGen account and records coarse usage by media type, source, and provider.

Mitigation: Set DO_NOT_TRACK=1 or HYPERFRAMES_NO_TELEMETRY=1 when telemetry should be disabled.

Risk: Recipe reuse and media operations can mutate project files such as frame.md or create derived media outputs.

Mitigation: Review recipe use and generated diffs before accepting changes in sensitive projects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/media-use)
- [HeyGen publisher profile](https://clawhub.ai/user/heygen-com)
- [Setup and providers](references/setup-providers.md)
- [Resolve and reuse workflow](references/resolve.md)
- [Media treatments](references/media-treatments.md)
- [Media operations](references/operations.md)
- [Audio workflow](references/audio.md)
- [Memory and recipes](references/memory.md)
- [Telemetry and privacy](references/meta.md)
- [HeyGen CLI documentation](https://developers.heygen.com/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON snippets, and generated or registered media-file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or reuse local media assets, ledger records, captions, transcripts, treatment JSON, and cached preferences or recipes.]

## Skill Version(s):

1.0.50 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
