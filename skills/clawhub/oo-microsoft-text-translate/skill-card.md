## Description:

Microsoft Text Translate helps agents run Microsoft Text Translate connector actions through the OOMOL oo CLI for translation, transliteration, language detection, sentence boundary detection, supported-language discovery, and dictionary lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to translate text, transliterate scripts, detect languages, inspect supported languages, and retrieve dictionary context through an OOMOL-connected Microsoft Text Translate account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Relevant text may be sent through OOMOL and Microsoft Text Translate.

Mitigation: Use the skill only for text approved for those services, and avoid sensitive or regulated content unless the user's organization permits that processing.

Risk: The setup instructions include remote installer commands that execute downloaded scripts in a shell.

Mitigation: Install the oo CLI only from a source the user independently trusts and verifies before running installer commands.

Risk: Actions depend on a valid OOMOL account, Microsoft Text Translate connection, credentials, and billing status.

Mitigation: Run connector actions after setup is complete, and stop on authentication, connection, credential, or billing errors until the user resolves them.

## Reference(s):

- [ClawHub Microsoft Text Translate Skill](https://clawhub.ai/oomol/skills/oo-microsoft-text-translate)
- [Microsoft Text Translate Homepage](https://azure.microsoft.com/en-us/products/ai-services/ai-translator)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses may include a data object and execution metadata from the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
