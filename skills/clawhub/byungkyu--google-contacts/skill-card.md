## Description:

Google Contacts integration that helps agents manage contacts, contact groups, and address-book search through Maton-managed OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search, read, create, update, and delete Google Contacts records and contact groups from an authorized Google account. It is suited for address-book maintenance and contact lookup workflows where the user has approved the Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Contacts data is routed through Maton as part of normal operation.

Mitigation: Install and use the skill only when that routing is acceptable for the account and data involved.

Risk: Overbroad authorization can expose more contacts data than the task needs.

Mitigation: Use OAuth with the narrowest available scopes, connect only the needed account, and specify the intended connection when multiple accounts exist.

Risk: Create, update, and delete actions can modify or remove address-book records.

Mitigation: Default to read and list calls first, then confirm the exact target, payload, and effect before every write or deletion.

Risk: Full address-book exports can unnecessarily expose personal data.

Mitigation: Request only the fields needed for the task and avoid full exports unless the user explicitly asks for them.

Risk: Maton package installation introduces normal supply-chain exposure.

Mitigation: Pin or verify Maton CLI and SDK packages before installation when the environment requires tighter control.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-contacts)
- [Maton Homepage](https://maton.ai)
- [Google People API Overview](https://developers.google.com/people/api/rest)
- [People Resource](https://developers.google.com/people/api/rest/v1/people)
- [Contact Groups Resource](https://developers.google.com/people/api/rest/v1/contactGroups)
- [Person Fields Reference](https://developers.google.com/people/api/rest/v1/people#Person)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Google Contacts API guidance and Maton CLI or SDK calls; API responses may contain personal contact data.]

## Skill Version(s):

1.2.1 (source: server release metadata; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
