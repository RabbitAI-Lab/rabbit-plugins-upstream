## Description:

Compress natural-language memory files into shorter caveman-style Markdown while preserving technical details, code, URLs, and document structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Compress to shorten natural-language memory files such as CLAUDE.md, todos, and preferences while retaining technical anchors needed by downstream agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected file contents may be sent to Claude/Anthropic during compression.

Mitigation: Use only on intentionally selected non-sensitive files and avoid files containing credentials, secrets, or private data.

Risk: The active file can be replaced by compressed output.

Mitigation: Keep the generated .original.md backup and review the diff before relying on the compressed memory file.

Risk: Compressed memory text may omit nuance or introduce misleading guidance for future agent sessions.

Mitigation: Review compressed output before treating it as authoritative agent memory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seanford/skills/compress)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and CLI status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May overwrite the selected natural-language file and create a .original.md backup after validation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
