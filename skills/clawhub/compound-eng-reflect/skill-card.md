## Description:

Session retrospective and skill audit tool for reflecting on a session, reviewing lessons learned, auditing what went well or wrong, and reviewing session effectiveness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to run structured session retrospectives, identify mistakes, friction, wasted effort, wins, and operational learnings, and propose concrete memory or skill improvements for review before persistence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proposed memory writes or skill edits can affect future agent behavior.

Mitigation: Review proposed memory entries and skill changes before approving persistence.

Risk: Session retrospectives may surface sensitive details from the conversation.

Mitigation: Do not persist secrets, credentials, private URLs, customer data, unredacted personal information, or machine-specific filesystem paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-reflect)
- [SKILL.md](artifact/SKILL.md)
- [SPEC.md](artifact/SPEC.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Guidance]

**Output Format:** [Markdown with numbered lists, tables, and diff or code blocks when proposing skill changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed memory entries or skill edits; persistence requires user authorization.]

## Skill Version(s):

4.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
