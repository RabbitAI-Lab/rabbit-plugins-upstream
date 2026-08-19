## Description:

A platform-agnostic meeting analysis and quality enhancement skill that turns meeting data into execution summaries, role-profile reports, group-dynamics analysis, knowledge assets, quality diagnostics, and improvement guidance across eight meeting scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and agents use this skill to process meeting transcripts, recordings, minutes, agendas, participant context, and historical meeting records into structured analysis, decision records, participant profiles, knowledge-base entries, quality scores, and concrete meeting-improvement plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may analyze sensitive meeting transcripts, recordings, minutes, agendas, participant data, and historical meeting records.

Mitigation: Use it only with appropriate participant notice and authorization, least-privilege access to meeting data, and explicit rules for retention, deletion, sharing, and human review.

Risk: Durable participant profiles and 12-dimension role inferences can create privacy, fairness, or overreach concerns.

Mitigation: Limit profile use to meeting-relevant, publicly expressed information; preserve confidence labels; avoid inferring text-invisible traits; and honor deletion requests for participant profile data.

Risk: Meeting-derived knowledge entries, decisions, and group-dynamics conclusions may be incorrect or insufficiently supported.

Mitigation: Require traceable source citations, confidence labels, and human review before promoting critical decisions or knowledge entries into durable systems.

Risk: The tmeet fallback and mutating or administrative meeting commands could expand access or change meeting state.

Mitigation: Enable fallback data-source commands only after separate approval and audit, and avoid mutating or administrative commands unless they are explicitly authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/meeting-deep-process)
- [Publisher profile](https://clawhub.ai/user/wangjiaocheng)
- [Meeting deep process catalog](references/meeting-deep-process-catalog.md)
- [Meeting deep process requirements](references/meeting-deep-process-requirements.md)
- [tmeet CLI reference](references/tmeet-cli-reference.md)
- [Report exemplar index](references/exemplars.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and structured text, with optional JSON/TXT exports and shell commands for data-source workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include meeting summaries, decision records, action lists, participant profiles, analysis reports, knowledge entries, quality diagnostics, intervention cards, follow-up questions, and improvement plans.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
