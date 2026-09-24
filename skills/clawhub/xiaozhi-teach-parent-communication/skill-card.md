## Description:

Helps independent teachers draft specific, low-anxiety, actionable parent communications from learning records while preserving consent checks, teacher review, and limited communication logging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this agent to draft one-to-one parent messages, weekly group announcements, renewal explanations, and concern responses for Chinese K12 tutoring contexts. The skill keeps the teacher in control by checking consent, avoiding automatic sending, and recording only limited channel and status fields.

### Deployment Geography for Use:

China Mainland by default; localize crisis-contact, curriculum, consent, and parent-communication assumptions before deployment elsewhere.

## Known Risks and Mitigations:

Risk: Parent messages could be drafted without the right consent or sent without teacher review.

Mitigation: Confirm parentCommunicationAllowed and emotionSharingWithParent before drafting; keep outputs as teacher-reviewed drafts and do not send automatically.

Risk: The published behavior assumes a Chinese K12 tutoring context, including curriculum, consent, and crisis-contact defaults.

Mitigation: Localize wording, curriculum assumptions, consent defaults, and crisis-contact guidance before using the skill outside that context.

Risk: Parent communication can expose student or family personal information.

Mitigation: Use student aliases, keep specific student feedback in private one-to-one channels, avoid contact details and family background, and persist only limited communication-log fields.

Risk: Crisis signals could be softened by normal low-anxiety parent-communication wording.

Mitigation: Stop the normal drafting flow when crisis signals appear and follow the crisis referral protocol, including locale checks before giving emergency resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-parent-communication)
- [Typical scenario scripts](references/typical-scenario-scripts.md)
- [Weekly group announcement template](references/weekly-group-announcement-template.md)
- [Communication principles examples](references/communication-principles-examples.md)
- [Solo teacher workspace schema](shared/solo-teacher-workspace.schema.json)
- [Authorization vocabulary](shared/vocab.md)
- [Crisis exception protocol](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Plain text or Markdown message drafts with structured parentCommunicationLogs[] fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts only; no automatic sending. Persistent writes are limited to parentCommunicationLogs[].]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
