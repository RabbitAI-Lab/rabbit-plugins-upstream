## Description:

Torii Image Translator lets agents use OOMOL's Torii connector to extract, translate, inpaint, and typeset text in public images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to automate Torii Image Translator workflows for OCR extraction, image translation, inpainting, and typesetting on public images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that execute downloaded scripts directly.

Mitigation: Install the oo CLI only from a verified official package or after manually inspecting and checksum-validating the installer.

Risk: Image translation, inpainting, and typesetting actions can modify image outputs or consume connected account credits.

Mitigation: Inspect the live action schema and confirm exact payloads with the user before running state-changing or credit-consuming actions.

## Reference(s):

- [Torii Image Translator homepage](https://toriitranslate.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-torii-image-translator)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions may return structured JSON, downloadable image outputs, PNG files through transit storage, or credit-balance data depending on the selected Torii action.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
