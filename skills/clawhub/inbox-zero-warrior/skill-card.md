## Description:

Triage, categorize, and conquer email overload by classifying emails by urgency, generating quick replies, detecting newsletters for bulk unsubscribe, and producing daily digests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Knowledge workers, freelancers, consultants, small business owners, and people returning to large unread inboxes use this skill to analyze email exports, prioritize responses, identify low-value messages, and draft routine replies. It is intended for local export analysis and decision support, not for sending email or making account changes directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email exports and generated triage outputs can contain sensitive personal, customer, or business information.

Mitigation: Process only exports the user is comfortable handling locally, and avoid saving or displaying outputs in shared terminals or folders.

Risk: Unsubscribe, delete/file, and reply recommendations can be wrong or incomplete.

Mitigation: Review every suggested unsubscribe, delete/file action, and reply draft before taking action in an email client.

## Reference(s):

- [Email Triage Classification Reference](references/triage_rules.md)
- [Server-resolved GitHub provenance](https://github.com/voronindenis5/inbox-zero-warrior)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/inbox-zero-warrior)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with command examples and JSON-compatible triage outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prioritized action lists, newsletter unsubscribe lists, digest summaries, and suggested replies for user review.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
