## Description:

SKILL1 helps agents run a local, zero-dependency Python file organization CLI for classifying files, batch renaming, cleaning empty directories and duplicates, and flattening nested folders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[q-ian-l](https://clawhub.ai/user/q-ian-l)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users can use this skill when they need an agent to organize an explicitly chosen local directory, preview planned file moves or deletions, and run the bundled file management CLI only after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The duplicate detection workflow reads local file bytes to compute hashes, despite artifact text claiming no file contents are read.

Mitigation: Avoid duplicate scans on sensitive folders unless local byte-level hashing is acceptable.

Risk: File organization, renaming, flattening, and cleanup actions can move, rename, or delete files when applied.

Mitigation: Run in dry-run mode first, inspect the planned changes, and use --apply only after the target directory and operation are confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/q-ian-l/skills/skill1)
- [Publisher profile](https://clawhub.ai/user/q-ian-l)
- [ClawHub homepage](https://clawhub.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs local Python CLI operations and should preview destructive actions before applying them.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
