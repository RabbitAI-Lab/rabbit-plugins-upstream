## Description:

Guides users through running local Ollama models and building a searchable personal knowledge base on modest hardware.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theoretical text all rights reserved

## Use Case:

Individuals and teams use this skill to set up a local LLM, organize text documents, and get guidance for summarization and knowledge-base Q&A.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document contents in summaries or questions can reach a remote HTTP endpoint when Ollama is configured away from localhost.

Mitigation: Keep OLLAMA_BASE on localhost unless you trust the remote server; review documents before submitting them.

Risk: The bundled security-audit claim does not accurately reflect the release's security assessment.

Mitigation: Do not rely on the bundled audit claim; review the release and its security findings before installing.

Risk: Setup reads library text files and may initialize a Git repository in the chosen library directory.

Mitigation: Limit the library directory to intended .md/.txt files and inspect the setup command before running it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/medxpert-llm-library)
- [MedXpert website](https://medxpert.cn)
- [Ollama download](https://ollama.com/download)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text, Markdown]

**Output Format:** [Markdown or plain text, with optional generated document summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries and answers depend on the configured library files and Ollama model.]

## Skill Version(s):

1.29.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
