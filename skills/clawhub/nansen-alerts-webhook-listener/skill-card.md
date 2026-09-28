## Description:

Sets up a local listener for Nansen smart alerts with webhook signature verification and public tunneling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Nansen users can set up a local, signature-verified webhook endpoint to receive smart alerts and optionally forward verified alerts to OpenClaw. The skill does not create or modify alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A public tunnel exposes the local listener to internet traffic.

Mitigation: Confirm exposure with the user, bind locally, verify webhook signatures, limit request size, and stop the tunnel when finished.

Risk: Optional localtunnel use via unpinned npx introduces a dependency risk.

Mitigation: Prefer ngrok; if using localtunnel, install or pin a trusted version instead of running unpinned npx.

Risk: Forwarded verified alerts can trigger OpenClaw agent turns.

Mitigation: Enable forwarding only after checking the gateway URL and authentication token.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nansen-devops/skills/nansen-alerts-webhook-listener)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with JavaScript and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local Node.js webhook listener and provides setup and alert-configuration steps.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
