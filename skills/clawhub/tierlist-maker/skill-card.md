## Description: <br>
Builds a TierVibe tier list through a step-by-step interview, drafts text or image cards with markdown commentary, and opens the completed import URL in the user's browser. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edison7009](https://clawhub.ai/user/edison7009) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to create TierVibe ranking boards through a guided interview. It is suited for producing tier lists with configured tiers, text or image cards, markdown explanations, and a browser-ready import flow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TierVibe opens in the user's system browser, which can expose activity through browser history, screenshots, shared links, or login state. <br>
Mitigation: Install and use only if that browser behavior is acceptable, avoid private or embarrassing tier-list content, and review the imported board before publishing. <br>
Risk: Private, signed, or unstable image URLs can leak information, expire, break cards, or create publish-time image issues. <br>
Mitigation: Use user-approved public HTTPS image URLs, avoid private or signed links, and swap images in the TierVibe editor when a local or platform-hosted asset is safer. <br>
Risk: The skill can generate a completed board quickly, but rankings and commentary may still be inaccurate or unwanted. <br>
Mitigation: Treat the imported board as a draft and require the user to inspect tiers, cards, and commentary before clicking Publish. <br>


## Reference(s): <br>
- [TierVibe import page](https://tiervibe.com/t/import) <br>
- [ClawHub skill page](https://clawhub.ai/edison7009/skills/tierlist-maker) <br>
- [TierVibe authoring schema](artifact/references/data-schema.md) <br>
- [Import flow](artifact/references/import-flow.md) <br>
- [Text and image cards](artifact/references/text-cards.md) <br>
- [Tier presets and colors](artifact/references/tier-config.md) <br>
- [Card explanations markdown subset](artifact/references/explanations.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [TierVibe JSON encoded into an import URL, with Markdown card commentary and concise browser-opening instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May open the user's default browser and may include user-provided public image URLs; users review and publish the board in TierVibe.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata; bundled SKILL.md frontmatter reports 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
