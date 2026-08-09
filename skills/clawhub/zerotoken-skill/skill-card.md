## Description:

Token-efficient assistant discipline for concise answers and task execution, including optional file and Windows encoding utilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phoenixlucky](https://clawhub.ai/user/phoenixlucky)

### License/Terms of Use:

GPL-3.0

## Use Case:

Developers and agent users use ZeroToken to keep assistant work concise, focused, and token-efficient across question answering, code changes, document summarization, and larger engineering tasks. The skill also provides optional guidance and utilities for Unicode-safe file handling, batch edits, and Windows/PowerShell encoding workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recursive encoding conversion or repair commands can modify many files if pointed at a broad directory.

Mitigation: Run scan or preview mode first, keep backups, and restrict repair commands to the intended path.

Risk: The skill can guide local file reads, file writes, batch edits, encoding conversion, and git operations.

Mitigation: Review proposed file and git changes before execution and operate inside a trusted workspace.

Risk: External search guidance may send query text to browser or search tooling when current information is required.

Mitigation: Do not include secrets, credentials, or sensitive unpublished information in search queries.

## Reference(s):

- [ZeroToken Skill on ClawHub](https://clawhub.ai/phoenixlucky/skills/zerotoken-skill)
- [Unicode Encoding Specification](docs/unicode-encoding-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Concise Markdown guidance with optional inline code, shell command snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include direct answers, short implementation plans, file edit guidance, and encoding repair commands.]

## Skill Version(s):

1.9.1 (source: server release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
