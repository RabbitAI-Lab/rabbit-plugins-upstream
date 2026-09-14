## Description:

Compresses prompts and long context by scoring sentence information density, preserving constraints, numbers, and code while removing filler and repetition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent operators use this skill to shorten prompts or source context before sending it to an AI agent, especially when token limits or context costs are a concern. It provides guidance plus a local Python CLI that trims lower-scoring sentences while preserving constraints, numeric details, and code blocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The published install instructions use an unpinned global installer, so installation may fetch code that differs from the reviewed artifact.

Mitigation: Install the reviewed artifact manually or pin the CLI and repository to a reviewed version or commit; avoid running the `npx` installer with administrator privileges.

Risk: The compressor reads the provided file path and prints selected content to stdout.

Mitigation: Only pass text or files intended for compression and avoid inputs containing secrets or sensitive data that should not appear in terminal output.

Risk: Compression can omit context that is useful for high-stakes decisions even when constraints, numbers, and code are protected.

Mitigation: Manually review compressed output before using it for critical, regulated, clinical, legal, or compliance-sensitive work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-compressor)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [LGD Hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with Python CLI commands and plain text compression output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI reads text or a file path, prints selected compressed content to stdout, and uses deterministic sentence scoring.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact files also reference 1.1.0 and 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
