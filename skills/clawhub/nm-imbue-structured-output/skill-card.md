## Description:

Formats review deliverables with consistent structure for comparable findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, reviewers, and analysts use this skill to turn review or analysis results into consistent stakeholder-facing deliverables with findings, recommendations, action items, and appendices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for ordinary formatting or reporting requests.

Mitigation: Use it when finalizing an analysis deliverable or when consistent reporting structure is explicitly relevant.

Risk: Generic command verification text in the artifact could be mistaken for required command execution.

Mitigation: Treat '--help' verification as optional and only when a specific command is already relevant; the skill itself does not require installing or running commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-structured-output)
- [Plugin homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/imbue)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report structures, action-item lists, release notes, incident reports, and appendix sections.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output is organized by selected deliverable type and ordered for stakeholder review.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
