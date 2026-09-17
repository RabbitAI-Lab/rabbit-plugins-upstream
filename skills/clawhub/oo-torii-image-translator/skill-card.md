## Description:

Torii Image Translator helps agents use OOMOL-connected Torii actions to extract OCR data, translate and typeset image text, inpaint masked areas, and check credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to route Torii Image Translator requests through the OOMOL oo CLI for OCR extraction, image translation, inpainting, typesetting, and credit lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner summary flags possible unintended paid image processing.

Mitigation: Confirm the exact image action, payload, and likely credit impact before running transformations such as translate, inpaint, or typeset.

Risk: The scanner guidance warns that installing the oo CLI by piping remote scripts into a shell can be unsafe.

Mitigation: Prefer verified official installation instructions and inspect or use safer installer methods before running remote install scripts.

Risk: User-supplied JSON passed directly to shell commands can create unsafe argument handling.

Mitigation: Use file-based JSON payloads or safe argument passing for user-provided data.

## Reference(s):

- [Torii Image Translator homepage](https://toriitranslate.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-torii-image-translator)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions may return structured OCR JSON, credit data, or downloadable image outputs.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
