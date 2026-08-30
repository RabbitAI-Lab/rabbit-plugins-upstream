## Description:

This skill helps an agent work with OurFamilyWizard co-parenting data, including messages, calendar events, expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their own OurFamilyWizard account for co-parenting workflows such as reviewing messages, managing drafts, checking events, tracking expenses, and creating journal entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration handles sensitive family and legal-record data from an OFW account.

Mitigation: Install it only for an account you control, keep credentials private, and use a dedicated configuration with the narrowest available access posture.

Risk: Some actions can change records or create visible effects, including sending messages, deleting items, creating records, or reading unread messages that can generate a visible read receipt.

Mitigation: Require explicit user review before write actions or unread-message reads, and prefer draft-only or read-only workflows where available.

Risk: Cached OFW data can be stale or incomplete, which can lead to incorrect status summaries.

Mitigation: Check freshness, completion, pagination, and live status fields before presenting current OFW state as fact.

## Reference(s):

- [OFW skill page](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)
- [ofw-mcp source repository linked by skill documentation](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON snippets, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool names, configuration snippets, status summaries, draft guidance, and user-confirmation prompts.]

## Skill Version(s):

2.13.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
