## Description:

Torii Image Translator helps an agent use an OOMOL-connected Torii account for image OCR, translation, inpainting, typesetting, and credit checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to extract text from public images, translate manga or comic images, remove masked text or objects, typeset translated text, and check connected Torii API credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes a remote shell installer for the oo CLI.

Mitigation: Review the setup path before installation and prefer trusted, documented release or package-manager instructions with verification.

Risk: Login and connection steps grant the skill access to an OOMOL-connected Torii Image Translator account.

Mitigation: Run authentication or connection steps only when intentionally enabling that account for this skill.

Risk: Some actions can alter outputs or consume connected service credits.

Mitigation: Inspect the live action schema, confirm write-action payloads with the user, and check credit status before retrying failed billing-related operations.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-torii-image-translator)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Torii Image Translator homepage](https://toriitranslate.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads or responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image actions may return downloadable PNG files through transit storage; connector responses include execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
