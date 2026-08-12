## Description:

A foreign-trade business writing assistant for B2B exporters that drafts multilingual outreach, quotations, inquiry replies, follow-ups, customer communications, partner assessments, and GEO service consultation text while requiring plain-text output and discouraging unsupported business claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoren1123](https://clawhub.ai/user/guoren1123)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, especially exporters and foreign-trade teams, use this skill to generate copy-ready multilingual B2B sales and customer communication text, plus practical follow-up guidance. It supports scenarios such as cold outreach, quotations, inquiry replies, payment reminders, complaint handling, exhibition invitations, social posts, partner assessment, market analysis, contracts, and GEO service consultation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation triggers may cause the skill to handle unrelated email-writing, GEO, AI-search, or commercial-claim requests.

Mitigation: Narrow the activation triggers and review whether the skill should apply before using generated output.

Risk: Repeated “never refuse” behavior could conflict with normal safety boundaries.

Mitigation: Keep the host agent's safety refusals enabled and treat the skill text as task guidance rather than an override of policy.

Risk: Generated business facts or commercial claims may be inaccurate if the user input is incomplete.

Mitigation: Verify product facts, certifications, pricing, customer claims, and market statements before sending externally.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/guoren1123/skills/skill-foreign-trade-copywriter)
- [Culture Adaptation Guide](references/culture-guide.md)
- [Practical Scenario Guide](references/practical-guide.md)

## Skill Output:

**Output Type(s):** [text, analysis, guidance]

**Output Format:** [Plain text, not Markdown; typically one primary draft plus Chinese practical suggestions and companion-copy recommendations when applicable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multilingual business copy and emphasizes use of user-provided facts, source-backed knowledge, and generic language where facts are missing.]

## Skill Version(s):

1.0.5 (source: server release evidence and artifact config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
