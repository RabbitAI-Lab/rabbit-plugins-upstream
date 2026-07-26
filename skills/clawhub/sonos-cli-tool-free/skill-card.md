## Description: <br>
Helps an agent control Sonos speakers through command-line workflows for playback, volume, grouping, status checks, alarms, and sleep timers in a personal home Sonos setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal Sonos users and developers use this skill to have an agent prepare or execute local CLI workflows for discovering speakers, controlling playback and volume, managing room groups, checking state, and setting alarms or sleep timers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording and immediate Sonos device-control instructions could cause accidental playback, volume, grouping, alarm, or timer changes. <br>
Mitigation: Constrain when the skill activates and require explicit user confirmation before any playback, volume, grouping, alarm, or timer command is executed. <br>
Risk: The skill asks users to install global npm or pip CLI dependencies before controlling local speakers. <br>
Mitigation: Verify the package source before installation and prefer a controlled environment for testing the CLI dependency. <br>
Risk: Commands interact with Sonos devices over the local network and can affect shared household audio devices. <br>
Mitigation: Confirm target room names, device groups, and volume levels before executing commands, especially for grouped playback or scheduled actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/sonos-cli-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON, text, or CSV command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute local Sonos CLI commands and device configuration examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
