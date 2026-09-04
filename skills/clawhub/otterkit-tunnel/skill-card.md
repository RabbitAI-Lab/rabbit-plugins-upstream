## Description:

Expose a local port to the internet via OtterKit tunnel, or create a webhook endpoint to capture incoming HTTP requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shivamanupadi](https://clawhub.ai/user/shivamanupadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create public HTTPS tunnels or webhook endpoints for local services, OpenClaw gateway webhooks, and webhook capture, replay, forwarding, and debugging workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public tunnels or webhook endpoints can expose local services to the internet.

Mitigation: Expose only intended services, avoid admin or unauthenticated local targets, use HTTP Basic auth or provider signature verification, prefer short TTLs, and stop tunnels when public access is no longer needed.

Risk: OtterKit credentials and tokens grant account access for tunnel and webhook provisioning.

Mitigation: Protect ~/.otterkit/credentials.json and OTTERKIT_TOKEN like account secrets and use headless tokens only where needed.

## Reference(s):

- [OtterKit Documentation](https://www.otterkit.com/docs)
- [OtterKit Tunnel on ClawHub](https://clawhub.ai/shivamanupadi/skills/otterkit-tunnel)
- [Publisher Profile](https://clawhub.ai/user/shivamanupadi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON-oriented CLI usage guidance for scripting with OtterKit commands.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
