## Description:

Guides an agent to mark specific regions of an image, prepare transparent markup or masks, and request GPT Image 2.6 edits through varg while checking the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Developers and image creators use this skill to request targeted changes to selected parts of an image, prepare per-color markup prompts, and inspect the result for unintended changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented install command uses an unpinned package version.

Mitigation: Review the package source and select a specific release version before installing.

Risk: Image content, annotations, and prompts may be sent to external services during editing.

Mitigation: Review what will be uploaded and avoid submitting sensitive material unless you are comfortable sharing it.

Risk: The security review was partial because a local reference could not be matched to a bundled artifact.

Mitigation: Resolve and review the referenced material before relying on guidance that depends on it.

## Reference(s):

- [OpenAI image generation guide](https://developers.openai.com/api/docs/guides/image-generation)
- [varg how-to guide for this skill](https://varg.ai/how-to/skills/gpt-image-markup-edit)
- [ClawHub skill release](https://clawhub.ai/vargai/skills/gpt-image-markup-edit)

## Skill Output:

**Output Type(s):** [Edited images, PNG markup and mask files, JSON shape specifications, Shell commands, Guidance]

**Output Format:** [Image files, JSON, and Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Markup and mask images match the source image dimensions; the skill includes a preview and optional image-difference check.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
