## Description:

Microsoft Text Translate lets an agent use OOMOL's Microsoft Text Translate connector to detect languages, translate text, transliterate scripts, inspect supported languages, and retrieve dictionary entries or examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Microsoft Text Translate actions through an OOMOL-connected account for translation, language detection, transliteration, sentence boundary detection, supported-language lookup, and dictionary context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Translation inputs may be sent through OOMOL's Microsoft Text Translate connector and the connected Microsoft service.

Mitigation: Do not use the skill for sensitive text unless that data is approved for the connected Microsoft and OOMOL services.

Risk: The skill depends on a working OOMOL CLI sign-in and Microsoft Text Translate connection.

Mitigation: Run setup or reconnection steps only after an auth, scope, credential, app, or billing error indicates they are needed.

## Reference(s):

- [Microsoft Text Translate Skill Page](https://clawhub.ai/oomol/skills/oo-microsoft-text-translate)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Microsoft Azure AI Translator](https://azure.microsoft.com/en-us/products/ai-services/ai-translator)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when actions are run with --json.]

## Skill Version(s):

1.0.0 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
