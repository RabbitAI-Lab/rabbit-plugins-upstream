## Description:

A cross-machine offline taskbox for queuing, syncing, and running local LLM tasks with Ollama when cloud use is costly, unavailable, or inappropriate for sensitive data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to manage offline task queues, exchange sync packs across machines, and process queued work with a local Ollama model. It is suited for batch, repeated, document, or sensitive tasks that should continue without network access or avoid cloud quota usage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task titles, details, and results are persisted in a local taskbox.json file.

Mitigation: Use a trusted local workspace, avoid adding secrets unless local storage is acceptable, and delete or protect taskbox.json according to the sensitivity of queued work.

Risk: Exported sync packs contain all tasks in the local taskbox.

Mitigation: Review task contents before exporting or sharing sync packs, especially when tasks may contain confidential data.

Risk: The offline worker sends queued task text to the user's local Ollama model process.

Mitigation: Run the worker only when the selected local model and machine are approved for the queued task content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/cross-machine-offline-taskbox)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and local JSON task data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local task records, sync-pack JSON files, and short local-model results when the bundled worker is run.]

## Skill Version(s):

2.2.2 (source: server release, SKILL.md frontmatter, and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
