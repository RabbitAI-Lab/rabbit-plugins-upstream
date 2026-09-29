## Description:

Set up a local webhook server to receive Nansen smart alerts in real time with HMAC signature verification and a public tunnel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Nansen users can set up a local listener for signed smart-alert webhooks and optionally forward verified alerts to a local OpenClaw Gateway. The skill provides setup and alert-configuration guidance; it does not create or modify alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A public tunnel exposes a local webhook endpoint to internet traffic.

Mitigation: Confirm before starting, bind the listener to localhost, require a private webhook secret and signature verification, limit request size, and stop the server and tunnel when finished.

Risk: Optional unpinned localtunnel execution adds supply-chain and availability uncertainty.

Mitigation: Prefer ngrok or a pinned, preinstalled tunnel tool; if using localtunnel, monitor availability and update the webhook URL when the tunnel changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-alerts-webhook-listener)
- [Nansen CLI browser-login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with JavaScript and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates a local webhook server script and instructions for running a tunnel and configuring an alert; does not create or change alerts.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
