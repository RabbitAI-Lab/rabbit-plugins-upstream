## Description:

Stellar Trails wraps agent work in a six-phase workflow with traceability IDs, entry and exit gates, scope commitment, verification reports, and adaptive handling for coding, document, data, visualization, planning, and question-answering tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and teams use this skill to impose process discipline on broad agent tasks, including coding, documents, data processing, charts, planning, and troubleshooting. It is intended to make work traceable through phase markers, gates, worklog snapshots, and verification outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is an always-on workflow wrapper with disclosed broad behaviors, including network commands, process management, self-updates, local serving, and persistent state.

Mitigation: Install only after review in an environment where those behaviors are acceptable, or make the behaviors explicit opt-in before broader deployment.

Risk: The security guidance warns against use in environments with sensitive repositories, tokens, or services bound to port 3000.

Mitigation: Run in an isolated workspace without sensitive credentials or services, and review local server and process behavior before installation.

Risk: Persistent logging and credential-related state may retain operational context beyond a single task.

Mitigation: Review generated logs and state files, avoid exposing secrets to the workspace, and clear state between sensitive tasks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [Workflow Phases](artifact/procedure/phases.md)
- [Error Resolution Decision Tree](artifact/procedure/error-resolution.md)
- [z.ai Sandbox Constraints](artifact/knowledge/zai-sandbox.md)
- [Evaluation Specification](artifact/evals/evals.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with phase markers, inline checklists, shell command blocks, file paths, and verification reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update workspace files, worklog snapshots, local process commands, and verification summaries depending on the task.]

## Skill Version(s):

9.14.0 (source: evidence release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
