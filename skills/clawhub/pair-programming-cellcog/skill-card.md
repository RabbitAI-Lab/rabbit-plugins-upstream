## Description:

AI pair programming powered by CellCog Desktop for coding, debugging, refactoring, and building directly on a user's machine with terminal and file access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to delegate coding, debugging, refactoring, setup, and documentation tasks to CellCog cloud agents operating through CellCog Desktop against a selected local workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous terminal and file access can modify or disclose content in the selected workspace.

Mitigation: Install only after review, use a narrow working directory, and avoid repositories containing secrets or regulated data.

Risk: CellCog Desktop and CELLCOG_API_KEY enable cloud-backed agents to act on the user's machine.

Mitigation: Protect the API key, stop the desktop bridge when it is not needed, and review tasks before enabling co-work.

## Reference(s):

- [Pair Programming skill page](https://clawhub.ai/cellcog/skills/pair-programming-cellcog)
- [CellCog publisher profile](https://clawhub.ai/user/cellcog)
- [CellCog homepage](https://cellcog.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and shell command examples; downstream agent runs may produce code, file changes, and command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, the cellcog dependency, CellCog Desktop, and CELLCOG_API_KEY; co-work sessions are scoped by the selected working directory.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
