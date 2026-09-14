## Description:

Use when someone wants a simple short clip from text or images -- quick B-roll, drafts, or start/end frame animation, not when the brief needs the highest quality or tight lip-sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide an agent through one simple Pruna p-video generation from text, image anchors, or audio-conditioned prompts. It is intended for quick drafts, basic B-roll, and short motion clips rather than best-quality, multi-scene, or tight lip-sync work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to install several remote PrunaAI skills through unpinned npx commands.

Mitigation: Review the referenced skills before use, pin trusted immutable versions where possible, and avoid automatic -y installs in controlled environments.

Risk: The workflow may upload user-provided media or audio to the Pruna API and requires PRUNA_API_KEY access.

Mitigation: Upload only intended assets, keep unrelated credentials out of the runtime environment, and confirm API-use expectations before generation.

## Reference(s):

- [ClawHub p-video skill page](https://clawhub.ai/pruna-ai/skills/p-video)
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with curl examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides a single p-video prediction; generated media is produced by the Pruna API.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
