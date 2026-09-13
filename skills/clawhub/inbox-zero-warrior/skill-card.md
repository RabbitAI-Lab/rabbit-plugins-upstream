## Description:

Inbox Zero Warrior analyzes local email exports to classify urgency and category, identify newsletters, draft quick replies, and produce prioritized digest and action guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and knowledge workers use this skill to process local inbox exports, prioritize required responses, identify newsletter senders, and draft routine replies without connecting to a live mailbox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive inbox content may be included in local exports, generated reports, terminal output, or suggested replies.

Mitigation: Use minimized or redacted local exports and avoid sharing generated files, reports, or terminal output.

Risk: Unsubscribe links extracted from emails may point to untrusted or privacy-sensitive destinations.

Mitigation: Manually inspect unsubscribe links before opening them and use browser or mail-client safety controls.

Risk: Delete, file, unsubscribe, and reply labels may be incorrect because they are heuristic recommendations.

Mitigation: Treat labels and replies as reviewable suggestions and confirm actions before applying them to a mailbox.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/voronindenis5/inbox-zero-warrior)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/inbox-zero-warrior)
- [Email Triage Classification Reference](references/triage_rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON file outputs, and terminal reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write triaged JSON files and print reports; does not send email or modify mailboxes directly.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
