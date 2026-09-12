## Description:

Operate a Git-backed Archivum as durable agent memory for projects, research, decisions, meetings, tasks, sources, and outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and project teams use Archivum to find, capture, connect, update, audit, and resume durable project memory with source-aware records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Durable captures and learned preferences may persist in the Archivum workspace.

Mitigation: Review where ARCHIVUM_ROOT points and avoid using the skill on sensitive archives unless that persistence is intended.

Risk: Archive records may be shared or published after the skill writes them.

Mitigation: Review changes before sharing or publishing and treat visibility metadata as separate from authorization to publish.

Risk: Incorrect assumptions could be recorded as durable project state.

Mitigation: Preserve evidence boundaries, source paths, and maturity labels when capturing or updating records.

## Reference(s):

- [Archivum ClawHub skill page](https://clawhub.ai/antreasantoniou/skills/archivum)
- [Publisher profile](https://clawhub.ai/user/antreasantoniou)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose with repository-relative paths, record updates, configuration guidance, and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write scoped Archivum records when the user asks to capture, update, audit, initialize, or resume work.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
