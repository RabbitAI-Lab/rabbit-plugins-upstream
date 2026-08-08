## Description:

Guides an agent through producing vertical short videos that artistically reconstruct historical figures using source research, AI imagery, narration, music, title cards, ffmpeg composition, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chugenice](https://clawhub.ai/user/chugenice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to plan and assemble short-form historical-persona videos with a repeatable workflow for material research, AI media generation, narration, soundtrack mixing, card design, video assembly, and final QA.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled RunningHub client grants broader media-generation authority than the historical-video workflow needs, including unrelated paid AI-app and media operations with local file and API-key access.

Mitigation: Install only when that authority is intended, use a self-owned RunningHub API key, expect paid account usage, avoid sensitive local media, and prefer a scoped version that removes unused endpoints.

Risk: Historical reconstructions can be mistaken for factual photographs or definitive likenesses.

Mitigation: Keep the workflow's required disclaimer that outputs are artistic AI visual reconstructions based on historical sources and clothing cues, not real photographs.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/chugenice/history-persona-video)
- [ClawHub skill page](https://clawhub.ai/chugenice/skills/history-persona-video)
- [history-persona-video README](artifact/README.md)
- [history-persona-video skill definition](artifact/SKILL.md)
- [RunningHub API key setup](artifact/skills/runninghub/references/api-key-setup.md)
- [RunningHub image model selection](artifact/skills/runninghub/references/image-models.md)
- [RunningHub video model selection](artifact/skills/runninghub/references/video-models.md)
- [RunningHub output delivery](artifact/skills/runninghub/references/output-delivery.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with command examples and local media artifacts when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected final artifact is a 1080x1920 MP4 under media/<person>/ with duration, resolution, voice, font, cost details, and an artistic-reconstruction disclaimer.]

## Skill Version(s):

0.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
