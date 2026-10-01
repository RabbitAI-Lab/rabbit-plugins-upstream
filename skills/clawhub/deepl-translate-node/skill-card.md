## Description:

Helps agents translate text with DeepL when terminology, idioms, or other ambiguity makes accuracy especially important.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can request DeepL translations for text with specialized terminology, proper nouns, idioms, or ambiguous language, and compare the result with their own interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Translated text is sent to DeepL using the user's API key.

Mitigation: Obtain approval before sending confidential, regulated, or private material; keep the API key private.

Risk: A configured API host could send text and credentials to an unintended service.

Mitigation: Use only DeepL's official Free or Pro API host for DEEPL_API_HOST.

Risk: Literal terminology replacements can unintentionally change parts of other words.

Mitigation: Use unambiguous terms and review replaced text before relying on the translation.

## Reference(s):

- [Skill homepage (release metadata)](https://github.com/rockbenben/aishort-skills/tree/main/skills/deepl-translate-node)
- [DeepL supported languages](https://developers.deepl.com/docs/getting-started/supported-languages)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text translation, with explanatory guidance when interpretations differ]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves paragraphs; optional literal terminology replacements]

## Skill Version(s):

1.1.7 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
