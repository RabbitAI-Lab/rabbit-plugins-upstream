## Description:

Cat Sticker analyzes message emotion and automatically matches a sticker from custom_stickers.json, with controls for trigger probability, enablement, and cooldown.

This skill is for research and development only.

## Publisher:

[efgyuhhgy](https://clawhub.ai/user/efgyuhhgy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to add offline, emotion-triggered sticker responses to chat agents. It maps user text to configured sticker assets and returns response metadata for the host agent to render.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic sticker insertion can trigger on ordinary chat text and may be inappropriate in sensitive conversations.

Mitigation: Lower the sticker probability, increase cooldown, or disable automatic sticker use for sensitive contexts.

Risk: Returned media metadata may expose local install paths.

Mitigation: Keep path exposure disabled where possible and avoid sharing raw result objects with users or external systems.

Risk: Bundled sticker images are documented as collected from public internet sources for personal learning and research use.

Mitigation: Review image rights before broader deployment or replace bundled images with approved assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/efgyuhhgy/skills/cat-sticker)
- [Publisher profile](https://clawhub.ai/user/efgyuhhgy)
- [Skill documentation](artifact/SKILL.md)
- [Core Python module](artifact/cat_sticker_skill.py)
- [Sticker metadata](artifact/custom_stickers.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, File references]

**Output Format:** [Python dictionary with text fields and optional Markdown image or media references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotion labels, confidence values, cooldown status, and local sticker file paths.]

## Skill Version(s):

2.1.0 (source: server release metadata; artifact openclaw metadata says 2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
