## Description:

Meeting Deep Process helps an agent analyze meeting transcripts and meeting metadata across execution, participant profiling, group dynamics, knowledge extraction, and meeting-quality improvement workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, consultants, and meeting facilitators use this skill to turn meeting recordings, transcripts, agendas, and participant context into structured meeting summaries, decision traceability, action follow-up, participant profiles, group-dynamics analysis, and improvement prompts for future meetings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can infer participant profiles and group dynamics from meeting transcripts, which may expose sensitive personal or workplace information.

Mitigation: Use only with authorized meetings where participants understand transcripts may be analyzed and profiles may be accumulated over time.

Risk: The bundled tmeet CLI reference includes broad meeting and control commands that exceed read-only analysis needs.

Mitigation: Use a pinned, isolated, read-only meeting-data integration and do not allow meeting administration commands.

Risk: Inferred profiles and meeting analytics could be misused for hiring, discipline, compensation, or other high-stakes decisions.

Mitigation: Require independent human review and avoid using these inferences as the sole basis for high-stakes decisions.

Risk: Negotiation or interaction-strategy examples may encourage deceptive or manipulative behavior if used operationally.

Mitigation: Remove or revise deceptive negotiation examples and enforce non-manipulative, consent-aware strategy guidance before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/meeting-deep-process)
- [Meeting Deep Process task catalog](references/meeting-deep-process-catalog.md)
- [Meeting Deep Process requirements](references/meeting-deep-process-requirements.md)
- [Meeting Deep Process exemplar index](references/exemplars.md)
- [tmeet CLI reference](references/tmeet-cli-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, structured tables, checklists, meeting-analysis notes, and occasional shell-command guidance for meeting data retrieval.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include confidence labels, source references to meeting IDs, speakers, timestamps, and review markers for sensitive or uncertain inferences.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
