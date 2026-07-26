## Description: <br>
媒体服务器控制 is a Jellyfin media-server control skill for searching media, resuming playback, discovering a controllable device, and issuing playback or TV-control commands for home entertainment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and home media enthusiasts use this skill to control a Jellyfin setup through an agent, including media search, playback, resume behavior, and single-device TV controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests Jellyfin and optional Home Assistant credentials that can affect media sessions or smart-home devices. <br>
Mitigation: Use limited-scope tokens where possible, keep credentials out of logs and shared prompts, and rotate exposed credentials. <br>
Risk: Generated playback, launch, power, or volume commands may target the wrong device or session if configuration is broad or stale. <br>
Mitigation: Confirm the target Jellyfin session and TV device before allowing execution, especially when power or playback commands are involved. <br>
Risk: The security evidence flags overly broad and partly mismatched invocation instructions. <br>
Mitigation: Review proposed commands before execution and test configuration on a trusted local network before routine use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/jellyfin-control-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose commands that require Jellyfin, local network, and optional smart-home credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
