## Description:

Set up a local webhook server to receive Nansen smart alerts in real-time with HMAC signature verification and public tunneling. Use when a user wants to listen for alerts on their local machine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Nansen smart alerts can set up a local receiver to verify incoming webhook signatures and view alert payloads, with optional forwarding of verified events to a local OpenClaw Gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags the optional unversioned `npx localtunnel` command as a medium-confidence concern, and the scan is partial.

Mitigation: Prefer the documented ngrok option, or review the package before running localtunnel; consider the security assessment a review signal rather than proof of malicious intent.

Risk: The public tunnel exposes a reachable URL, so requests can reach the local listener even though unsigned requests are rejected.

Mitigation: Keep HMAC-SHA256 signature verification enabled, retain the localhost-only binding, and stop the tunnel when finished.

Risk: Optional OpenClaw forwarding sends verified alert contents to a local Gateway and may include an authorization token.

Mitigation: Enable forwarding only when needed and configure the Gateway URL and token deliberately.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-alerts-webhook-listener)
- [Nansen CLI browser login platform scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown setup instructions with JavaScript server code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local webhook server template and optional OpenClaw forwarding setup.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
