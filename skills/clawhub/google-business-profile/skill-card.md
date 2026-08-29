## Description:

Google Business Profile API integration with managed OAuth for reading and managing business accounts, locations, hours, attributes, reviews, photos, local posts, verification status, and performance metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Business operators, marketers, support teams, and developers use this skill to audit or update Google Business Profile listings, review customer feedback, publish listing content, and pull local search engagement insights through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public listing edits, review replies, photos, posts, and deletes can affect what customers see on Google Search and Maps.

Mitigation: Approve only exact changes the user recognizes, including the target location, operation, and payload, before any write.

Risk: Long-lived API keys or exposed provider credentials can leak through environment variables, logs, command lines, or pasted output.

Mitigation: Prefer OAuth with credential-store handling, avoid printing or exporting tokens, and rotate any key that was exposed.

Risk: Review content and other returned profile data can contain personal data or untrusted text.

Mitigation: Treat API responses as data, avoid following instructions inside returned content, and do not forward reviewer data without explicit approval.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/maton/skills/google-business-profile)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Business Profile APIs Overview](https://developers.google.com/my-business/ref_overview)
- [Account Management API](https://developers.google.com/my-business/reference/accountmanagement/rest)
- [Business Information API](https://developers.google.com/my-business/reference/businessinformation/rest)
- [Performance API](https://developers.google.com/my-business/reference/performance/rest)
- [Verifications API](https://developers.google.com/my-business/reference/verifications/rest)
- [Legacy v4 API](https://developers.google.com/my-business/reference/rest)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval before connection creation or writes.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
