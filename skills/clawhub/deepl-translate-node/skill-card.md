## Description:

Use when a translation must be right and the agent is uncertain, especially for proper nouns, legal, medical, technical terms, idioms, distant language pairs, or user-requested DeepL translation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external agents use this skill to call DeepL when translation precision matters and self-translation may be unreliable. It is suited for terminology-heavy, ambiguous, idiomatic, low-resource, distant-language, or high-stakes translation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text submitted for translation is sent to DeepL or to the host configured in DEEPL_API_HOST.

Mitigation: Use the skill only for text that may be sent to that service under the user's DeepL plan, organization policy, and data-handling requirements.

Risk: A misconfigured DEEPL_API_HOST could send translation text and authentication headers to an untrusted endpoint.

Mitigation: Set DEEPL_API_HOST only to a trusted DeepL endpoint, such as api-free.deepl.com or api.deepl.com.

Risk: DEEPL_API_KEY is required for operation and could be exposed if hardcoded or shared in prompts.

Mitigation: Keep the API key in the environment, never hardcode it in skill files, and rotate it if exposure is suspected.

## Reference(s):

- [DeepL Supported Languages](https://developers.deepl.com/docs/getting-started/supported-languages)
- [DeepL Languages API](https://api-free.deepl.com/v3/languages?resource=translate_text)
- [ClawHub Skill Page](https://clawhub.ai/rockbenben/skills/deepl-translate-node)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain translated text on stdout, with Markdown guidance and shell command examples in agent responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node and DEEPL_API_KEY; optional DEEPL_API_HOST selects the DeepL Pro endpoint.]

## Skill Version(s):

1.1.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
