## Description:

Read a SimplePractice Client Portal through the simplepractice-mcp server for upcoming appointments, billing records, balance and saved cards, paperwork, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to read SimplePractice client-portal information such as therapy or healthcare appointments, billing documents, forms, saved payment-method summaries, and practice announcements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive healthcare, billing, document, and limited payment-method information from a SimplePractice client portal.

Mitigation: Use it only when the user intends that access, confirm whose record is being discussed when a login covers multiple clients, and report only the information requested.

Risk: Repeated sign-in link requests can trigger rate limits and disrupt the user's only authentication path.

Mitigation: Check session status first, ask before sending a sign-in email, and avoid duplicate requests or retry loops.

Risk: Portal data can be misunderstood, such as treating an empty invoice list as proof that nothing is owed or implying an appointment can be cancelled through the skill.

Mitigation: State only what the portal data supports, distinguish missing portal records from absence of debt, and direct cancellation actions to the portal or practice policy.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text guidance for using SimplePractice portal tools and reporting results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal access; compact and full response views are available for selected read tools.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
