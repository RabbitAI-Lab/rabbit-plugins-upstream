## Description:

Resend API integration with managed authentication for sending transactional emails and managing domains, contacts, templates, broadcasts, webhooks, and API keys through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with a connected Resend account from an agent: listing resources first, then sending email or managing domains, contacts, templates, broadcasts, webhooks, and API keys after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize access to a Resend account through Maton.

Mitigation: Install only when comfortable authorizing Maton access, review connection scope, use the intended connection when multiple accounts exist, and require clear confirmation before creating a connection.

Risk: Email sends, broadcasts, domain changes, contact updates, API-key operations, deletions, and webhook configuration can create external side effects or data loss.

Mitigation: Default to read and list calls, then confirm the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE operation.

Risk: Maton or provider-issued credentials could be exposed if printed, logged, persisted, or passed on a command line.

Mitigation: Prefer OAuth-backed CLI authentication, do not inspect or store credentials, and use the documented stdin-based raw HTTP fallback only when the CLI cannot be installed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/resend-api)
- [Maton Homepage](https://maton.ai)
- [Resend API Documentation](https://resend.com/docs/api-reference/introduction)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Resend connection; write operations require explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata; artifact frontmatter lists 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
