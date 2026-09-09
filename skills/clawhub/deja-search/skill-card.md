## Description:

deja-vu memory - search the user's past AI coding sessions with the deja CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to search local AI coding-session history before repeating prior debugging, implementation, or decision work. It helps retrieve past fixes, commands, file rationale, and durable decisions through the deja CLI when relevant history exists on the machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent search broad local AI coding-session history across tools on the machine.

Mitigation: Install only when that access is acceptable, and prefer project, time, role, and result-limit filters when searching.

Risk: Full transcript retrieval can expose more historical context than needed for the current task.

Mitigation: Use summary or targeted search commands first, and retrieve full transcript pages only when detailed reasoning is necessary.

Risk: Durable memory entries may persist decisions beyond the current session.

Mitigation: Confirm any durable fact with the user before storing it with deja remember.

## Reference(s):

- [deja-vu memory for OpenClaw](https://vshulcz.github.io/deja-vu/guide/memory-for-openclaw.html)
- [ClawHub skill page](https://clawhub.ai/vshulcz/skills/deja-search)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-producing CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize recalled local session history and recommend filtered deja CLI searches; full transcript retrieval should be limited to cases where detailed context is needed.]

## Skill Version(s):

0.18.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
