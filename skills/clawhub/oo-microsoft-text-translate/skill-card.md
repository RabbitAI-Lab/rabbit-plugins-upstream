## Description:

Microsoft Text Translate helps agents use an OOMOL-connected Microsoft Text Translate account to translate text, transliterate scripts, detect languages, identify sentence boundaries, and retrieve dictionary information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to run Microsoft Text Translate connector actions through OOMOL for translation, transliteration, language detection, sentence boundary detection, supported-language discovery, and dictionary lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the installer path before use and prefer a pinned official release or package-manager install with signature or checksum verification.

## Reference(s):

- [Microsoft Text Translate ClawHub Skill](https://clawhub.ai/oomol/skills/oo-microsoft-text-translate)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Azure AI Translator](https://azure.microsoft.com/en-us/products/ai-services/ai-translator)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON payloads and connector response summaries.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
