## Description:

Compresses verbose markdown daily logs into structured memory summaries that preserve key events, lessons, decisions, and todos without API keys or external dependencies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linglin6](https://clawhub.ai/user/linglin6)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to compress markdown daily logs into curated long-term memory entries for systems such as OpenClaw, Cursor, Claude Code, or other markdown-based memory workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted log text can be compressed into content that may later be added to long-term agent memory.

Mitigation: Review the compressed output before appending it to persistent memory, and treat source logs as untrusted data rather than instructions.

Risk: The default output path is a temporary file location.

Mitigation: Pass an explicit output file in a trusted workspace directory instead of relying on the default /tmp/compressed-memory.md path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linglin6/skills/memory-compress)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown summaries with CLI status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a compressed markdown summary to the requested output path; users should review it before appending to long-term memory.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
