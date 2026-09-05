## Description:

Read a SimplePractice Client Portal (`<practice>.clientsecure.me`) from a shell - appointments, invoices/statements/superbills/receipts, documents to sign, announcements, practice and clinician info - with plain `curl` against its JSON:API, instead of running the simplepractice-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation agents use this skill to read their own SimplePractice Client Portal data from a shell without running the MCP server. It provides curl-first guidance for passwordless sign-in, optional browser-cookie capture, and read-only JSON:API requests for appointments, billing items, documents, announcements, practice details, and clinician details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal responses can contain protected health information and billing data.

Mitigation: Use the skill only for the user's own SimplePractice portal, keep outputs private, and avoid pasting portal data into shared logs or public systems.

Risk: Magic links, PINs, cookie jars, and fpx-captured cookies provide full portal account access.

Mitigation: Treat these values as credentials, keep the cookie jar chmod 600, exclude it from git, and avoid shared machines.

Risk: Repeated failed sign-in requests can trigger email- or IP-scoped rate limits and block the only authentication path.

Mitigation: Do not retry failed sign-ins repeatedly; wait out rate limits and request a fresh token or PIN when needed.

Risk: Using write endpoints could change appointments, payments, signed documents, or messages without normal portal review.

Mitigation: Keep usage to the documented read-only examples and use the web portal for payments, signatures, cancellations, or messages.

## Reference(s):

- [SimplePractice Client Portal request reference](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, curl, jq, and JSON:API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only examples; state-changing portal actions such as payments, signatures, cancellations, and messages are out of scope.]

## Skill Version(s):

0.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
