## Description: <br>
Build or update the BlueBubbles external channel plugin for Clawdbot, including the extension package, REST send and probe helpers, and webhook inbound handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kevin19830331](https://clawhub.ai/user/kevin19830331) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill when building or maintaining a BlueBubbles messaging bridge for Clawdbot. It guides work on plugin layout, REST health checks and delivery, webhook ingestion, reactions, typing and read state, and inbound media handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The BlueBubbles bridge uses sensitive messaging configuration, including a server URL, password, and webhook endpoint. <br>
Mitigation: Protect the BlueBubbles password, restrict access to the webhook endpoint, and confirm configuration before enabling the plugin. <br>
Risk: Message, reaction, read or typing state, and media handling can affect real conversations if implemented incorrectly. <br>
Mitigation: Review message routing, reaction targets, read and typing behavior, and media attachment handling before using the plugin in a live deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kevin19830331/skills/bluebubbles) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, configuration] <br>
**Output Format:** [Markdown guidance with file paths, helper names, and configuration keys] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only helper; review generated or modified plugin code before deployment.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
