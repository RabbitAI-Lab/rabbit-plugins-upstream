## Description:

Google Business Profile API integration with managed OAuth for reading and managing business accounts, locations, hours, attributes, reviews, photos, local posts, verification status, and performance metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to audit or update Google Business Profile listings, read customer reviews, manage photos and local posts, and retrieve search and engagement insights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Business Profile listing edits, local posts, photos, and review replies can be public-facing or irreversible.

Mitigation: Require the agent to show the exact business location, field, content, and intended effect, then obtain explicit user approval before any public write or deletion.

Risk: OAuth tokens, API keys, and provider-issued credentials could be exposed through logs, files, shell history, or command output.

Mitigation: Prefer OAuth through the Maton CLI, do not print or persist credentials, and send any Maton API key only to api.maton.ai.

Risk: Review text and other API-returned content may contain personal data or adversarial instructions.

Mitigation: Treat returned content as untrusted data, avoid following instructions inside it, and do not forward reviewer data to another host without explicit approval.

Risk: Multiple Maton accounts or Google Business Profile connections can cause reads or writes to target the wrong business.

Mitigation: List and verify the intended account and location first, then pin the appropriate profile or connection before sensitive operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maton/skills/google-business-profile)
- [Maton Homepage](https://maton.ai)
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

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and a Maton account; public writes and new connections require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
