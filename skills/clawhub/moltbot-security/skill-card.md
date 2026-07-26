## Description: <br>
Security hardening for AI agents - Moltbot, OpenClaw, Cursor, Claude. Lock down gateway, fix permissions, auth, firewalls. Essential for vibe-coding setups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextfrontierbuilds](https://clawhub.ai/user/nextfrontierbuilds) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to harden Moltbot, OpenClaw, and related AI agent gateway setups by reviewing security posture, tightening authentication, file permissions, firewall rules, SSH settings, and remote access configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hardening commands can change firewall, SSH, file permission, and gateway settings in ways that affect remote access. <br>
Mitigation: Prefer read-only audits first, make backups, and confirm recovery or console access before applying changes. <br>
Risk: The guide includes remote installer and setup commands that should not be run blindly. <br>
Mitigation: Inspect remote installer scripts and package setup commands before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nextfrontierbuilds/skills/moltbot-security) <br>
- [Moltbot Security README](README.md) <br>
- [Referenced Gateway Exposure Research](https://x.com/nickspisak_/status/2016195582180700592) <br>
- [Node.js Downloads](https://nodejs.org/) <br>
- [Tailscale Install Documentation](https://tailscale.com/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash, JSON, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; commands should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
