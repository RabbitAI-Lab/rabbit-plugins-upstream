## Description:

Batch-translates PDF, Markdown, and text documents with a user-controlled local llama.cpp-compatible translation endpoint, supporting eight major languages and Markdown output on Windows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[43622283](https://clawhub.ai/user/43622283)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and document-heavy users use this skill to translate individual files or batches of PDFs into target-language Markdown while keeping the default model endpoint local.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text is sent to the configured llama.cpp-compatible API endpoint, so using a remote or untrusted endpoint can expose confidential content.

Mitigation: Keep the API URL at the localhost default, confirm the server binds to 127.0.0.1, and configure a remote endpoint only when sending document text there is intentional.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/43622283/skills/li-local-pdf-translate)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown files and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are named with the target language code and may include per-run translation statistics.]

## Skill Version(s):

2.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
