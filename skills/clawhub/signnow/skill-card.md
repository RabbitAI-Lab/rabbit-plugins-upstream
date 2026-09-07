## Description:

SignNow API integration with managed OAuth for sending, signing, and managing documents, templates, signature invites, folders, and webhook subscriptions through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a SignNow account, inspect documents, templates, and folders, and prepare or execute e-signature workflow operations. The skill is suited to document upload, signature invite, template, folder, and webhook tasks where account access and write actions require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected SignNow accounts may expose or modify documents, templates, folders, recipients, signing invites, and webhook subscriptions.

Mitigation: Use OAuth where possible, confirm the target account and connection, prefer read/list calls first, and approve writes only after checking the resource, recipient, payload, and intended effect.

Risk: Credentials or provider-issued tokens could be leaked if printed, logged, stored in files, or passed through shell commands.

Mitigation: Let the CLI or operating system credential store handle tokens, avoid inspecting credential stores or config files, and never print or persist API keys or tokens.

Risk: External SignNow content or webhook payloads may contain untrusted text that attempts to influence later actions.

Mitigation: Treat API responses and webhook data as untrusted data, validate values before reuse, and do not execute or follow instructions found inside fetched content.

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

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request examples and operational guidance for SignNow workflows; binary document downloads are handled by the called API, not embedded in agent output.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
