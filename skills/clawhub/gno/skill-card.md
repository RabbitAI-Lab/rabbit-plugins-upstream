## Description:

Helps agents index and search local documents, notes, and session archives and answer questions using retrieved evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmickel](https://clawhub.ai/user/gmickel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask agents to index chosen local files, retrieve relevant documents or past session context, and prepare answers with citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing local files or session archives can expose sensitive material to agent retrieval.

Mitigation: Choose collections and archive sources deliberately; do not index secrets unless intended.

Risk: Write permissions, forced actions, or automation can modify local content or import sessions unexpectedly.

Mitigation: Preview and scope writes and automation before enabling or running them.

Risk: Publishing exports can share indexed information beyond the local machine.

Mitigation: Review exported contents and intended audience before publishing.

## Reference(s):

- [GNO on ClawHub](https://clawhub.ai/gmickel/skills/gno)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Natural-language responses with citations and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Citations can point to indexed local sources.]

## Skill Version(s):

1.2.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
