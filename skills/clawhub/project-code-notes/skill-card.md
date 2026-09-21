## Description:

Combines prepare project context from an intake note with build a delivery ledger entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations and implementation teams use this skill to turn project intake notes into structured project context and account-facing delivery ledger entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project intake notes may contain confidential client or account details.

Mitigation: Only provide details needed for the requested project context or delivery entry, and omit unnecessary confidential information.

Risk: Delivery ledger entries can become misleading if the source project context is incomplete or stale.

Mitigation: Review generated entries against the current intake note or handoff before sharing them with account-facing teams.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/project-code-notes)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text containing project context and delivery ledger entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consumes project intake notes or prepared project context and produces a requested delivery operations result.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
