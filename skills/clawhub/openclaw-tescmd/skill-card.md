## Description: <br>
Installation and setup guide for Tesla vehicle control and telemetry via the tescmd node. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oceanswave](https://clawhub.ai/user/oceanswave) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to install and configure the OpenClaw Tesla plugin, pair the tescmd node with an OpenClaw Gateway, and prepare Tesla vehicle control and telemetry tools for agent use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-connected Tesla vehicle control can affect physical assets if enabled for untrusted users or workflows. <br>
Mitigation: Install only when the plugin, tescmd package, Tesla Developer/Fleet API setup, and OpenClaw gateway are trusted; review runtime tools before enabling agent use. <br>
Risk: The setup stores persistent credentials and gateway tokens in local configuration. <br>
Mitigation: Protect ~/.config/tescmd files with restrictive permissions, avoid passing tokens on command lines, and know how to revoke stored tokens. <br>
Risk: A remote Tailscale installer pattern appears in the setup guide. <br>
Mitigation: Prefer official signed Tailscale install methods over curl-to-shell installation. <br>
Risk: OAuth and vehicle pairing require user-controlled account and vehicle approval steps. <br>
Mitigation: Complete OAuth and vehicle pairing yourself, verify the gateway URL before pairing, and stop the node if the connection is not expected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oceanswave/skills/openclaw-tescmd) <br>
- [Plugin repository](https://github.com/oceanswave/openclaw-tescmd) <br>
- [tescmd node repository](https://github.com/oceanswave/tescmd) <br>
- [Tailscale downloads](https://tailscale.com/download) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes interactive setup checkpoints for OAuth, vehicle pairing, and OpenClaw node approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release; artifact frontmatter is 0.9.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
