## Description:

Creates structured GPT Image 2 poster briefs and AI Hive image-generation commands for activity, launch, promotion, hiring, exhibition, conference, and bilingual poster layouts with reviewable text fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and developers use this skill to prepare poster information hierarchy, generate GPT Image 2 poster backgrounds, and preserve fields for later copy review. It is suited to event, product launch, promotion, recruiting, exhibition, conference, and Chinese-English bilingual poster workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper requires an AI Hive API key and sends prompts and selected reference files to AI Hive.

Mitigation: Install only when that data flow is acceptable, avoid sensitive reference media, and protect the API key through CLI, environment, or a restricted local config file.

Risk: Generated poster text or factual event details may be incorrect if exact copy is delegated to the image model.

Mitigation: Use approved source data for titles, dates, venues, prices, QR codes, sponsors, and legal text; generate text-free backgrounds when exact copy cannot be guaranteed.

Risk: The bundled helper contains broader AI Hive client functions than the active poster examples use.

Mitigation: Review the helper before deployment and keep routine use to the poster-focused generate, task, upload, and init commands described by the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-poster)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands, JSON task responses, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key; generated outputs default to ~/Downloads/AiHive unless an output directory is provided.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
