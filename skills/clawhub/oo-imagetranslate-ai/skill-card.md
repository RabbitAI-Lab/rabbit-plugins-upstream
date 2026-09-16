## Description:

ImageTranslate.AI helps an agent translate text in public images through the ImageTranslate.AI connector while preserving the selected layout style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate text in public images with ImageTranslate.AI through an OOMOL-connected account, including checking action schemas and running the translate_image action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External image processing may expose confidential, regulated, or otherwise sensitive image content to ImageTranslate.AI.

Mitigation: Use the skill only for deliberate image-translation requests and avoid confidential or regulated images unless the external service terms are acceptable.

Risk: Setup guidance includes remote installer commands for the OOMOL CLI.

Mitigation: Do not run remote installer commands unless the OOMOL CLI installation path has been independently trusted and verified.

Risk: The translate_image action is an external, potentially billable action.

Mitigation: Confirm the user's intent and payload before running translate_image, especially when billing, file size, or external processing could matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-imagetranslate-ai)
- [ImageTranslate.AI homepage](https://imagetranslate.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The translate_image action may return rendered PNG results up to 50 MB through transit storage.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
