## Description:

Helps an agent work with HoneyBook client-portal data such as vendor files, contracts, invoices, signing links, and payment links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect HoneyBook wedding-vendor portal status, summarize shared files, identify unsigned contracts or open invoices, and return portal deep links for user-confirmed signing or payment actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HoneyBook magic links, cached sessions, payment methods, contracts, and invoice links can expose sensitive account or transaction material.

Mitigation: Treat these values as sensitive, share only what is necessary for the user's request, and avoid exposing session details in unrelated responses.

Risk: Signing or payment deep links could be used for the wrong vendor or document if context is mixed across portal sessions.

Mitigation: Confirm the vendor, document, and requested action with the user before returning or using signing and payment links.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text with HoneyBook portal status, file summaries, and deep-link guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Signing and payment links require explicit user confirmation before use.]

## Skill Version(s):

0.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
