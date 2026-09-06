## Description:

Plandeck gives agents a live local Kanban board and deterministic continuity layer for long-running, dependency-aware plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Plandeck to turn multi-step project plans into a file-backed board that tracks dependencies, progress, next actions, and recovery state across context resets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes planning, board, and continuity files into the project workspace.

Mitigation: Run it only in projects where local planning artifacts are expected, and review generated plan and continuity files before sharing or committing them.

Risk: Board contents may be exposed if the local board is bound beyond localhost.

Mitigation: Keep the default localhost binding unless wider network access is intentional and acceptable.

Risk: Referenced card notes and receipts can appear in the local board API.

Mitigation: Avoid putting secrets or sensitive data in card notes, receipts, or plan files used with the board.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/plandeck)
- [Server-resolved GitHub provenance](https://github.com/OthmanAdi/plandeck)
- [README](README.md)
- [planning-with-files lineage](https://github.com/OthmanAdi/planning-with-files)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and generated local planning files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic file-backed outputs; optional local browser board for live plan state.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
