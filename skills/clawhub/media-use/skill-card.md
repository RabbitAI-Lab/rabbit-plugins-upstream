## Description: <br>
Agent Media OS for HyperFrames projects that helps agents resolve, generate, operate on, and reuse media assets including background music, sound effects, images, icons, logos, voices, grades, LUTs, captions, transcription, and background removal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative agents use this skill to select, generate, transform, freeze, and reuse media assets for HyperFrames projects. It is suited to workflows that need local media ledgers, provider-aware media resolution, audio processing, captions, transcription, color treatments, and reusable project or cross-project assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can contact cloud media providers, CDNs, model registries, package registries, and service APIs. <br>
Mitigation: Review provider choices before sending private media to cloud services, and use --local-only for sensitive work when local providers and cached assets are sufficient. <br>
Risk: Usage telemetry may be linked to a HeyGen email or account identity. <br>
Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1 when telemetry should be disabled. <br>
Risk: The skill uses local credential or profile files and stores reusable media state under ~/.media. <br>
Mitigation: Inspect local credential, profile, and media-cache locations before shared or regulated use, and clear or isolate reusable state when switching projects or clients. <br>
Risk: Some workflows can auto-install dependencies or use model and package registries. <br>
Mitigation: Run in a controlled environment, review dependency sources, and pin or preinstall approved tools for production workflows. <br>
Risk: Media adoption and recipe workflows can alter project media assumptions. <br>
Mitigation: Back up frame.md and review generated ledgers, recipes, and asset selections before adopting them into an existing project. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/media-use) <br>
- [Setup and providers](artifact/references/setup-providers.md) <br>
- [Resolve](artifact/references/resolve.md) <br>
- [Audio](artifact/references/audio.md) <br>
- [Operations](artifact/references/operations.md) <br>
- [Media treatments](artifact/references/media-treatments.md) <br>
- [HeyGen CLI documentation](https://developers.heygen.com/cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON snippets, file paths, and reusable media ledger entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or reference local media files, frozen assets, captions, transcripts, color-treatment JSON, LUT files, and reusable project or global media state.] <br>

## Skill Version(s): <br>
1.0.34 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
