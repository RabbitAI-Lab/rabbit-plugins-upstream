## Description:

CEO To-Do keeps one canonical markdown to-do document current by capturing commitments, turning them into prioritized next actions, flagging stale or waiting items, archiving completed work, and validating mutating runs with snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillsandagentsco](https://clawhub.ai/user/skillsandagentsco)

### License/Terms of Use:

MIT-0

## Use Case:

CEOs and executive operators use this skill to maintain a trusted single source of truth for commitments, next actions, waiting items, stale work, and weekly review. The companion daily agent can read Gmail and Slack through read-only connectors to capture new commitments into the same markdown workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The manual skill can modify the markdown to-do file selected by the user.

Mitigation: Use it only on the intended canonical file and keep the snapshot, proposal validation, written-file validation, and postcondition report gates in place.

Risk: The daily agent reads Gmail and Slack through connectors to identify commitments.

Mitigation: Use the daily agent only when read-only connector access is acceptable, and keep outbound actions human-controlled.

Risk: Ambiguous input could be turned into an incorrect commitment or priority.

Mitigation: Place unclear captures in NEEDS-REVIEW verbatim and require human clarification before treating them as committed next actions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/skillsandagentsco/skills/ceo-todo)
- [Skills & Agents CEO To-Do catalog page](https://skillsandagents.co/skills/ceo-todo/)
- [Skills & Agents CEO To-Do Daily agent page](https://skillsandagents.co/agents/ceo-todo-daily/)
- [Brian Halligan public single-doc system post](https://x.com/bhalligan/status/2054689082857730097)
- [Brian Halligan follow-up post](https://x.com/bhalligan/status/2054691150175584330)
- [Sample canonical to-do document](references/sample-todo.md)
- [Validator script](references/validate.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown document updates, inline shell commands, and concise postcondition reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mutating runs are snapshot-backed and validator-gated; the daily agent uses read-only Gmail and Slack connectors when enabled.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
