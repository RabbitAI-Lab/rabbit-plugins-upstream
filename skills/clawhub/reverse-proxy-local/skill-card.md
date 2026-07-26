## Description: <br>
Connects OpenClaw to the internet via Tailscale Funnel with bearer-token access to OpenAI-compatible API endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tsheasha](https://clawhub.ai/user/tsheasha) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to expose a local OpenClaw gateway through Tailscale Funnel, check connection status, disable public access, and package API credentials for another user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill intentionally exposes an OpenClaw API endpoint to the public internet. <br>
Mitigation: Install it only when public remote access is intended, confirm the Tailscale Funnel endpoint, and keep bearer-token authentication enabled. <br>
Risk: The generated bearer token grants live remote API access and can be copied into a shareable package. <br>
Mitigation: Share credentials only with trusted recipients and regenerate or revoke the token immediately after sharing is no longer needed. <br>
Risk: The setup scripts make high-impact network and system changes, including sudo Tailscale commands, package installation, OpenClaw config changes, and gateway restarts. <br>
Mitigation: Review each install, sudo, and configuration-change step before running the scripts on the intended macOS OpenClaw host. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tsheasha/skills/reverse-proxy-local) <br>
- [Publisher profile](https://clawhub.ai/user/tsheasha) <br>
- [Tailscale](https://tailscale.com) <br>
- [Tailscale Funnel admin](https://login.tailscale.com/admin/machines) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON credential examples, and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Targets macOS with Homebrew, Tailscale, sudo access, and OpenClaw installed; produces and uses a local credentials JSON file for API access.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
