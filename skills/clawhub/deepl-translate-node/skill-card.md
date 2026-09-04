## Description:

Use when a translation must be right and uncertainty is costly, including proper nouns, domain terms, idioms, and distant language pairs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Agents, developers, and other users use this skill to call DeepL for translations where terminology, idioms, regional variants, or high-stakes wording make self-translation risky. It guides when to use DeepL, how to configure credentials, and how to run the bundled Node helper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected translation text is sent to DeepL.

Mitigation: Use this skill only when the user or deployment policy allows sending the selected text to DeepL.

Risk: The skill requires a DeepL API key.

Mitigation: Provide the key through DEEPL_API_KEY and avoid hardcoding or committing credentials.

Risk: DEEPL_API_HOST can redirect requests away from the default Free endpoint.

Mitigation: Keep DEEPL_API_HOST pointed at DeepL's official hosts unless a different endpoint is intentional and approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rockbenben/skills/deepl-translate-node)
- [Skill homepage](https://github.com/rockbenben/aishort-skills/tree/main/skills/deepl-translate-node)
- [DeepL supported languages](https://developers.deepl.com/docs/getting-started/supported-languages)
- [DeepL languages endpoint](https://api-free.deepl.com/v3/languages?resource=translate_text)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text translation on stdout; guidance may be Markdown with shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper preserves paragraphs, writes failures to stderr, exits non-zero on errors, and caps DeepL requests at 60 seconds.]

## Skill Version(s):

1.1.6 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
