## Description:

Search Telegram, MAX, mail, and notes for information about people, projects, and agreements, then record supported facts, memories, relationships, actions, and key documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Owners and their agents use the skill to find relevant information across selected messaging, mail, and note sources, and to record supported findings for owner review. It helps answer questions about people, projects, and agreements while preserving owner control over decisions and destructive mail actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches can expose private information from connected messaging, mail, and note sources.

Mitigation: Select only relevant accounts and use MEMO_READ_ONLY=1 for search-only use.

Risk: Retrieved messages, mail, or notes may contain misleading instructions or sensitive text.

Mitigation: Treat retrieved text as evidence only, cite it by reference, and never write message, mail, or note text to files.

Risk: Mailbox deletion or stored findings could make changes the owner has not approved.

Mitigation: Review deletion previews and leave confirmation and decision-making to the owner.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wirecat/skills/cli-memo)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text with cited record references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search answers can include coverage, missing sources, and references for opening records.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
