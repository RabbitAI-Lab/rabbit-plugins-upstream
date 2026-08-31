## Description:

Ecommerce livestream avatar and AI spokesperson guidance for product selling videos, including base portrait recipes and a script to TTS to avatar to B-roll workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, content teams, and developers use this skill to plan reusable AI spokesperson videos for product selling workflows, from base portrait selection through scripting, TTS, avatar driving, B-roll, and assembly guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses the third-party dLazy CLI and sends product media, prompts, and generated assets to dLazy service endpoints.

Mitigation: Install only a trusted dLazy CLI package, review the command payloads before execution, and avoid sending confidential product media unless approved.

Risk: The skill uses an API key stored in ~/.dlazy/config.json or supplied through DLAZY_API_KEY.

Mitigation: Protect the API key, avoid committing local config files, and rotate the key if it is exposed.

Risk: Media-generation requests can consume paid credits, especially avatar driving and repeated retries.

Mitigation: Use dry-run checks where supported, segment scripts before generation, and monitor credit usage before running batches.

Risk: Generated ecommerce avatar videos can create misleading advertising claims or require platform disclosure as AI-generated content.

Mitigation: Review scripts and visuals for prohibited claims, false credentials, and platform-specific AI disclosure requirements before publishing.

Risk: Avatar quality depends on base portrait constraints, model availability, and compatible media formats.

Mitigation: Check portrait driveability before costly generation, keep fallback paths for avatar model outages, and re-encode mixed video assets before final assembly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [dLazy homepage](https://dlazy.com)
- [Skill overview](artifact/SKILL.md)
- [Base portrait recipes](artifact/recipes.md)
- [Product-to-video pipeline](artifact/pipeline.md)
- [Troubleshooting and cost controls](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces procedural recommendations and command templates for external CLI and media-generation services; generated media is produced by those services, not by the skill text itself.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
