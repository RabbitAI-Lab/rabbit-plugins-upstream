## Description:

家长沟通助手 helps independent teachers draft concrete, low-anxiety, actionable parent communication while checking consent, communication cadence, and send-status logging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to draft parent messages for lesson updates, learning concerns, renewal conversations, and weekly group announcements. It is intended to keep communication factual, low-anxiety, consent-aware, and teacher-reviewed before sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reference file expands beyond parent-message drafting into changing student status or communication preferences and touching stage-report-like workflows.

Mitigation: Keep normal use scoped to drafting and parentCommunicationLogs; require explicit teacher authorization for student status or preference changes and route stage reports to the dedicated renewal-report workflow.

Risk: Crisis referral guidance includes region-specific emergency and hotline references that may be wrong for users outside that locale.

Mitigation: Confirm the user's country or region before presenting hotline guidance, and use local emergency and professional-support resources.

Risk: Parent communications can disclose student performance or emotional observations without proper consent or in an inappropriate group channel.

Mitigation: Check parent communication and emotion-sharing consent before drafting, use aliases, keep individual feedback in private channels, and avoid storing contact details or parent reply text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-parent-communication)
- [communication-principles-examples.md](references/communication-principles-examples.md)
- [typical-scenario-scripts.md](references/typical-scenario-scripts.md)
- [weekly-group-announcement-template.md](references/weekly-group-announcement-template.md)
- [vocab.md](shared/vocab.md)
- [crisis-exception.md](shared/crisis-exception.md)
- [crisis-referral-protocol.md](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain-text parent-message drafts with structured communication log fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher reviews and sends drafts; logs should record channel/status only and avoid contact details or parent reply text.]

## Skill Version(s):

2.1.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
