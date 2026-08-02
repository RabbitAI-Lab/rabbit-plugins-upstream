## Description: <br>
Builds TierVibe tier lists through a guided interview, producing text or image cards, markdown explanations, tier styling, and a browser import handoff. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edison7009](https://clawhub.ai/user/edison7009) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to create TierVibe ranking boards from a conversational workflow. It helps collect the topic, tiers, items, placements, card styling, optional image inputs, and per-card commentary before handing the board to the TierVibe import page. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated handoff files may contain tier-list text and, for local image workflows, embedded image data. <br>
Mitigation: Review generated files before sharing and delete launcher.html, manifest.md, or .tiervibe.json files when they are no longer needed. <br>
Risk: Opening a generated import handoff sends the board payload to the TierVibe import page. <br>
Mitigation: Prefer opening the generated launcher manually and review the board in the browser before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edison7009/skills/tierlist-maker) <br>
- [TierVibe import page](https://tiervibe.com/t/import) <br>
- [Data schema](references/data-schema.md) <br>
- [Import flow](references/import-flow.md) <br>
- [Text and image cards](references/text-cards.md) <br>
- [Explanations](references/explanations.md) <br>
- [Tier presets and colors](references/tier-config.md) <br>
- [Worked example](examples/ai-models-tierlist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-compatible TierVibe board data and local handoff files such as launcher.html, manifest.md, or .tiervibe.json when needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can include TierVibe import configuration, markdown card details, and local files containing board text or embedded image data.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
