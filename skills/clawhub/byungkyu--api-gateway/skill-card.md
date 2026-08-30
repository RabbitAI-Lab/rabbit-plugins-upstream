## Description:

Call third-party APIs through the Maton gateway, which injects credentials for apps the user has already connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to route requests to user-connected third-party apps, manage app connections, and set up event triggers or webhook forwarding when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mediate broad access to connected third-party apps, including writes and deletions.

Mitigation: Default to read/list operations and require explicit confirmation of the target service, resource, payload, and intended effect before any write or deletion.

Risk: Webhook destinations can create persistent forwarding of future event data to an external URL.

Mitigation: Create or update destinations only for user-controlled URLs after disclosing the destination, forwarded data, persistence, and any credential use; remove destinations when no longer needed.

Risk: Local --exec event handlers run local code on untrusted event payloads.

Mitigation: Use only user-authored or user-reviewed handlers, require separate approval before starting a watch, and validate event data before it reaches commands or scripts.

Risk: Maton API keys and provider-issued tokens could be exposed through logs, command lines, destination templates, or pasted output.

Mitigation: Prefer OAuth and least-privilege scopes, keep credentials in the credential store or secret manager, never print or persist them, and send them only to the intended Maton endpoint.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway on ClawHub](https://clawhub.ai/byungkyu/skills/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-connected app credentials mediated by Maton.]

## Skill Version(s):

1.0.151 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
