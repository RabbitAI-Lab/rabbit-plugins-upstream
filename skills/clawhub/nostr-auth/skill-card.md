## Description:

Nostr Auth helps agents authenticate to Nostr sign-in challenges by signing kind-22242 AUTH events with a locally derived secp256k1 key and optionally submitting them to a service callback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dyegolara](https://clawhub.ai/user/dyegolara)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a site or API asks for a signed Nostr event to prove key ownership. It supports inspecting a signed event first and then submitting it to an expected callback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates or uses a local agent Nostr identity that can authenticate to services when given a challenge and callback.

Mitigation: Use dry-run first, inspect the signed event, and verify that the callback URL belongs to the intended service before submitting.

Risk: Using a valuable personal Nostr private key would cause the helper to authenticate as that identity.

Mitigation: Use the generated local agent identity unless intentionally reusing an existing personal identity.

Risk: Signed events are sent to a user-specified callback URL.

Mitigation: Confirm the callback URL before execution and avoid submitting to unexpected or untrusted endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dyegolara/skills/nostr-auth)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and may use NOSTR_AUTH_KEYFILE for the persistent local master secret.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
