## Description:

Reviews a session for lessons learned and audits skills for actionable improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to review a session's mistakes, friction, and successes, then prioritize improvements and audit any skills used.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive information could be retained in session learnings.

Mitigation: Review proposed memory items and exclude secrets and sensitive personal data before approving any write.

Risk: Cross-project memory could carry inappropriate guidance into other work.

Mitigation: Approve concrete items and their destination before any cross-project memory write.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-reflect)
- [Capture and remedy routing](references/capture-and-routing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown retrospective and prioritized recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose memory items or skill edits; persistence requires authorization.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
