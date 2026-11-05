## Description:

Find what the owner knows about a person or a project across Telegram, MAX, mail and notes through memo, and record facts, memories and key documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can search personal messages, mail, notes, meetings, and project records to answer questions about people, projects, and past decisions. They can also stage cited facts and findings for the owner's review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches can expose private messages, mail, notes, and other personal records to the agent.

Mitigation: Choose the accounts the agent may search and keep each read scoped to the owner's selected sources.

Risk: Proposed facts, meeting findings, or financial records could be inaccurate if accepted without review.

Mitigation: Review the cited evidence and leave confirmation of proposals and financial records to the owner.

Risk: Remote MCP access and scheduled runs can act under configured permissions; MCP's ask setting does not prompt interactively.

Mitigation: Enable remote access and scheduling deliberately, and check the configured permissions before use.

Risk: The separately installed CLI package and its runtime safeguards were outside this artifact review.

Mitigation: Review the installed package and its runtime permissions before granting access to personal records.

## Reference(s):

- [Cli Memo on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-memo)
- [WireCat publisher profile](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Text or Markdown answers with source references and inline CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers preserve source references; proposed changes wait for owner review.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
