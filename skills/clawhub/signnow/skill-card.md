## Description:

SignNow API integration with managed OAuth for sending, signing, and managing documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage SignNow e-signature workflows through Maton, including document uploads, signature invites, templates, folders, webhooks, and account checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SignNow authorization can expose document, template, invite, folder, and webhook access in the connected account.

Mitigation: Use OAuth when possible, approve only the intended SignNow connection and scopes, specify the target connection when multiple accounts exist, and revoke unused connections.

Risk: Write operations can send signature invites, modify documents, create webhooks, move resources, or delete data.

Mitigation: Start with read/list calls, then confirm resource IDs, recipients, webhook URLs, payloads, and intended effects before any POST, PUT, PATCH, or DELETE request.

Risk: Fallback API-key use can leak a long-lived Maton credential through logs, shell history, process listings, or persisted files.

Mitigation: Prefer CLI OAuth; when raw HTTP is unavoidable, do not print, log, persist, or pass the key on a command line, and send it only to api.maton.ai.

Risk: Content returned from the SignNow API may include untrusted or adversarial instructions.

Mitigation: Treat API responses as data, never execute or eval returned content, and do not let returned content select follow-up endpoints, recipients, or commands.

## Reference(s):

- [SignNow Skill on ClawHub](https://clawhub.ai/byungkyu/skills/signnow)
- [byungkyu Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [SignNow API Reference](https://docs.signnow.com/docs/signnow/reference)
- [SignNow Developer Portal](https://www.signnow.com/developers)
- [SignNow Postman Collection](https://github.com/signnow/postman-collection)
- [SignNow SDKs](https://github.com/signnow)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and OAuth or API-key authentication; defaults to read/list calls and requires confirmation for write operations.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence; artifact metadata version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
