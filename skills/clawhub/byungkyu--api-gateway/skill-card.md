## Description:

API Gateway helps agents call third-party services through the Maton gateway using app connections the user has already authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to route concrete tasks to connected apps, such as reading mail, querying CRMs, filing issues, updating spreadsheets, or managing approved event automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad connected-app access can modify real accounts, publish content, send communications, or affect billing.

Mitigation: Default to read and list calls, verify the target account and resource first, and require explicit user confirmation before any write or high-impact operation.

Risk: Trigger destinations and webhooks can create persistent forwarding of event data to external URLs.

Mitigation: Require isolated approval for the exact destination URL, disclose what data will flow there, avoid embedding credentials, and delete destinations when no longer needed.

Risk: Local --exec handlers run code on untrusted event payloads.

Mitigation: Use only user-authored or user-reviewed handlers, get separate approval before starting a watcher, and pass event data as discrete arguments rather than shell-interpolated strings.

Risk: Maton or provider credentials could leak through logs, command lines, destinations, or raw HTTP fallback flows.

Mitigation: Prefer OAuth and the operating system credential store, never print or extract stored credentials, and use raw API keys only when the CLI is unavailable.

Risk: Hosted functions run with the Maton account identity that deployed them.

Mitigation: Deploy or invoke functions only after a least-privilege review of the handler, connected accounts, and network policy; prefer DENY_ALL network policy unless specific hosts are approved.

## Reference(s):

- [API Gateway on ClawHub](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Supported App References](references/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target Maton-connected apps and require explicit user confirmation before writes, connection changes, triggers, destinations, functions, or local event handlers.]

## Skill Version(s):

1.2.22 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
