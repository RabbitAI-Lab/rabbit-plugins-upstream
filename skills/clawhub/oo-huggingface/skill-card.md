## Description:

This skill lets agents use Hugging Face through the OOMOL-connected `oo` CLI for searching, reading data, generating chat completions, and generating embeddings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Hugging Face through an OOMOL-connected account for model, dataset, Space, endpoint, repository, trending-content, chat-completion, and embedding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Prefer a verified or package-manager installation path for the oo CLI, and review installer contents before execution.

Risk: Inference actions can send prompts or embedding text to Hugging Face Inference Providers and may affect billing.

Mitigation: Send sensitive text only when the user intends external processing, and confirm cost-sensitive inference use before running those actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-huggingface)
- [Hugging Face](https://huggingface.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
