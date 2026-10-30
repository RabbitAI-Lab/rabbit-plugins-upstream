## Description:

Guides developers in sending browser Web Push notifications from Go services with VAPID, encrypted payloads, subscription storage, and browser-side setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to build or migrate Go backends for browser push notifications, including VAPID setup, browser subscriptions, Postgres storage, and delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Subscriber-provided endpoints could direct server requests to unintended destinations.

Mitigation: Restrict delivery to approved push services and validate resolved addresses and redirects before sending.

Risk: Example API calls or quiet-mode behavior may be incorrect for the deployed library and notification platform.

Mitigation: Review and correct the library calls and notification behavior against the deployed versions before use.

Risk: Exposure of private VAPID keys could allow unauthorized use of the push identity.

Mitigation: Keep private VAPID keys in protected server-side secrets and never expose them to browser clients.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/web-push-go)
- [webpush-go API reference](artifact/references/go-api.md)
- [Browser-side Web Push reference](artifact/references/browser-side.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go, JavaScript, SQL, and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples should be adapted and reviewed for the target application before deployment.]

## Skill Version(s):

1.0.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
