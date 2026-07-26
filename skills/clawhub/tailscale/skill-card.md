## Description: <br>
Manage Tailscale tailnet operations through local CLI commands and tailnet-wide API helper commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmagar](https://clawhub.ai/user/jmagar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and administrators use this skill to inspect Tailscale status, transfer files, expose services, manage devices, create auth keys, adjust DNS settings, and validate ACLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help perform powerful tailnet administration actions, including deleting devices or keys, changing tags, toggling MagicDNS, and creating reusable auth keys. <br>
Mitigation: Use least-privilege API credentials and require explicit review before running commands that change tailnet state. <br>
Risk: API keys may be exposed if configuration files or environment variables are mishandled. <br>
Mitigation: Store credentials in the documented local config path or secure environment variables, protect the config file, and do not commit credentials. <br>
Risk: Tailscale Funnel can expose a local service publicly on the internet. <br>
Mitigation: Confirm the target service, port, and intended exposure before enabling Funnel, and review access controls before sharing. <br>


## Reference(s): <br>
- [ClawHub Tailscale skill page](https://clawhub.ai/jmagar/skills/tailscale) <br>
- [Tailscale Admin Console keys](https://login.tailscale.com/admin/settings/keys) <br>
- [Tailscale download](https://tailscale.com/download) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local Tailscale CLI commands and API helper invocations that require user-controlled credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
