## Description:

meeting-deep-process helps agents process meeting records into execution summaries, decision traces, participant-profile analyses, knowledge artifacts, and meeting-quality improvement guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers can use this skill to turn meeting transcripts, agendas, attendance data, recordings, and summaries into structured meeting reports, decision records, action lists, participant-profile analyses, and quality-improvement plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create sensitive long-term participant profiles and meeting-derived negotiation or interaction strategies.

Mitigation: Use only with organizational authorization and participant notice, treat generated profiles as sensitive records, set retention limits, and avoid covert monitoring, employment decisions, or manipulation.

Risk: The Tencent Meeting CLI fallback can install mutable software and expose meeting-control, mutation, permission-request, contact-lookup, and log-upload commands.

Mitigation: Prefer read-only meeting-data credentials and do not allow global @latest installs or control and mutation commands without separate explicit approval.

Risk: Meeting summaries, knowledge entries, and participant inferences may be incorrect or unsupported if raw meeting data is incomplete or ambiguous.

Mitigation: Require source citations, confidence labels, and human review for key decisions, knowledge entries, profile inferences, and quality-improvement recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/meeting-deep-process)
- [meeting-deep-process catalog](references/meeting-deep-process-catalog.md)
- [meeting-deep-process requirements](references/meeting-deep-process-requirements.md)
- [meeting-deep-process exemplars](references/exemplars.md)
- [tmeet CLI reference](references/tmeet-cli-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and structured lists, with optional JSON, TXT, CLI command, and configuration snippets when meeting-data workflows require them.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include participant profile inferences, meeting-quality scores, decision provenance, knowledge entries, action items, intervention suggestions, and retention guidance.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
