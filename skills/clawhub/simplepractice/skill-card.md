## Description:

Read a SimplePractice Client Portal through the simplepractice-mcp server to view upcoming appointments, billing records, saved payment cards, paperwork requests, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to ask an agent about their SimplePractice client portal, including appointments, billing documents, balances, saved cards, paperwork, and announcements. It is especially suited to therapy or healthcare portal questions where the agent should report only the requested client information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The portal can expose sensitive health, billing, and family-member records.

Mitigation: Confirm which client record is in use and answer only the user's specific question instead of volunteering unrelated portal data.

Risk: A sign-in link request can send a real email and may be rate-limited.

Mitigation: Check session status first, ask before requesting a new link, and avoid retry loops.

Risk: An empty billing list may be misread as no outstanding balance.

Mitigation: State that no matching billing items were found in the portal rather than concluding that nothing is owed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, API Calls, guidance]

**Output Format:** [Markdown or plain text responses summarizing portal records and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal guidance; compact responses are preferred when supported by the underlying tools.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
