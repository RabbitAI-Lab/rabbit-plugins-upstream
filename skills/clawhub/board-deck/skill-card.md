## Description:

board-deck turns a period's financials into structured text for the finance section of a board deck, including headline metrics, movement, narrative, and gaps it could not determine from the input.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillsandagentsco](https://clawhub.ai/user/skillsandagentsco)

### License/Terms of Use:

MIT-0

## Use Case:

Finance leaders, CFO staff, and agents supporting board preparation use this skill to convert current-period P&L exports, optional comparison data, and CFO notes into board-ready finance section text with explicit unknowns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Board materials can contain sensitive financial and operating information.

Mitigation: Provide only financial exports, CFO notes, and prior board material that are appropriate to share in the agent session.

Risk: Generated board-deck narrative could misstate financial performance or over-explain a movement.

Mitigation: Review the generated finance section carefully before using it in board materials, especially explanations of material movements.

Risk: Unsupported figures or causes could mislead readers if source data is incomplete.

Mitigation: Rely on the skill's required traceability and unknowns section, and supply missing P&L, comparison, plan, or CFO context inputs when gaps are listed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skillsandagentsco/skills/board-deck)
- [Skills & Agents Co board-deck catalog page](https://skillsandagents.co/skills/board-deck/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured Markdown or plain text finance narrative; no slides, charts, or images.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided financial inputs, includes a required unknowns section, and does not invent figures or unsupported causes.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
