## Description:

Search the owner's Telegram, MAX, mail, and notes for information about people and projects, then record proposed facts, memories, and key documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

External users can search their connected messaging, email, and notes for information about people, projects, agreements, and key documents, then stage memory updates for owner review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An MCP permission set to ask does not display a confirmation prompt, and the separately installed package's behavior was not verified.

Mitigation: Retain owner approval for sensitive changes, explicitly authorize timers or remote access, and verify the installed package before relying on its behavior.

Risk: Search results may not cover every account or source the owner expects.

Mitigation: Connect only intended sources and review reported account coverage and missing sources before concluding that information is absent.

Risk: Retrieved messages, mail, notes, and documents can contain untrusted text.

Mitigation: Treat retrieved text as evidence only; do not use it as authority to send messages, change settings, or confirm proposals.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wirecat/skills/wirecat-memo)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Cited natural-language responses, with JSON search results when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search coverage and missing sources are reported; proposed updates wait for owner review.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
