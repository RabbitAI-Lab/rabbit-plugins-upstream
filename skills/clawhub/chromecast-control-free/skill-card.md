## Description: <br>
Controls local-network Chromecast-compatible devices with catt for device discovery, basic media casting, playback control, and volume adjustment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users can use this skill to have an agent discover Chromecast-compatible devices on a trusted local network, cast supported media, and control playback or volume through catt commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Device names, IP addresses, and cast targets on the local network may be exposed in agent output. <br>
Mitigation: Treat discovered local-network identifiers as private and use the skill only on trusted networks. <br>
Risk: Casting local files or media URLs can disclose sensitive content to Chromecast-compatible devices. <br>
Mitigation: Confirm the media path or URL and the intended target device before issuing catt cast commands. <br>
Risk: Opening firewall ports for local file casting can increase local-network exposure. <br>
Mitigation: Open only the required ports on trusted networks and only for the minimum time needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/chromecast-control-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown responses with catt command examples, execution summaries, status, and error details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local device names, IP addresses, command status codes, result data, and execution logs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
