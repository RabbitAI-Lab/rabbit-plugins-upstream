## Description:

Memory Bank text-based update workflow following integrated-rules v6.12 for manually updating markdown memory-bank task, session, cache, and edit-history files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[space-cadet](https://clawhub.ai/user/space-cadet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to document project work in classic text-based memory-bank repositories by creating or updating task records, session files, session cache, implementation notes, and edit chunks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can read project history and status files while reconstructing undocumented work.

Mitigation: Use it only in workspaces where that project context may be reviewed for memory-bank maintenance.

Risk: The workflow can create or update markdown files under memory-bank as part of documentation maintenance.

Mitigation: Install it only in projects where text-based memory-bank maintenance is intended, and clarify approval requirements before use.

Risk: Using the text workflow in a database-native memory-bank project can produce inconsistent documentation.

Mitigation: Use this skill for classic text-based memory banks and use the database-native workflow when the project requires one.

## Reference(s):

- [Memory Bank Text-Based Update Workflow](artifact/SKILL.md)
- [Integrated Code Rules and Memory Bank System](artifact/references/integrated-rules-v6.12.md)
- [Memory Bank File Templates](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with templates and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides updates to text-based memory-bank files and expects approval requirements to be clarified before file changes.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
