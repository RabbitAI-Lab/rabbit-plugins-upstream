## Description:

Compresses long AI-agent logs into structured Markdown summaries for memory maintenance, preserving key events, lessons, and follow-up items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to compress daily or weekly Markdown memory logs into shorter summaries before appending them to MEMORY.md. It is intended for explicit log-compression and memory-maintenance requests where the user can review the generated summary before persistent writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command and write authority over persistent agent memory.

Mitigation: Use it only after an explicit log-compression request, confirm the input and output paths, and review generated summaries before writing to MEMORY.md.

Risk: The referenced Node.js compression script is not included in the artifact.

Mitigation: Inspect and verify the publisher-provided script before granting exec access or running compression commands.

Risk: Automatic archive or move operations can make original logs harder to recover.

Mitigation: Keep backups and avoid moving or archiving original logs automatically unless recovery has been tested.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/thcjp/skills/memory-compress)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Markdown summaries with shell command snippets and file-write guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries should be reviewed before appending to persistent memory files.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
