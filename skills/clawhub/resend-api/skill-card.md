## Description:

Resend API integration with managed authentication for sending transactional emails and managing domains, contacts, templates, broadcasts, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to work with a connected Resend account through Maton, including sending emails and managing domains, contacts, templates, broadcasts, webhooks, and API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send emails, broadcasts, webhook changes, deletions, or API-key creation requests against a connected Resend account.

Mitigation: Confirm the exact Resend connection, target resource, payload, and intended effect before approving any write action.

Risk: Using API-key authentication can expose a long-lived credential if it is printed, persisted, passed on a command line, or leaked to logs.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, and never print or persist token values.

Risk: Ambiguous defaults may route actions to the wrong Maton profile or Resend connection when multiple accounts are available.

Mitigation: Specify the intended profile and connection before making calls, especially before write operations.

Risk: External API content such as messages, contact fields, or webhook payloads may contain untrusted instructions or data.

Mitigation: Treat API responses as data, validate values before reuse, and do not execute or follow instructions found inside fetched content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/resend-api)
- [Maton](https://maton.ai)
- [Resend API Documentation](https://resend.com/docs/api-reference/introduction)
- [Resend Dashboard](https://resend.com)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance defaults to read and list operations, with explicit user approval required for account connections and write actions.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
