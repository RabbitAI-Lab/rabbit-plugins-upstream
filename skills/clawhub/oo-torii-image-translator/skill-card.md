## Description:

Torii Image Translator helps agents use the OOMOL oo CLI connector for OCR, public-image translation, inpainting, typesetting, and credit checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Torii Image Translator account from an agent, including extracting text from public images, translating and typesetting image text, inpainting images, and checking remaining credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs or payloads may be sent to Torii/OOMOL services.

Mitigation: Use the skill only with images and payloads appropriate for the connected Torii/OOMOL account and confirm sensitive data handling before execution.

Risk: Some actions can consume credits or create modified images.

Mitigation: Confirm the intended action, payload, and expected effect with the user before running credit-consuming or image-modifying actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-torii-image-translator)
- [Torii Image Translator homepage](https://toriitranslate.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector runs are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: artifact metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
