## Description: <br>
Control Home Assistant smart home devices, lights, scenes, and automations via the moltbot-ha CLI with configurable safety confirmations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iamvaleriofantozzi](https://clawhub.ai/user/iamvaleriofantozzi) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, smart-home administrators, and agent operators use this skill to let an agent inspect and control Home Assistant devices, scenes, automations, and configuration through the moltbot-ha CLI. It is suited for agent-assisted smart-home workflows that need explicit safety confirmations for critical actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent-issued Home Assistant commands can affect physical devices, access controls, alarms, covers, climate, appliances, and scenes. <br>
Mitigation: Keep safety enabled, require confirmation for critical or broad write actions, and do not use --force without explicit user approval. <br>
Risk: A broad Home Assistant token or unrestricted entity set can give an agent excessive smart-home control. <br>
Mitigation: Use a dedicated Home Assistant token where possible, prefer HA_TOKEN over storing the token in config, configure allowed_entities and blocked_entities, and expand critical_domains or safety level for sensitive domains. <br>
Risk: Incorrect URLs, revoked tokens, or unreachable Home Assistant instances can cause failed or misleading control attempts. <br>
Mitigation: Run moltbot-ha test, verify HA_URL and HA_TOKEN, and review action logs during setup. <br>


## Reference(s): <br>
- [Moltbot Home Assistant ClawHub Skill](https://clawhub.ai/iamvaleriofantozzi/skills/moltbot-ha) <br>
- [Home Assistant REST API Docs](https://developers.home-assistant.io/docs/api/rest/) <br>
- [Moltbot Documentation](https://docs.molt.bot/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Home Assistant CLI commands, JSON output requests, and safety confirmation guidance.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata and CHANGELOG, released 2026-02-02) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
