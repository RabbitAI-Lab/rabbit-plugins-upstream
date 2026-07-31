## Description: <br>
Tierlist Maker guides a user through creating a TierVibe tier list, including tiers, cards, markdown commentary, and a browser launcher for importing the board. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edison7009](https://clawhub.ai/user/edison7009) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to turn a ranking idea into a TierVibe board through a step-by-step interview. It helps collect items, choose tiers and styling, draft markdown card commentary, and hand off a launcher file that opens the completed import flow in the user's browser. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local launcher file can contain the generated tier-list payload, including user-provided text and image data. <br>
Mitigation: Avoid including sensitive private content unless it is intended to appear in the local file and potentially in a published TierVibe board. <br>
Risk: Local images may be embedded as base64 when file reading is available and may later be sent to TierVibe if the user publishes the board. <br>
Mitigation: Use only images the user intends to publish, and review the generated board before publishing. <br>
Risk: Untrusted or unstable image sources can produce broken cards or publishing friction. <br>
Mitigation: Prefer trusted image sources or local uploads the user controls, and treat external image URLs as placeholders when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edison7009/skills/tierlist-maker) <br>
- [TierVibe import page](https://tiervibe.com/t/import) <br>
- [TierVibe data schema](references/data-schema.md) <br>
- [Import flow](references/import-flow.md) <br>
- [Text and image cards](references/text-cards.md) <br>
- [Tier presets and colors](references/tier-config.md) <br>
- [Explanations markdown subset](references/explanations.md) <br>
- [Worked example: AI models tier list](examples/ai-models-tierlist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance plus TierVibe JSON-compatible board data and a local HTML launcher] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create a local launcher file containing the import payload; may include a markdown image manifest when local image placeholders are used.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
