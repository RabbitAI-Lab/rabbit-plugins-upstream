## Description: <br>
Securely expose an OpenClaw Gateway WebUI on a VPS via Cloudflare Zero Trust Access + Cloudflare Tunnel (cloudflared), including DNS cutover for custom hostnames and optional cleanup of Tailscale Serve. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jskoiz](https://clawhub.ai/user/jskoiz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to publish an OpenClaw Gateway WebUI through Cloudflare Tunnel while protecting the hostname with Cloudflare Access. It also helps manage DNS cutover and related VPS service setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The DNS helper can create, update, and delete records for the configured Cloudflare zone. <br>
Mitigation: Use a zone-scoped Cloudflare API token with only Zone:DNS:Edit and Zone:Zone:Read, and inspect or back up existing DNS records before cutover. <br>
Risk: The tunnel service exposes a public hostname that depends on Cloudflare Access policy correctness. <br>
Mitigation: Create and verify the Cloudflare Access allowlist and block policy before relying on the hostname. <br>
Risk: The install script downloads and installs the cloudflared package on the VPS. <br>
Mitigation: Verify the cloudflared package source according to local supply-chain controls before installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jskoiz/skills/openclaw-cloudflare-secure) <br>
- [Cloudflare API endpoint used by DNS helper](https://api.cloudflare.com/client/v4) <br>
- [cloudflared Linux AMD64 package source](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline bash code blocks and bundled helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Cloudflare account access, a zone-scoped Cloudflare API token, a Cloudflare Tunnel token, and VPS shell access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
