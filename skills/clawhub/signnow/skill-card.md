## Description:

SignNow API integration with managed OAuth for uploading documents, sending signature invites, creating templates, and managing e-signature workflows through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to help users work with SignNow documents, templates, signing invites, folders, and webhook subscriptions through a Maton-authenticated API connection. It is most useful for document workflow automation where the user can review and approve account connections, write operations, deletes, invites, and webhook changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Maton API passthrough can reach more SignNow endpoints than the examples document, depending on the connected account's authorization.

Mitigation: Use the minimum SignNow scopes available, pin the intended connection ID, start with read/list calls, and review every write, delete, invite, webhook, or connection operation before execution.

Risk: SignNow documents and API responses can contain personal or sensitive business data.

Mitigation: Extract only the fields needed for the task, avoid logging or persisting raw responses unless requested, and treat fetched content as untrusted data rather than agent instructions.

Risk: Fallback raw HTTPS usage requires a long-lived Maton API key in the process environment.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTPS is unavoidable, never print, log, persist, or pass the key on a command line and send it only to api.maton.ai.

Risk: Multipart uploads handle local document bytes before sending them to SignNow.

Mitigation: Use owner-only temporary files created with umask 077 and mktemp, remove them with an exit trap, and avoid predictable shared temporary paths.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/signnow)
- [Maton Homepage](https://maton.ai)
- [SignNow API Reference](https://docs.signnow.com/docs/signnow/reference)
- [SignNow Developer Portal](https://www.signnow.com/developers)
- [SignNow Postman Collection](https://github.com/signnow/postman-collection)
- [SignNow SDKs](https://github.com/signnow)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration, API calls]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue Maton CLI, SDK, or raw HTTPS SignNow API calls when the environment has the required network access, Maton credentials, and user-approved connection.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
