## Description: <br>
Builds TierVibe tier lists through a step-by-step interview, producing text or image-card boards with markdown commentary and opening the completed board in the user's default browser. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edison7009](https://clawhub.ai/user/edison7009) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creators use this skill to plan a tier-list topic, choose tiers, assign items, draft card commentary, and open a TierVibe import URL for final editing and publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill opens tiervibe.com in the user's default browser and places tier-list content in the URL fragment for the editor to load. <br>
Mitigation: Use the skill only when this browser handoff is acceptable, and review the loaded board before publishing. <br>
Risk: Third-party image hosts may see viewer metadata when image cards load. <br>
Mitigation: Prefer text cards or trusted public image URLs, and replace placeholder images in the editor when needed. <br>
Risk: The generated board may not match the user's intended rankings, colors, or commentary on the first pass. <br>
Mitigation: Inspect and edit the board in TierVibe before clicking Publish. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edison7009/skills/tierlist-maker) <br>
- [Server-resolved GitHub provenance](https://github.com/edison7009/TierList-Maker/tree/main/plugins/tierlist-maker/skills/tierlist-maker) <br>
- [TierVibe import page](https://tiervibe.com/t/import) <br>
- [.tiervibe.json authoring format](references/data-schema.md) <br>
- [Import flow](references/import-flow.md) <br>
- [Text and image cards](references/text-cards.md) <br>
- [Tier presets and colors](references/tier-config.md) <br>
- [Markdown explanations](references/explanations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance plus TierVibe JSON encoded into an import URL and an OS browser-open command.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Opens https://tiervibe.com/t/import#data=... in the user's default browser; no server calls or login prompts occur until the final browser handoff.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
