## Description:

Creates color-coded transparent markup layers and prompts to guide localized image edits with GPT Image 2.6 on varg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and image editors use this skill to specify localized changes to an image with colored marks and prompts, then review the result or use a mask for tighter regions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts may be sent to external services, including image areas outside the marked region.

Mitigation: Avoid sensitive images or prompts unless you are comfortable sharing them with those services.

Risk: The installer and source are unpinned, and scan coverage is partial because a referenced path could not be resolved.

Mitigation: Review the installer and resolved source before use, and scan the complete files you install.

## Reference(s):

- [OpenAI image generation guide](https://developers.openai.com/api/docs/guides/image-generation)
- [varg skill page](https://clawhub.ai/vargai/skills/gpt-image-markup-edit)
- [varg how-to](https://varg.ai/how-to)

## Skill Output:

**Output Type(s):** [Files, JSON, Text, API Calls, Shell commands]

**Output Format:** [JSON shape specifications, prompt text, shell commands, and PNG markup, preview, or mask images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A transparent markup PNG matches the source image dimensions; an optional black-and-white mask can also be produced.]

## Skill Version(s):

1.0.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
