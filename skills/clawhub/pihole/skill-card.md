## Description: <br>
Pi-hole Control helps an agent check Pi-hole status and statistics, enable or disable DNS blocking, and inspect recently blocked domains through the Pi-hole v6 API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baanish](https://clawhub.ai/user/baanish) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Use this skill when an agent is authorized to operate a user's Pi-hole instance, review DNS blocking status, temporarily disable or re-enable blocking, and summarize blocked-domain activity for troubleshooting. <br>

### Deployment Geography for Use: <br>
No geographic restriction is specified in the evidence; deployment depends on the user's reachable Pi-hole network environment and local operational requirements. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can disable DNS blocking for the whole network. <br>
Mitigation: Use it only in environments where the agent is authorized to control Pi-hole, and review off or disable actions before execution. <br>
Risk: Credential and transport choices can expose Pi-hole access if HTTP or disabled certificate validation is used. <br>
Mitigation: Prefer HTTPS with certificate validation, avoid insecure mode except on trusted local setups, and rotate the Pi-hole app password after testing with weaker transport settings. <br>
Risk: The security evidence flags the release as needing review because credential and transport risks are under-disclosed. <br>
Mitigation: Review the skill and its configuration before deployment, and confirm the configured API endpoint, credential storage, and network access controls meet local requirements. <br>


## Reference(s): <br>
- [Pi-hole Control on ClawHub](https://clawhub.ai/baanish/skills/pihole) <br>
- [Publisher profile](https://clawhub.ai/user/baanish) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain-text command responses, status summaries, statistics, blocked-domain lists, and setup snippets for Pi-hole API configuration.] <br>
**Output Parameters:** [Pi-hole API URL, Pi-hole app password or API token, optional certificate-validation setting, command name, optional duration, optional query window, and optional result limit.] <br>
**Other Properties Related to Output:** [The skill uses session-based Pi-hole v6 API access and can change network-wide DNS blocking state, so it should be used only with explicit operator authorization.] <br>

## Skill Version(s): <br>
2.0.1 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
