## Description:

Write or revise MiniMax H3 Ref2VA prompts for editing a source video from reference images or audio, especially masked or false-colour person replacement, face replacement, costume or object replacement, cross-shot identity persistence, overlay cleanup, and lip-sync preservation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangminrui2022](https://clawhub.ai/user/wangminrui2022)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, prompt engineers, and video workflow operators use this skill to draft structured MiniMax H3 Ref2VA editing prompts for masked-region, face, costume, object, cross-shot identity, overlay cleanup, and lip-sync-sensitive edits. It helps assign responsibility between source video, mask, reference imagery, and audio before producing the six-field H3 prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated prompts can overstate what prompt wording alone can guarantee for spatial masks, untouched time ranges, cross-shot identity, or frame-accurate lip sync.

Mitigation: Inspect the actual media, choose the appropriate lip-sync branch, and use shot segmentation, splicing, or downstream lip-sync tools when exact timing or identity persistence is required.

Risk: The skill may default generated prompts to English even when the source media includes dialogue, lyrics, visible text, or user context in another language.

Mitigation: Review the prompt language before use and preserve dialogue, lyrics, and visible text in their original language as the skill directs.

Risk: Users may provide media and ask for saved output, which can create local files in the workspace.

Mitigation: Save generated prompt files only when explicitly requested and review workspace outputs before sharing or deployment.

## Reference(s):

- [Universal Replacement Template](references/universal-replacement-template.md)
- [Editing Recipes](references/editing-recipes.md)
- [ClawHub skill page](https://clawhub.ai/wangminrui2022/skills/h3-video-editing-prompt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [English text block with six named Ref2VA fields; analysis or markdown only when requested by the user.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets about 7000 characters and must not exceed 10000 characters; saves a copy only when the environment has a workspace and the user requests a file.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
