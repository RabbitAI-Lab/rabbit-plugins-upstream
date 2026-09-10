## Description:

Translates PDF, Markdown, and TXT documents on Ubuntu/Linux through a local llama.cpp-compatible model endpoint, with eight-language support and target-language Markdown output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[43622283](https://clawhub.ai/user/43622283)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to translate batches of PDF, Markdown, or TXT documents through a local model endpoint and produce target-language Markdown for review or downstream editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text is sent to the configured translation endpoint, and a remote api_url would receive the user's document content.

Mitigation: Keep api_url pointed at localhost for private material and use only trusted endpoints when changing the configuration.

Risk: The default local API key may be unsuitable if the local server is exposed beyond the user's machine.

Mitigation: Bind the model server to localhost for local use and change the default API key when local exposure matters.

Risk: Environment setup can involve installing dependencies, llama.cpp components, or large model files.

Mitigation: Review the exact commands and model sources before approving any installation or download.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/43622283/skills/li-local-pdf-translate-linux)
- [Publisher profile](https://clawhub.ai/user/43622283)
- [README.md](README.md)

## Skill Output:

**Output Type(s):** [markdown, text, shell commands, configuration, guidance]

**Output Format:** [Markdown files plus concise command and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates target-language .md files with source, direction, depth, timestamp, and per-page headings when translating documents.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
