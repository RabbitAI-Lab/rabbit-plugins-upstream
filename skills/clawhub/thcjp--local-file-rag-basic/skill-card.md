## Description:

文件RAG is a Chinese-language local file RAG helper for reading, processing, converting, and extracting content from local documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, independent operators, and enterprise teams use this skill to organize local files, extract document content, convert formats, and support knowledge-management workflows in Chinese-language agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests local read, write, and command execution authority for file and RAG workflows.

Mitigation: Review proposed file paths and commands before execution, run in a constrained workspace, and avoid destructive operations without explicit approval.

Risk: Security evidence warns that claimed encryption, permission controls, sandboxing, command allowlists, sharing, and collaboration features are not supported by the submitted artifact.

Mitigation: Do not rely on those protections unless they are provided by the host agent or independently verified outside the skill.

Risk: Local file processing can expose secrets, credentials, or confidential folders to the agent context.

Mitigation: Avoid sensitive directories and secret-bearing files unless the user has reviewed and approved the exact scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/local-file-rag-basic)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request local file paths, operation parameters, and optional user context.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
