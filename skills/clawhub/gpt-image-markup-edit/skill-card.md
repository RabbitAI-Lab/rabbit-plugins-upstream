## Description:

Guides agents through marked-up image edits with GPT Image 2.6 on varg, including annotation creation, prompt writing, and result checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to direct edits to specific image regions with color-coded markup, generate the edit, and check whether unintended areas changed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images, annotations, and prompts are sent to varg and its processing providers.

Mitigation: Use content you are authorized to upload and review the providers’ privacy terms.

Risk: Image edits consume credits and may change pixels outside marked areas.

Mitigation: Check the cost before editing and use the provided diff check to inspect the result.

Risk: Full-collection installs or unreviewed installer versions and repository revisions can add unreviewed behavior.

Mitigation: Install only this skill unless you need the full collection, and prefer reviewed installer versions and repository revisions.

## Reference(s):

- [OpenAI image generation guide](https://developers.openai.com/api/docs/guides/image-generation)
- [varg how-to](https://varg.ai/how-to)
- [ClawHub skill release](https://clawhub.ai/vargai/skills/gpt-image-markup-edit)

## Skill Output:

**Output Type(s):** [PNG images, JSON, Prompt text, Shell commands, Guidance]

**Output Format:** [Transparent PNG annotations and previews, edited images, JSON shape specifications, and natural-language edit prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image edits are model-guided; a diff check is provided to review changes outside marked areas.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
