## Description:

Sets up a local knowledge base and retrieval workflow on a Mac mini, including document extraction, OCR repair, summaries, and optional scheduled Feishu delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Mac mini owners and developers can use this skill to set up and maintain a local document knowledge base with retrieval, OCR, and scheduled summaries. It also guides troubleshooting and migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OCR repair can copy unrelated private documents into summaries that may later be sent to Feishu.

Mitigation: Wait for source-path containment checks before batch OCR repair, keep imported archives untrusted, back up summaries, and verify the recipient before enabling scheduled delivery.

Risk: Installation changes default-agent permissions, and dependency verification is incomplete.

Mitigation: Review the permission and dependency changes before installation; test setup and document conversion in the intended environment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/seairteng/skills/macmini-knowledge-base)
- [Ollama download](https://ollama.com/download)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands and configuration snippets, plus document summaries and catalog files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create or update summary and catalog files and configure persistent scheduled analysis and Feishu delivery.]

## Skill Version(s):

1.4.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
